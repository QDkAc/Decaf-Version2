package decaf.tacvm.exec;

import java.io.BufferedReader;
import java.util.Queue;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.Timer;
import java.util.TimerTask;

import decaf.tacvm.parser.Tac;

public final class Executor {

	private static final String[] intrinsics = new String[] { "_Alloc", "_GC",
			"_Halt", "_PrintBool", "_PrintInt", "_PrintString", "_ReadInteger",
			"_ReadLine", "_StringEqual", };

	public static int getIntrinsicIndex(String name) {
		return Arrays.binarySearch(intrinsics, name);
	}

	public class Intrinsic {

		public int callIntrinsic(int index) {
			int ret;
			switch (index) {
			case 0:
				ret = _Alloc();
				garbageCollector.setRvReferenceMemory(new HeapAddress(ret, 0));
				return ret;
			case 1:
				garbageCollector.cyclicReferenceDetection();
				break;
			case 2:
				_Halt();
				break;
			case 3:
				_PrintBool();
				break;
			case 4:
				_PrintInt();
				break;
			case 5:
				_PrintString();
				break;
			case 6:
				return _ReadInteger();
			case 7:
				ret = _ReadLine();
				garbageCollector.setRvReferenceStringTable(ret);
				return ret;
			case 8:
				return _StringEqual();

			default:
				throw new ExecuteException("unknown intrinsic call");
			}
			return 0;
		}

		private int _Alloc() {
			return memory.alloc(stack[sp + 1]);
		}

		private void _Halt() {
			// printStackTrace();
			memoryLog.close();
			garbageCollectorLog.close();
			System.exit(0);
		}

		private void _PrintBool() {
			System.out.print(stack[sp + 1] == 0 ? "false" : "true");
		}

		private void _PrintInt() {
			System.out.print(stack[sp + 1]);
		}

		private void _PrintString() {
			System.out.print(stringTable.get(stack[sp + 1]));
		}

		private int _ReadInteger() {
			Scanner scanner = new Scanner(System.in);
			return scanner.nextInt();
		}

		private int _ReadLine() {
			BufferedReader br = new BufferedReader(new InputStreamReader(
					System.in));
			try {
				String s = br.readLine();
				stringTable.add(s);
				return stringTable.size() - 1;
			} catch (IOException e) {
				throw new ExecuteException(e);
			}
		}

		private int _StringEqual() {
			String str1 = stringTable.get(stack[sp + 1]);
			String str2 = stringTable.get(stack[sp + 2]);
			return str1.equals(str2) ? 1 : 0;
		}
	}

	static class HeapAddress {
		int base, offset;

		HeapAddress(int base, int offset) {
			this.base = base;
			this.offset = offset;
		}

		@Override
		public boolean equals(Object another) {
			if (another instanceof HeapAddress)
				return base == ((HeapAddress) another).base
						&& offset == ((HeapAddress) another).offset;
			else
				return false;
		}

		@Override
		public int hashCode() {
			return base ^ offset;
		}
	}

	public class GarbageCollector {

		private Map<HeapAddress, Integer> memoryReferenceCount;
		private Map<HeapAddress, HeapAddress> heapReferenceMemory;
		private Map<Integer, HeapAddress> stackReferenceMemory;
		private Map<Integer, Integer> stringTableReferenceCount;
		private Map<HeapAddress, Integer> heapReferenceStringTable;
		private Map<Integer, Integer> stackReferenceStringTable;
		private HeapAddress rvReferenceMemory;
		private Integer rvReferenceStringTable;
		private PrintWriter log;

		public GarbageCollector(long period, PrintWriter log) {
			this.log = log;
			if (period == -1) {
				period = 1000;
			}
			memoryReferenceCount = new HashMap<HeapAddress, Integer>();
			heapReferenceMemory = new HashMap<HeapAddress, HeapAddress>();
			stackReferenceMemory = new HashMap<Integer, HeapAddress>();
			stringTableReferenceCount = new HashMap<Integer, Integer>();
			heapReferenceStringTable = new HashMap<HeapAddress, Integer>();
			stackReferenceStringTable = new HashMap<Integer, Integer>();
			rvReferenceMemory = null;
			rvReferenceStringTable = null;
			Timer timer = new Timer();
			timer.schedule(new TimerTask() {

				@Override
				public void run() {
					synchronized (Executor.this) {
						cyclicReferenceDetection();
					}
				}

			}, 0, period);
		}

		void setRvReferenceMemory(HeapAddress address) {
			clearRv();
			// System.out.println("rv is now referencing memory " + address);
			rvReferenceMemory = address;
			if (memoryReferenceCount.containsKey(address))
				memoryReferenceCount.put(address,
						memoryReferenceCount.get(address) + 1);
			else
				memoryReferenceCount.put(address, 1);
		}

		void setRvReferenceStringTable(Integer address) {
			clearRv();
			rvReferenceStringTable = address;
			if (stringTableReferenceCount.containsKey(address))
				stringTableReferenceCount.put(address,
						stringTableReferenceCount.get(address) + 1);
			else
				stringTableReferenceCount.put(address, 1);
		}

		void setStackReferenceMemory(Integer address, HeapAddress content) {
			// System.out.println("stack " + address + " is now referencing
			// memory " + content);
			stackReferenceMemory.put(address, content);
			if (memoryReferenceCount.containsKey(content))
				memoryReferenceCount.put(content,
						memoryReferenceCount.get(content) + 1);
			else
				memoryReferenceCount.put(content, 1);
		}

		void setStackReferenceStringTable(Integer address, Integer content) {
			stackReferenceStringTable.put(address, content);
			if (stringTableReferenceCount.containsKey(content))
				stringTableReferenceCount.put(content,
						stringTableReferenceCount.get(content) + 1);
			else
				stringTableReferenceCount.put(content, 1);
		}

		void setHeapReferenceMemory(HeapAddress address, HeapAddress content) {
			// System.out.println("heap " + address + " is now referencing
			// memory " + content);
			heapReferenceMemory.put(address, content);
			if (memoryReferenceCount.containsKey(content))
				memoryReferenceCount.put(content,
						memoryReferenceCount.get(content) + 1);
			else
				memoryReferenceCount.put(content, 1);
		}

		void setHeapReferenceStringTable(HeapAddress address, Integer content) {
			heapReferenceStringTable.put(address, content);
			if (stringTableReferenceCount.containsKey(content))
				stringTableReferenceCount.put(content,
						stringTableReferenceCount.get(content) + 1);
			else
				stringTableReferenceCount.put(content, 1);
		}

		void clearBlock(int base) {
			int size = memory.getBlockSize(base);
			for (int i = 0; i < size; i++)
				clearHeap(new HeapAddress(base, i * 4));
		}

		void clearRv() {
			if (rvReferenceMemory != null) {
				memoryReferenceCount.put(rvReferenceMemory,
						memoryReferenceCount.get(rvReferenceMemory) - 1);
				if (memoryReferenceCount.get(rvReferenceMemory) == 0) {
					log.println("Memory at address " + rvReferenceMemory
							+ " will be disposed due to zero ref count");
					log.println("\tCurrent inst: " + insts[pc - 1]);
					clearBlock(rvReferenceMemory.base);
					memory.dispose(rvReferenceMemory.base);
				}
				rvReferenceMemory = null;
			}
			if (rvReferenceStringTable != null) {
				stringTableReferenceCount.put(rvReferenceStringTable,
						memoryReferenceCount.get(rvReferenceStringTable) - 1);
				if (stringTableReferenceCount.get(rvReferenceStringTable) == 0) {
					log.println("String Table at address "
							+ rvReferenceStringTable
							+ " will be disposed due to zero ref count");
					log.println("\tContent inside this block: "
							+ stringTable.get(rvReferenceStringTable));
					log.println("\tCurrent inst: " + insts[pc - 1]);
				}
				rvReferenceStringTable = null;
			}

		}

		void clearStack(int address) {
			if (stackReferenceMemory.containsKey(address)) {
				HeapAddress to = stackReferenceMemory.get(address);
				memoryReferenceCount.put(to, memoryReferenceCount.get(to) - 1);
				if (memoryReferenceCount.get(to) == 0) {
					log.println("Memory at address " + to.base
							+ " will be disposed due to zero ref count");
					log.println("\tCurrent inst: " + insts[pc - 1]);
					clearBlock(to.base);
					memory.dispose(to.base);
				}
				stackReferenceMemory.remove(address);
				return;
			}
			if (stackReferenceStringTable.containsKey(address)) {
				Integer to = stackReferenceStringTable.get(address);
				stringTableReferenceCount.put(to,
						stringTableReferenceCount.get(to) - 1);
				if (stringTableReferenceCount.get(to) == 0) {
					log.println("String Table at address " + to
							+ " will be disposed due to zero ref count");
					log.println("\tContent inside this block: "
							+ stringTable.get(to));
					log.println("\tCurrent inst: " + insts[pc - 1]);
				}
				stackReferenceStringTable.remove(address);
				return;
			}
		}

		void clearHeap(HeapAddress address) {
			if (heapReferenceMemory.containsKey(address)) {
				HeapAddress to = heapReferenceMemory.get(address);
				memoryReferenceCount.put(to, memoryReferenceCount.get(to) - 1);
				if (memoryReferenceCount.get(to) == 0) {
					log.println("Memory at address " + to.base
							+ " will be disposed due to zero ref count");
					log.println("\tCurrent inst: " + insts[pc - 1]);
					clearBlock(to.base);
					memory.dispose(to.base);
				}
				heapReferenceMemory.remove(address);
				return;
			}
			if (heapReferenceStringTable.containsKey(address)) {
				Integer to = heapReferenceStringTable.get(address);
				stringTableReferenceCount.put(to,
						stringTableReferenceCount.get(to) - 1);
				if (stringTableReferenceCount.get(to) == 0) {
					log.println("String Table at address " + to
							+ " will be disposed due to zero ref count");
					log.println("\tContent inside this block: "
							+ stringTable.get(to));
					log.println("\tCurrent inst: " + insts[pc - 1]);
				}
				heapReferenceStringTable.remove(address);
				return;
			}
		}

		public void assignRvToStack(int address) {
			clearRv();
			if (stackReferenceMemory.containsKey(address)) {
				setRvReferenceMemory(stackReferenceMemory.get(address));
				return;
			}
			if (stackReferenceStringTable.containsKey(address)) {
				setRvReferenceStringTable(stackReferenceStringTable
						.get(address));
				return;
			}

		}

		public void assignStackToRv(int address) {
			clearStack(address);
			if (rvReferenceMemory != null) {
				setStackReferenceMemory(address, rvReferenceMemory);
			}
			if (rvReferenceStringTable != null) {
				setStackReferenceStringTable(address, rvReferenceStringTable);
			}
		}

		public void assignStackToStack(int from, int to) {
			clearStack(to);
			if (stackReferenceMemory.containsKey(from)) {
				setStackReferenceMemory(to, stackReferenceMemory.get(from));
				return;
			}
			if (stackReferenceStringTable.containsKey(from)) {
				setStackReferenceStringTable(to,
						stackReferenceStringTable.get(from));
				return;
			}
		}

		public void assignStackToHeap(int from, HeapAddress to) {
			clearHeap(to);
			if (stackReferenceMemory.containsKey(from)) {
				setHeapReferenceMemory(to, stackReferenceMemory.get(from));
				return;
			}
			if (stackReferenceStringTable.containsKey(from)) {
				setHeapReferenceStringTable(to,
						stackReferenceStringTable.get(from));
				return;
			}
		}

		public void assignHeapToStack(HeapAddress from, int to) {
			clearStack(to);
			if (heapReferenceMemory.containsKey(from)) {
				setStackReferenceMemory(to, heapReferenceMemory.get(from));
				return;
			}
			if (heapReferenceStringTable.containsKey(from)) {
				setStackReferenceStringTable(to,
						heapReferenceStringTable.get(from));
				return;
			}
		}

		public void cyclicReferenceDetection() {
			Queue<HeapAddress> queue = new LinkedList<HeapAddress>();
			Set<HeapAddress> visitedNodes = new HashSet<HeapAddress>();
			for (int i = sp + 1; i < stack.length; i++)
				if (stackReferenceMemory.containsKey(i)
						&& visitedNodes.contains(i) == false) {
					queue.add(stackReferenceMemory.get(i));
					visitedNodes.add(stackReferenceMemory.get(i));
				}
			if (rvReferenceMemory != null
					&& visitedNodes.contains(rvReferenceMemory) == false) {
				queue.add(rvReferenceMemory);
				visitedNodes.add(rvReferenceMemory);
			}
			while (queue.isEmpty() == false) {
				HeapAddress current = queue.poll();
				int size = memory.getBlockSize(current.base);
				for (int i = 0; i < size; i++)
					if (heapReferenceMemory.containsKey(new HeapAddress(
							current.base, i * 4))) {
						HeapAddress to = heapReferenceMemory
								.get(new HeapAddress(current.base, i * 4));
						if (visitedNodes.contains(to) == false) {
							visitedNodes.add(to);
							queue.add(to);
						}
					}
			}
			int[] blocks = memory.getAllObject();
			for (int block : blocks)
				if (visitedNodes.contains(new HeapAddress(block, 0)) == false) {
					log.println("Memory at address "
							+ block
							+ " will be disposed due to cyclic reference detection");
					memory.dispose(block);
				}
		}
	}

	private Inst[] insts;

	private int enterPoint;

	private Memory memory;

	private Intrinsic intrinsic;

	private List<String> stringTable;

	GarbageCollector garbageCollector;

	private static final int DEFAULT_STACK_SIZE = 1024 * 1024;

	private int fp = DEFAULT_STACK_SIZE - 1;

	private int sp = DEFAULT_STACK_SIZE - 1;

	private int ra = -1;

	private int pc;

	private int rv = -1;

	private int[] stack = new int[DEFAULT_STACK_SIZE];

	private void checkStackAccess(int index) {
		if (index >= stack.length) {
			throw new ExecuteException("stack access index = " + index
					+ " out of bounds");
		}
		if (index < 0) {
			int[] newStack = new int[stack.length * 2];
			System.arraycopy(stack, 0, newStack, stack.length, stack.length);
			fp += stack.length;
			sp += stack.length;
			stack = newStack;
		}
	}

	private PrintWriter memoryLog, garbageCollectorLog;

	public void init(List<String> stringTable, List<Tac> tacs, int[] vtable,
			int enterPoint, PrintWriter memoryLog,
			PrintWriter garbageCollectorLog, int period) {
		memory = new Memory(memoryLog);
		memory.setVTable(vtable);
		this.stringTable = stringTable;
		this.memoryLog = memoryLog;
		this.garbageCollectorLog = garbageCollectorLog;

		insts = new Inst[tacs.size()];
		Iterator<Tac> iter = tacs.iterator();
		for (int i = 0; iter.hasNext(); i++) {
			Tac tac = iter.next();
			insts[i] = new Inst();
			insts[i].opc = tac.opc;
			if (tac.opr0 != null) {
				insts[i].opr0 = tac.opr0.iVal;
			}
			if (tac.opr1 != null) {
				insts[i].opr1 = tac.opr1.iVal;
			}
			if (tac.opr2 != null) {
				insts[i].opr2 = tac.opr2.iVal;
			}
			insts[i].tac = tac.text;
			insts[i].loc = tac.loc;
		}
		this.enterPoint = enterPoint;
		this.intrinsic = new Intrinsic();
		garbageCollector = new GarbageCollector(period, garbageCollectorLog);
	}

	public void exec() {
		pc = enterPoint;
		rv = -1;

		while (pc != -1) {
			synchronized (this) {
				Inst inst = insts[pc++];
				// if (inst.loc.getLine() == 113) {
				// System.out.println("haha");
				// }
				int resultIndex;
				try {
					switch (inst.opc) {
					case ENTER_FUNC:
						checkStackAccess(sp - 1);
						stack[sp] = fp;
						stack[sp - 1] = ra;
						fp = sp;
						sp -= inst.opr0;
						break;
					case LEAVE_FUNC:
						for (int i = sp + 1; i < fp - 1; i++)
							garbageCollector.clearStack(i);
						sp = fp;
						ra = stack[fp - 1];
						fp = stack[fp];
						pc = ra;
						break;
					case INDIRECT_CALL:
						ra = pc;
						pc = stack[fp + inst.opr0 / 4];
						break;
					case DIRECT_CALL:
						ra = pc;
						pc = inst.opr0;
						break;
					case LIB_CALL:
						rv = intrinsic.callIntrinsic(inst.opr0);
						break;
					case MOVE_FROM_RV:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = rv;
						garbageCollector.assignStackToRv(resultIndex);
						break;
					case RETURN:
						rv = stack[fp + inst.opr0 / 4];
						garbageCollector.assignRvToStack(fp + inst.opr0 / 4);
						break;
					case ASSIGN:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4];
						garbageCollector.assignStackToStack(fp + inst.opr1 / 4,
								resultIndex);
						break;
					case ADD:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								+ stack[fp + inst.opr2 / 4];
						break;
					case SUB:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								- stack[fp + inst.opr2 / 4];
						break;
					case MUL:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								* stack[fp + inst.opr2 / 4];
						break;
					case DIV:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								/ stack[fp + inst.opr2 / 4];
						break;
					case MOD:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								% stack[fp + inst.opr2 / 4];
						break;
					case NEG:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = -stack[fp + inst.opr1 / 4];
						break;
					case GTR:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4] > stack[fp
								+ inst.opr2 / 4] ? 1 : 0;
						break;
					case GEQ:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4] >= stack[fp
								+ inst.opr2 / 4] ? 1 : 0;
						break;
					case EQU:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4] == stack[fp
								+ inst.opr2 / 4] ? 1 : 0;
						break;
					case NEQ:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4] != stack[fp
								+ inst.opr2 / 4] ? 1 : 0;
						break;
					case LEQ:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4] <= stack[fp
								+ inst.opr2 / 4] ? 1 : 0;
						break;
					case LES:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4] < stack[fp
								+ inst.opr2 / 4] ? 1 : 0;
						break;
					case LAND:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								& stack[fp + inst.opr2 / 4];
						break;
					case LOR:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = stack[fp + inst.opr1 / 4]
								| stack[fp + inst.opr2 / 4];
						break;
					case LNOT:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = 1 - stack[fp + inst.opr1 / 4];
						break;
					case PARM:
						checkStackAccess(sp);
						stack[sp + inst.opr1 / 4] = stack[fp + inst.opr0 / 4];
						garbageCollector.assignStackToStack(fp + inst.opr0 / 4,
								sp + inst.opr1 / 4);
						break;
					case LOAD_VTBL:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = inst.opr1;
						break;
					case LOAD_IMM4:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = inst.opr1;
						break;
					case LOAD_STR:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = inst.opr1;
						garbageCollector.clearStack(resultIndex);
						garbageCollector.setStackReferenceStringTable(
								resultIndex, inst.opr1);
						break;
					case BRANCH:
						pc = inst.opr0;
						break;
					case BEQZ:
						if (stack[fp + inst.opr0 / 4] == 0) {
							pc = inst.opr1;
						}
						break;
					case BNEZ:
						if (stack[fp + inst.opr0 / 4] != 0) {
							pc = inst.opr1;
						}
						break;
					case LOAD:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = memory.load(stack[fp + inst.opr1
								/ 4], inst.opr2);
						garbageCollector.assignHeapToStack(new HeapAddress(
								stack[fp + inst.opr1 / 4], inst.opr2),
								resultIndex);
						break;
					case LOADMOD:
						resultIndex = fp + inst.opr0 / 4;
						checkStackAccess(resultIndex);
						stack[resultIndex] = memory.load(stack[fp + inst.opr1
								/ 4], stack[fp + inst.opr2 / 4]);
						garbageCollector.assignHeapToStack(new HeapAddress(
								stack[fp + inst.opr1 / 4], stack[fp + inst.opr2
										/ 4]), resultIndex);
						break;
					case STORE:
						memory.store(stack[fp + inst.opr0 / 4], stack[fp
								+ inst.opr1 / 4], inst.opr2);
						garbageCollector.assignStackToHeap(fp + inst.opr0 / 4,
								new HeapAddress(stack[fp + inst.opr1 / 4],
										inst.opr2));
						break;
					case STOREMOD:
						memory.store(stack[fp + inst.opr0 / 4], stack[fp
								+ inst.opr1 / 4], stack[fp + inst.opr2 / 4]);
						garbageCollector.assignStackToHeap(fp + inst.opr0 / 4,
								new HeapAddress(stack[fp + inst.opr1 / 4],
										stack[fp + inst.opr2 / 4]));
						break;
					default:
						if (inst.loc != null) {
							System.err.println("***Error at " + inst.loc
									+ ", tac = " + inst.tac + ": unknown tac");
						} else {
							System.err.println("***Error, tac = " + inst.tac
									+ ": unknown tac");
						}
						// printStackTrace();
						memoryLog.close();
						garbageCollectorLog.close();
						System.exit(0);
					}
				} catch (ExecuteException e) {
					e.printStackTrace();
					if (inst.loc != null) {
						System.err
								.println("***Error at " + inst.loc + ", tac = "
										+ inst.tac + ": " + e.getMessage());
					} else {
						System.err.println("***Error, tac = " + inst.tac + ": "
								+ e.getMessage());
					}
					// printStackTrace();
					memoryLog.close();
					garbageCollectorLog.close();
					System.exit(0);
				} catch (Exception e) {
					if (inst.loc != null) {
						System.err.println("vm crash at " + inst.loc
								+ ", tac = " + inst.tac);
						System.err.println("Caused by:");
						e.printStackTrace(System.err);
					} else {
						System.err.println("vm crash, tac = " + inst.tac);
						System.err.println("Caused by:");
						e.printStackTrace(System.err);
					}
					// printStackTrace();
					memoryLog.close();
					garbageCollectorLog.close();
					System.exit(0);
				}
			}
		}
	}

	/*
	 * private void printStackTrace() { int fp = this.fp; System.err.println(
	 * "stack trace:"); Inst inst = insts[pc]; if (inst.loc != null) {
	 * System.err.println("\t" + inst.loc + ", tac = " + inst.tac); } else {
	 * System.err.println("\ttac = " + inst.tac); } while (fp != stack.length -
	 * 1) { inst = insts[stack[fp - 1] - 1]; if (inst.loc != null) {
	 * System.err.println("\t" + inst.loc + ", tac = " + inst.tac); } else {
	 * System.err.println("\ttac = " + inst.tac); } fp = stack[fp]; } }
	 */

	public void dumpInsts() {
		for (Inst inst : insts) {
			System.out.println(inst);
		}
	}
}
