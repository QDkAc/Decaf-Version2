package decaf.tacvm.exec;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Memory {
	// the whole logic naming space start from 0
	public static int BLOCK_SIZE = 1024;// a page is 1024 bit

	public static int NUM_BLOCKS = 1 << 15;// number of blocks

	public static int THRESHOLD = BLOCK_SIZE / 2;

	public static int MAX_IDENTIFIERS = 3 << 20;// maximum number of objects

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
	private int[] memory = new int[BLOCK_SIZE * NUM_BLOCKS];
	private int[] freeBlocks = new int[NUM_BLOCKS];
	private int numFreeBlocks;

	private int[] freeIds = new int[MAX_IDENTIFIERS];
	private boolean[] active = new boolean[MAX_IDENTIFIERS];
	private int numFreeIds;

	private int[] startAddr = new int[MAX_IDENTIFIERS];
	private int[] objectSize = new int[MAX_IDENTIFIERS];

	private class ActiveIdList {
		// a double linked list for all active ids
		private int[] next = new int[MAX_IDENTIFIERS + 2];
		private int[] prev = new int[MAX_IDENTIFIERS + 2];

		int first, last;

		public ActiveIdList() {
			first = MAX_IDENTIFIERS;
			last = MAX_IDENTIFIERS + 1;

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

	private PageTable[] pageTable = new PageTable[MAX_IDENTIFIERS];
	private SmallItemsBlock[] myBlock = new SmallItemsBlock[MAX_IDENTIFIERS];

	private SmallItemsBlock[] blocks = new SmallItemsBlock[NUM_BLOCKS];

	Map<Integer, Integer> startAdrToSize = new HashMap<Integer, Integer>();

	// for big object
	private class PageTable {
		int[] pages;

		public PageTable(int numPages) {
			pages = new int[numPages];
			for (int i = 0; i < numPages; i++) {
				pages[i] = getFreeBlock();
			}
		}

		int logicToPhysic(int at) {
			return pages[at >> 10] + (at & 1023);
		}
	}

	//
	private class SmallItemsBlock {
		int page;
		int currentAddr;
		int numActiveObject;

		void clear() {
			currentAddr = 0;
			numActiveObject = 0;
		}

		public SmallItemsBlock(int page) {
			this.page = page;
			clear();
		}

		int alloc(int num) {
			int rest = BLOCK_SIZE - currentAddr;
			if (rest < num)
				return -1;
			int addr = (page << 1024) + currentAddr;
			currentAddr += num;
			numActiveObject++;
			return addr;
		}
	}

	private void recycleBlock(int blockId) {
		freeBlocks[numFreeBlocks++] = blockId;
	}

	private int getFreeBlock() {
		if (numFreeBlocks == 0) {
			throw new ExecuteException("Insufficent Memory");
		}
		int id = freeBlocks[--numFreeBlocks];
		// clear the block before it is used
		Arrays.fill(memory, id << 10, (id << 10) + 1024, 0);
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

	public Memory() {
		numFreeBlocks = 0;
		for (int i = 0; i < NUM_BLOCKS; i++) {
			recycleBlock(i);
			blocks[i] = new SmallItemsBlock(i);

		}
		numFreeIds = 0;
		for (int i = 0; i < MAX_IDENTIFIERS; i++) {
			freeIds[numFreeIds++] = i;
		}
	}

	SmallItemsBlock currentBlock;

	public int alloc(int size) {
		if (size < 0 || size % 4 != 0) {
			throw new ExecuteException("bad alloc size = " + size);
		}
		size /= 4;

		int id = getFreeId();
		objectSize[id] = size;

		if (size > THRESHOLD) {// big item
			int numPages = (size + BLOCK_SIZE - 1) / BLOCK_SIZE;
			PageTable tab = new PageTable(numPages);

			pageTable[id] = tab;
			startAddr[id] = -1;
		} else {// small item
			if (currentBlock == null) {
				currentBlock = blocks[getFreeBlock()];
			}
			int addr = currentBlock.alloc(size);
			if (addr == -1) {
				currentBlock = blocks[getFreeBlock()];
				addr = currentBlock.alloc(size);
			}
			startAddr[id] = addr;
			myBlock[id] = currentBlock;
		}
		System.out.println(id + " allocated");
		return id;
	}

	private int logicToPhysic(int id, int offset) {
		System.out.println("idlogic:" + id);
		if (id < 0 || id >= MAX_IDENTIFIERS || !active[id] || offset % 4 != 0) {
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
		System.out.println("id:" + id);
		if (id < 0 || id >= MAX_IDENTIFIERS || !active[id]) {
			throw new ExecuteException("bad memory access id = " + id);
		}
		return objectSize[id];
	}

	public void store(int val, int id, int offset) {
		memory[logicToPhysic(id, offset)] = val;
	}

	public void dispose(int id) {
		System.out.println(id + " disposed");
		assert (active[id]);
		if (startAddr[id] != -1) {
			// smallItem
			SmallItemsBlock block = myBlock[id];
			block.numActiveObject--;
			assert (block.numActiveObject >= 0);
			if (block.numActiveObject == 0) {
				block.clear();
				recycleBlock(block.page);
				if (currentBlock == block) {
					currentBlock = null;
				}
			}
		} else {
			// bigItem
			PageTable tab = pageTable[id];
			for (int page : tab.pages)
				recycleBlock(page);
		}

		recycleId(id);

		System.out.println("Garbage detected: address @ " + id);
	}
}
