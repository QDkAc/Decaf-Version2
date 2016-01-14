package decaf.tacvm.exec;

import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Memory {
	// the whole logic naming space start from 0
	public static int PAGE_SIZE = 1024;// a page is 1024 ints

	public static int NUM_PAGES = 1 << 15;// number of blocks

	public static int THRESHOLD = PAGE_SIZE / 2;

	public static int MAX_NUM_IDENTIFIERS = 3 << 20;// maximum number of objects

	// vtable: keep the same
	private int[] vtable;

	public void setVTable(int[] vtable) {
		this.vtable = vtable;
	}

	private int accessVTable(int base, int offset) {
		if (base % 4 != 0 || offset < 0 || offset % 4 != 0) {
			throw new ExecuteException("bad vtable access base = " + base
					+ " offset = " + offset);
		}
		base /= 4;
		offset /= 4;
		if (offset >= vtable[base]) {
			throw new ExecuteException("vtable access base = " + base * 4
					+ " offset = " + offset * 4 + " out of bounds");
		}
		return vtable[base + offset + 1];
	}

	// new part
	// the start of block i is i*1024
	private int[] memory = new int[PAGE_SIZE * NUM_PAGES];
	private int[] freePages = new int[NUM_PAGES];
	private int numFreePages;

	private int[] halfPages = new int[NUM_PAGES];
	private int[] halfPageIndex = new int[NUM_PAGES];
	private int numHalfPages;

	private int[] freeIds = new int[MAX_NUM_IDENTIFIERS];
	private boolean[] active = new boolean[MAX_NUM_IDENTIFIERS];
	private int numFreeIds;

	private int[] startAddr = new int[MAX_NUM_IDENTIFIERS];
	private int[] objectSize = new int[MAX_NUM_IDENTIFIERS];

	private int[] next = new int[MAX_NUM_IDENTIFIERS + NUM_PAGES];
	private int[] prev = new int[MAX_NUM_IDENTIFIERS + NUM_PAGES];

	private class ActiveIdList {
		// a double linked list for all active ids
		private int[] next = new int[MAX_NUM_IDENTIFIERS + 1];
		private int[] prev = new int[MAX_NUM_IDENTIFIERS + 1];
		int first;

		public ActiveIdList() {
			first = MAX_NUM_IDENTIFIERS;

			next[first] = first;
			prev[first] = first;
		}

		void add(int x) {
			next[x] = next[first];
			prev[x] = first;

			prev[next[x]] = x;
			next[prev[x]] = x;
		}

		void remove(int x) {
			prev[next[x]] = prev[x];
			next[prev[x]] = next[x];
		}

		int[] getAll() {
			int cnt = 0;
			for (int i = next[first]; i != first; i = next[i]) {
				++cnt;
			}
			int[] ret = new int[cnt];
			cnt = 0;
			for (int i = next[first]; i != first; i = next[i]) {
				ret[cnt++] = i;
			}
			return ret;
		}
	}

	private ActiveIdList activeIdList = new ActiveIdList();

	private PageTable[] pageTable = new PageTable[MAX_NUM_IDENTIFIERS];
	private SmallItemsPage[] myPage = new SmallItemsPage[MAX_NUM_IDENTIFIERS];

	private SmallItemsPage[] pages = new SmallItemsPage[NUM_PAGES];

	// for big object
	private class PageTable {
		int[] pages;

		public PageTable(int numPages) {
			pages = new int[numPages];
			for (int i = 0; i < numPages; i++) {
				pages[i] = getFreePage();
				Arrays.fill(memory, pages[i] << 10, (pages[i] + 1) << 10, 0);
			}
		}

		int logicToPhysic(int at) {
			return (pages[at >> 10] << 10) + (at & 1023);
		}
	}

	//
	private class SmallItemsPage {
		int page;
		int currentAddr;
		int numActiveObject;
		int usedSpace;

		void clear() {
			currentAddr = 0;
			numActiveObject = 0;
			usedSpace = 0;

			// a double linked list of block ids in this page
			int me = page + MAX_NUM_IDENTIFIERS;
			prev[me] = me;
			next[me] = me;
		}

		public SmallItemsPage(int page) {
			this.page = page;
			clear();
		}

		int alloc(int num) {
			int rest = PAGE_SIZE - currentAddr;
			if (rest < num)
				return -1;
			int addr = (page << 10) + currentAddr;
			currentAddr += num;
			numActiveObject++;
			usedSpace += num;

			return addr;
		}

		void recycle(int num) {
			usedSpace -= num;
			numActiveObject--;
		}

	}

	void objectListAdd(int page, int id) {
		int first = page + MAX_NUM_IDENTIFIERS;
		int last = prev[first];

		prev[id] = last;
		next[id] = first;

		prev[next[id]] = id;
		next[prev[id]] = id;
	}

	void objectListRemove(int id) {
		next[prev[id]] = next[id];
		prev[next[id]] = prev[id];
	}

	private void recyclePage(int pageId) {
		freePages[numFreePages++] = pageId;
	}

	private int getFreePage() {
		if (numFreePages == 0) {
			if (numHalfPages >= 2) {
				compacify();
			} else {
				throw new ExecuteException("Insufficent Memory");
			}
		}
		int id = freePages[--numFreePages];
		return id;
	}

	private void recycleId(int id) {
		active[id] = false;
		activeIdList.remove(id);
		freeIds[numFreeIds++] = id;
	}

	private int getFreeId() {
		if (numFreeIds == 0) {
			throw new ExecuteException("Too many objects");
		}

		int id = freeIds[--numFreeIds];
		active[id] = true;
		activeIdList.add(id);
		return id;
	}

	public int[] getAllObject() {
		return activeIdList.getAll();
	}

	void removeHalfPage(int page) {
		// swap with the last one
		assert (halfPageIndex[page] != -1);

		int idx = halfPageIndex[page];
		int last = halfPages[numHalfPages - 1];
		halfPages[idx] = last;
		halfPageIndex[last] = idx;

		--numHalfPages;
		halfPageIndex[page] = -1;
	}

	void addHalfPage(int page) {
		halfPages[numHalfPages] = page;
		halfPageIndex[page] = numHalfPages++;
	}

	int[] tmp = new int[1024];

	void merge(int p1, int p2) {
		SmallItemsPage page1 = pages[p1];
		SmallItemsPage page2 = pages[p2];

		int cnt = 0;
		int first = p1 + MAX_NUM_IDENTIFIERS;
		for (int i = next[first]; i != first; i = next[i]) {
			tmp[cnt++] = i;
		}
		first = p2 + MAX_NUM_IDENTIFIERS;
		for (int i = next[first]; i != first; i = next[i]) {
			tmp[cnt++] = i;
		}

		// remove all these items
		for (int i = 0; i < cnt; i++) {
			objectListRemove(tmp[i]);
		}

		// adding them to page1
		page1.clear();
		for (int i = 0; i < cnt; i++) {
			int id = tmp[i];
			// copying the old space
			int addr = page1.alloc(objectSize[id]);
			System.arraycopy(memory, startAddr[id], memory, addr,
					objectSize[id]);
			startAddr[id] = addr;
			myPage[id] = page1;
			objectListAdd(p1, id);
		}
		// recycle page2
		page2.clear();
		recyclePage(p2);
	}

	void compacify() {
		// if there are two half pages, merge them
		if (numHalfPages >= 2) {
			int p1 = halfPages[numHalfPages - 1];
			int p2 = halfPages[numHalfPages - 2];

			removeHalfPage(p1);
			removeHalfPage(p2);
			merge(p1, p2);

			if (pages[p1].usedSpace <= THRESHOLD)
				addHalfPage(p1);
		}
	}

	private PrintWriter log;

	public Memory(PrintWriter log) {
		this.log = log;
		numFreePages = 0;
		for (int i = 0; i < NUM_PAGES; i++) {
			recyclePage(i);
			pages[i] = new SmallItemsPage(i);

		}
		numFreeIds = 0;
		for (int i = 1; i < MAX_NUM_IDENTIFIERS; i++) {
			freeIds[numFreeIds++] = i;
		}

		numHalfPages = 0;
		Arrays.fill(halfPageIndex, -1);
	}

	SmallItemsPage currentPage;

	public int alloc(int size) {
		if (size < 0 || size % 4 != 0) {
			throw new ExecuteException("bad alloc size = " + size);
		}

		// while (numHalfPages >= 2)
		// compacify();

		size /= 4;

		int id = getFreeId();
		objectSize[id] = size;
		log.println("Allocating size: " + size * 4);

		if (size > THRESHOLD) {// big block
			log.println("\tIt is a big block");
			int numPages = (size + PAGE_SIZE - 1) / PAGE_SIZE;
			PageTable tab = new PageTable(numPages);
			log.println("\t\tAllocated " + numPages + " pages");

			pageTable[id] = tab;
			startAddr[id] = -1;
		} else {// small block
			log.println("\tIt is a small block");
			if (currentPage == null) {
				currentPage = pages[getFreePage()];
				log.println("\t\tUsing a new page " + currentPage.page);
			}
			int addr = currentPage.alloc(size);
			if (addr == -1) {
				// This is possible!
				if (currentPage.usedSpace <= THRESHOLD)
					addHalfPage(currentPage.page);

				currentPage = pages[getFreePage()];
				addr = currentPage.alloc(size);
				log.println("\t\tUsing a new page " + currentPage.page);
			}

			objectListAdd(currentPage.page, id);
			startAddr[id] = addr;
			myPage[id] = currentPage;
			Arrays.fill(memory, addr, addr + size, 0);
			log.println("\t\tstarting physical address: " + addr);
		}
		log.println("\tAllocated to logic address " + id);
		return id;
	}

	private int logicToPhysic(int id, int offset) {
		// System.out.println("idlogic:" + id);
		if (id < 0 || id >= MAX_NUM_IDENTIFIERS || !active[id]
				|| offset % 4 != 0) {
			throw new ExecuteException("bad memory access id = " + id
					+ " offset = " + offset);
		}
		offset /= 4;

		if (offset < 0 || offset >= objectSize[id])
			throw new ExecuteException("memory access id = " + id
					+ " offset = " + offset * 4 + " out of bounds");

		if (startAddr[id] != -1) {
			// small item
			return startAddr[id] + offset;
		} else {
			return pageTable[id].logicToPhysic(offset);
		}
	}

	public int load(int id, int offset) {
		if (id < 0) {
			return accessVTable(-id - 1, offset);
		} else {
			return memory[logicToPhysic(id, offset)];
		}
	}

	public int getBlockSize(int id) {
		if (id < 0 || id >= MAX_NUM_IDENTIFIERS || !active[id]) {
			throw new ExecuteException("bad memory access id = " + id);
		}
		return objectSize[id];
	}

	public void store(int val, int id, int offset) {
		memory[logicToPhysic(id, offset)] = val;
	}

	public void dispose(int id) {
		log.println("Disposing logic address " + id);
		assert (active[id]);

		// while (numHalfPages >= 2)
		// compacify();

		if (startAddr[id] != -1) {
			log.println("\tIt is a small block");
			// smallItem
			SmallItemsPage page = myPage[id];
			page.recycle(objectSize[id]);
			objectListRemove(id);

			assert (page.numActiveObject >= 0);

			if (page.numActiveObject == 0) {
				page.clear();

				if (halfPageIndex[page.page] != -1) {
					removeHalfPage(page.page);
				}

				recyclePage(page.page);
				if (currentPage == page) {
					currentPage = null;
				}
				log.println("\tPage " + page.page
						+ " becomes empty and is recycled.");
			} else if (page != currentPage && page.usedSpace <= THRESHOLD
					&& halfPageIndex[page.page] == -1) {
				addHalfPage(page.page);
			}
		} else {
			log.println("\tIt is a big block");
			PageTable tab = pageTable[id];
			for (int page : tab.pages) {
				recyclePage(page);
				log.println("\t\tRecycled page " + page);
			}
			pageTable[id] = null;
		}

		recycleId(id);
	}
}
