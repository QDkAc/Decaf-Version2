package decaf.tacvm;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;

import decaf.tacvm.exec.Executor;
import decaf.tacvm.parser.Errs;
import decaf.tacvm.parser.Lexer;
import decaf.tacvm.parser.Parser;

public final class TacVM {
	private InputStream input = System.in;

	public TacVM(String[] args) {
		for (int i = 0; i < args.length; i++) {
			try {
				input = new BufferedInputStream(
						new FileInputStream(args[i]));
			} catch (FileNotFoundException e) {
				System.err.println("File " + args[0] + " not found");
				System.exit(1);
			}
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
