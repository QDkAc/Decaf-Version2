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
	private PrintWriter log;

	public TacVM(String[] args) {
		try {
			input = new BufferedInputStream(new FileInputStream(args[0]));
		} catch (FileNotFoundException e) {
			System.err.println("File " + args[0] + " not found");
			System.exit(1);
		}

		if (args.length > 1) {
			try {
				log = new PrintWriter(args[1]);
			} catch (FileNotFoundException e) {
				System.err.println("File " + args[1] + " not found");
				System.exit(1);
			}
		} else {
			log = new PrintWriter(System.out);
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
		executor.init(parser.getStringTable(), parser.getTacs(),
				parser.getVTables(), parser.getEnterPoint());
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
