package decaf.tacvm;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.io.PrintWriter;

import decaf.tacvm.exec.Executor;
import decaf.tacvm.parser.Errs;
import decaf.tacvm.parser.Lexer;
import decaf.tacvm.parser.Parser;

public final class TacVM {
	private InputStream input = System.in;
	private PrintWriter memoryLog, garbageCollectorLog;
	private int cyclicReferenceDetectionPeriod = -1;

	public TacVM(String[] args) {
		// try {
		// input = new BufferedInputStream(new FileInputStream(args[0]));
		// } catch (FileNotFoundException e) {
		// System.err.println("File " + args[0] + " not found");
		// System.exit(1);
		// }
		//
		// if (args.length > 1) {
		// try {
		// log = new PrintWriter(args[1]);
		// } catch (FileNotFoundException e) {
		// System.err.println("File " + args[1] + " not found");
		// System.exit(1);
		// }
		// } else {
		// log = new PrintWriter(new OutputStream() {
		// @Override
		// public void write(int b) throws IOException {
		// }
		// });
		// }
		for (int i = 0; i < args.length; i++) {
			if (args[i].equals("-m")) {
				i++;
				if (i < args.length) {
					try {
						memoryLog = new PrintWriter(args[i]);
					} catch (Exception e) {
						System.err.println("Can not open file " + args[i]);
					}
				}
			} else if (args[i].equals("-g")) {
				i++;
				if (i < args.length) {
					try {
						garbageCollectorLog = new PrintWriter(args[i]);
					} catch (Exception e) {
						System.err.println("Can not open file " + args[i]);
					}
				}

			} else if (args[i].equals("-p")) {
				i++;
				if (i < args.length) {
					cyclicReferenceDetectionPeriod = Integer.parseInt(args[i]);
				}
			} else {
				try {
					input = new BufferedInputStream(new FileInputStream(args[0]));
				} catch (FileNotFoundException e) {
					System.err.println("File " + args[0] + " not found");
					System.exit(1);
				}
			}
		}
		if (input == null) {
			System.err.println("Input file not specified");
			System.exit(1);
		}
		if (garbageCollectorLog == null) {
			garbageCollectorLog = new PrintWriter(new OutputStream() {
				@Override
				public void write(int b) throws IOException {
				}
			});
		}
		if (memoryLog == null) {
			memoryLog = new PrintWriter(new OutputStream() {
				@Override
				public void write(int b) throws IOException {
				}

			});
		}
	}

	public void run() {
		Lexer lexer = new Lexer(input);
		Parser parser = new Parser();
		lexer.setParser(parser);
		parser.setLexer(lexer);
		parser.parse();
		Errs.checkPoint(new PrintWriter(System.err));
		Executor executor = new Executor();
		System.out.println(memoryLog);

		executor.init(parser.getStringTable(), parser.getTacs(), parser.getVTables(), parser.getEnterPoint(), memoryLog,
				garbageCollectorLog, cyclicReferenceDetectionPeriod);
		// executor.dumpInsts();
		executor.exec();
		System.exit(0);
	}

	public static void main(String[] args) {
		// args = new String[]{"D:/test.tac"};
		// PrintWriter pw = new PrintWriter("a.out");
		// pw.print("Haha");
		// pw.close();
		TacVM vm = new TacVM(args);
		vm.run();
	}
}
