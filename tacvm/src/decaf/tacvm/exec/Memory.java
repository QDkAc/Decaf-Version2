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

	private int[] freeIds = new int[MAX_NUM_IDENTIFIERS];
	private boolean[] active = new boolean[MAX_NUM_IDENTIFIERS];
	private int numFreeIds;

	private int[] startAddr = new int[MAX_NUM_IDENTIFIERS];
	private int[] objectSize = new int[MAX_NUM_IDENTIFIERS];

	private class ActiveIdList {
		// a double linked list for all active ids
		private int[] next = new int[MAX_NUM_IDENTIFIERS + 2];
		private int[] prev = new int[MAX_NUM_IDENTIFIERS + 2];

		int first, last;

		public ActiveIdList() {
			first = MAX_NUM_IDENTIFIERS;
			last = MAX_NUM_IDENTIFIERS + 1;

			next[first] = last;
			prev[last] = first;
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
			for (int i = next[first]; i != last; i = next[i]) {
				++cnt;
			}
			int[] ret = new int[cnt];
			cnt = 0;
			for (int i = next[first]; i != last; i = next[i]) {
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

		void clear() {
			currentAddr = 0;
			numActiveObject = 0;
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
			return addr;
		}
	}

	private void recyclePage(int pageId) {
		freePages[numFreePages++] = pageId;
	}

	private int getFreePage() {
		if (numFreePages == 0) {
			throw new ExecuteException("Insufficent Memory");
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
	}

	SmallItemsPage currentPage;

	public int alloc(int size) {
		if (size < 0 || size % 4 != 0) {
			throw new ExecuteException("bad alloc size = " + size);
		}
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
		} else {// small item
			log.println("\tIt is a small block");
			if (currentPage == null) {
				currentPage = pages[getFreePage()];
				log.println("\t\tUsing a new page " + currentPage.page);
			}
			int addr = currentPage.alloc(size);
			if (addr == -1) {
				currentPage = pages[getFreePage()];
				addr = currentPage.alloc(size);
				log.println("\t\tUsing a new page " + currentPage.page);
			}
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
		if (startAddr[id] != -1) {
			log.println("\tIt is a small block");
			// smallItem
			SmallItemsPage block = myPage[id];
			block.numActiveObject--;
			assert (block.numActiveObject >= 0);
			if (block.numActiveObject == 0) {
				block.clear();
				recyclePage(block.page);
				if (currentPage == block) {
					currentPage = null;
				}
				log.println("\tPage " + block.page
						+ " becomes empty and is recycled.");
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
