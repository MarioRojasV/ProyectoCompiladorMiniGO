// Generated from /home/mario-rojas/Documents/Universidad/Trabajos_TEC/2026/Semestre_5/Compiladores/ProyectoEvaluado/ProyectoMario_Jeff/MiniGO.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiniGOLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PACKAGE=1, VAR=2, TYPE=3, FUNC=4, STRUCT=5, IF=6, ELSE=7, FOR=8, SWITCH=9, 
		CASE=10, DEFAULT=11, RETURN=12, BREAK=13, CONTINUE=14, PRINT=15, PRINTLN=16, 
		APPEND=17, LEN=18, CAP=19, PLUS=20, MINUS=21, MULT=22, DIV=23, MOD=24, 
		LSHIFT=25, RSHIFT=26, AMP=27, AMPXOR=28, PIPE=29, XOR=30, EQ=31, NEQ=32, 
		LT=33, GT=34, LEQ=35, GEQ=36, AND=37, OR=38, NOT=39, ASSIGN=40, DECLARE_ASSIGN=41, 
		PLUS_ASSIGN=42, MINUS_ASSIGN=43, MULT_ASSIGN=44, DIV_ASSIGN=45, MOD_ASSIGN=46, 
		AMP_ASSIGN=47, PIPE_ASSIGN=48, XOR_ASSIGN=49, LSHIFT_ASSIGN=50, RSHIFT_ASSIGN=51, 
		AMPXOR_ASSIGN=52, INC=53, DEC=54, LPAREN=55, RPAREN=56, LBRACE=57, RBRACE=58, 
		LBRACKET=59, RBRACKET=60, SEMICOLON=61, COLON=62, COMMA=63, DOT=64, INTLITERAL=65, 
		FLOATLITERAL=66, RUNELITERAL=67, RAWSTRINGLITERAL=68, INTERPRETEDSTRINGLITERAL=69, 
		IDENTIFIER=70, WS=71, LINE_COMMENT=72, BLOCK_COMMENT=73;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PACKAGE", "VAR", "TYPE", "FUNC", "STRUCT", "IF", "ELSE", "FOR", "SWITCH", 
			"CASE", "DEFAULT", "RETURN", "BREAK", "CONTINUE", "PRINT", "PRINTLN", 
			"APPEND", "LEN", "CAP", "PLUS", "MINUS", "MULT", "DIV", "MOD", "LSHIFT", 
			"RSHIFT", "AMP", "AMPXOR", "PIPE", "XOR", "EQ", "NEQ", "LT", "GT", "LEQ", 
			"GEQ", "AND", "OR", "NOT", "ASSIGN", "DECLARE_ASSIGN", "PLUS_ASSIGN", 
			"MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AMP_ASSIGN", 
			"PIPE_ASSIGN", "XOR_ASSIGN", "LSHIFT_ASSIGN", "RSHIFT_ASSIGN", "AMPXOR_ASSIGN", 
			"INC", "DEC", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
			"SEMICOLON", "COLON", "COMMA", "DOT", "INTLITERAL", "FLOATLITERAL", "RUNELITERAL", 
			"RAWSTRINGLITERAL", "INTERPRETEDSTRINGLITERAL", "IDENTIFIER", "WS", "LINE_COMMENT", 
			"BLOCK_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'package'", "'var'", "'type'", "'func'", "'struct'", "'if'", "'else'", 
			"'for'", "'switch'", "'case'", "'default'", "'return'", "'break'", "'continue'", 
			"'print'", "'println'", "'append'", "'len'", "'cap'", "'+'", "'-'", "'*'", 
			"'/'", "'%'", "'<<'", "'>>'", "'&'", "'&^'", "'|'", "'^'", "'=='", "'!='", 
			"'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", 
			"'-='", "'*='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", 
			"'&^='", "'++'", "'--'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
			"':'", "','", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PACKAGE", "VAR", "TYPE", "FUNC", "STRUCT", "IF", "ELSE", "FOR", 
			"SWITCH", "CASE", "DEFAULT", "RETURN", "BREAK", "CONTINUE", "PRINT", 
			"PRINTLN", "APPEND", "LEN", "CAP", "PLUS", "MINUS", "MULT", "DIV", "MOD", 
			"LSHIFT", "RSHIFT", "AMP", "AMPXOR", "PIPE", "XOR", "EQ", "NEQ", "LT", 
			"GT", "LEQ", "GEQ", "AND", "OR", "NOT", "ASSIGN", "DECLARE_ASSIGN", "PLUS_ASSIGN", 
			"MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AMP_ASSIGN", 
			"PIPE_ASSIGN", "XOR_ASSIGN", "LSHIFT_ASSIGN", "RSHIFT_ASSIGN", "AMPXOR_ASSIGN", 
			"INC", "DEC", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
			"SEMICOLON", "COLON", "COMMA", "DOT", "INTLITERAL", "FLOATLITERAL", "RUNELITERAL", 
			"RAWSTRINGLITERAL", "INTERPRETEDSTRINGLITERAL", "IDENTIFIER", "WS", "LINE_COMMENT", 
			"BLOCK_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MiniGOLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiniGO.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K\u01d5\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4"+
		"\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3"+
		"\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3"+
		"\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3"+
		"\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3"+
		"\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3"+
		"\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'"+
		"\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3"+
		"/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64"+
		"\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\3"+
		"8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\6B\u017b\n"+
		"B\rB\16B\u017c\3C\6C\u0180\nC\rC\16C\u0181\3C\3C\7C\u0186\nC\fC\16C\u0189"+
		"\13C\3C\3C\6C\u018d\nC\rC\16C\u018e\5C\u0191\nC\3D\3D\3D\3D\5D\u0197\n"+
		"D\3D\3D\3E\3E\7E\u019d\nE\fE\16E\u01a0\13E\3E\3E\3F\3F\3F\3F\7F\u01a8"+
		"\nF\fF\16F\u01ab\13F\3F\3F\3G\3G\7G\u01b1\nG\fG\16G\u01b4\13G\3H\6H\u01b7"+
		"\nH\rH\16H\u01b8\3H\3H\3I\3I\3I\3I\7I\u01c1\nI\fI\16I\u01c4\13I\3I\3I"+
		"\3J\3J\3J\3J\7J\u01cc\nJ\fJ\16J\u01cf\13J\3J\3J\3J\3J\3J\3\u01cd\2K\3"+
		"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37"+
		"\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37="+
		" ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9"+
		"q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008f"+
		"I\u0091J\u0093K\3\2\n\3\2\62;\6\2\f\f\17\17))^^\3\2bb\6\2\f\f\17\17$$"+
		"^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2\u01e1"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2"+
		"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3"+
		"\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2"+
		"\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2"+
		"{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085"+
		"\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2"+
		"\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u009d"+
		"\3\2\2\2\7\u00a1\3\2\2\2\t\u00a6\3\2\2\2\13\u00ab\3\2\2\2\r\u00b2\3\2"+
		"\2\2\17\u00b5\3\2\2\2\21\u00ba\3\2\2\2\23\u00be\3\2\2\2\25\u00c5\3\2\2"+
		"\2\27\u00ca\3\2\2\2\31\u00d2\3\2\2\2\33\u00d9\3\2\2\2\35\u00df\3\2\2\2"+
		"\37\u00e8\3\2\2\2!\u00ee\3\2\2\2#\u00f6\3\2\2\2%\u00fd\3\2\2\2\'\u0101"+
		"\3\2\2\2)\u0105\3\2\2\2+\u0107\3\2\2\2-\u0109\3\2\2\2/\u010b\3\2\2\2\61"+
		"\u010d\3\2\2\2\63\u010f\3\2\2\2\65\u0112\3\2\2\2\67\u0115\3\2\2\29\u0117"+
		"\3\2\2\2;\u011a\3\2\2\2=\u011c\3\2\2\2?\u011e\3\2\2\2A\u0121\3\2\2\2C"+
		"\u0124\3\2\2\2E\u0126\3\2\2\2G\u0128\3\2\2\2I\u012b\3\2\2\2K\u012e\3\2"+
		"\2\2M\u0131\3\2\2\2O\u0134\3\2\2\2Q\u0136\3\2\2\2S\u0138\3\2\2\2U\u013b"+
		"\3\2\2\2W\u013e\3\2\2\2Y\u0141\3\2\2\2[\u0144\3\2\2\2]\u0147\3\2\2\2_"+
		"\u014a\3\2\2\2a\u014d\3\2\2\2c\u0150\3\2\2\2e\u0153\3\2\2\2g\u0157\3\2"+
		"\2\2i\u015b\3\2\2\2k\u015f\3\2\2\2m\u0162\3\2\2\2o\u0165\3\2\2\2q\u0167"+
		"\3\2\2\2s\u0169\3\2\2\2u\u016b\3\2\2\2w\u016d\3\2\2\2y\u016f\3\2\2\2{"+
		"\u0171\3\2\2\2}\u0173\3\2\2\2\177\u0175\3\2\2\2\u0081\u0177\3\2\2\2\u0083"+
		"\u017a\3\2\2\2\u0085\u0190\3\2\2\2\u0087\u0192\3\2\2\2\u0089\u019a\3\2"+
		"\2\2\u008b\u01a3\3\2\2\2\u008d\u01ae\3\2\2\2\u008f\u01b6\3\2\2\2\u0091"+
		"\u01bc\3\2\2\2\u0093\u01c7\3\2\2\2\u0095\u0096\7r\2\2\u0096\u0097\7c\2"+
		"\2\u0097\u0098\7e\2\2\u0098\u0099\7m\2\2\u0099\u009a\7c\2\2\u009a\u009b"+
		"\7i\2\2\u009b\u009c\7g\2\2\u009c\4\3\2\2\2\u009d\u009e\7x\2\2\u009e\u009f"+
		"\7c\2\2\u009f\u00a0\7t\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3"+
		"\7{\2\2\u00a3\u00a4\7r\2\2\u00a4\u00a5\7g\2\2\u00a5\b\3\2\2\2\u00a6\u00a7"+
		"\7h\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7e\2\2\u00aa"+
		"\n\3\2\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7t\2\2\u00ae"+
		"\u00af\7w\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1\7v\2\2\u00b1\f\3\2\2\2\u00b2"+
		"\u00b3\7k\2\2\u00b3\u00b4\7h\2\2\u00b4\16\3\2\2\2\u00b5\u00b6\7g\2\2\u00b6"+
		"\u00b7\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\20\3\2\2\2\u00ba"+
		"\u00bb\7h\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7t\2\2\u00bd\22\3\2\2\2\u00be"+
		"\u00bf\7u\2\2\u00bf\u00c0\7y\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7v\2\2"+
		"\u00c2\u00c3\7e\2\2\u00c3\u00c4\7j\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\7"+
		"e\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7g\2\2\u00c9\26"+
		"\3\2\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7h\2\2\u00cd"+
		"\u00ce\7c\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7v\2\2"+
		"\u00d1\30\3\2\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7"+
		"v\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7p\2\2\u00d8\32"+
		"\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc"+
		"\u00dd\7c\2\2\u00dd\u00de\7m\2\2\u00de\34\3\2\2\2\u00df\u00e0\7e\2\2\u00e0"+
		"\u00e1\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7k\2\2"+
		"\u00e4\u00e5\7p\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7g\2\2\u00e7\36\3\2"+
		"\2\2\u00e8\u00e9\7r\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec"+
		"\7p\2\2\u00ec\u00ed\7v\2\2\u00ed \3\2\2\2\u00ee\u00ef\7r\2\2\u00ef\u00f0"+
		"\7t\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7v\2\2\u00f3"+
		"\u00f4\7n\2\2\u00f4\u00f5\7p\2\2\u00f5\"\3\2\2\2\u00f6\u00f7\7c\2\2\u00f7"+
		"\u00f8\7r\2\2\u00f8\u00f9\7r\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7p\2\2"+
		"\u00fb\u00fc\7f\2\2\u00fc$\3\2\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7g\2"+
		"\2\u00ff\u0100\7p\2\2\u0100&\3\2\2\2\u0101\u0102\7e\2\2\u0102\u0103\7"+
		"c\2\2\u0103\u0104\7r\2\2\u0104(\3\2\2\2\u0105\u0106\7-\2\2\u0106*\3\2"+
		"\2\2\u0107\u0108\7/\2\2\u0108,\3\2\2\2\u0109\u010a\7,\2\2\u010a.\3\2\2"+
		"\2\u010b\u010c\7\61\2\2\u010c\60\3\2\2\2\u010d\u010e\7\'\2\2\u010e\62"+
		"\3\2\2\2\u010f\u0110\7>\2\2\u0110\u0111\7>\2\2\u0111\64\3\2\2\2\u0112"+
		"\u0113\7@\2\2\u0113\u0114\7@\2\2\u0114\66\3\2\2\2\u0115\u0116\7(\2\2\u0116"+
		"8\3\2\2\2\u0117\u0118\7(\2\2\u0118\u0119\7`\2\2\u0119:\3\2\2\2\u011a\u011b"+
		"\7~\2\2\u011b<\3\2\2\2\u011c\u011d\7`\2\2\u011d>\3\2\2\2\u011e\u011f\7"+
		"?\2\2\u011f\u0120\7?\2\2\u0120@\3\2\2\2\u0121\u0122\7#\2\2\u0122\u0123"+
		"\7?\2\2\u0123B\3\2\2\2\u0124\u0125\7>\2\2\u0125D\3\2\2\2\u0126\u0127\7"+
		"@\2\2\u0127F\3\2\2\2\u0128\u0129\7>\2\2\u0129\u012a\7?\2\2\u012aH\3\2"+
		"\2\2\u012b\u012c\7@\2\2\u012c\u012d\7?\2\2\u012dJ\3\2\2\2\u012e\u012f"+
		"\7(\2\2\u012f\u0130\7(\2\2\u0130L\3\2\2\2\u0131\u0132\7~\2\2\u0132\u0133"+
		"\7~\2\2\u0133N\3\2\2\2\u0134\u0135\7#\2\2\u0135P\3\2\2\2\u0136\u0137\7"+
		"?\2\2\u0137R\3\2\2\2\u0138\u0139\7<\2\2\u0139\u013a\7?\2\2\u013aT\3\2"+
		"\2\2\u013b\u013c\7-\2\2\u013c\u013d\7?\2\2\u013dV\3\2\2\2\u013e\u013f"+
		"\7/\2\2\u013f\u0140\7?\2\2\u0140X\3\2\2\2\u0141\u0142\7,\2\2\u0142\u0143"+
		"\7?\2\2\u0143Z\3\2\2\2\u0144\u0145\7\61\2\2\u0145\u0146\7?\2\2\u0146\\"+
		"\3\2\2\2\u0147\u0148\7\'\2\2\u0148\u0149\7?\2\2\u0149^\3\2\2\2\u014a\u014b"+
		"\7(\2\2\u014b\u014c\7?\2\2\u014c`\3\2\2\2\u014d\u014e\7~\2\2\u014e\u014f"+
		"\7?\2\2\u014fb\3\2\2\2\u0150\u0151\7`\2\2\u0151\u0152\7?\2\2\u0152d\3"+
		"\2\2\2\u0153\u0154\7>\2\2\u0154\u0155\7>\2\2\u0155\u0156\7?\2\2\u0156"+
		"f\3\2\2\2\u0157\u0158\7@\2\2\u0158\u0159\7@\2\2\u0159\u015a\7?\2\2\u015a"+
		"h\3\2\2\2\u015b\u015c\7(\2\2\u015c\u015d\7`\2\2\u015d\u015e\7?\2\2\u015e"+
		"j\3\2\2\2\u015f\u0160\7-\2\2\u0160\u0161\7-\2\2\u0161l\3\2\2\2\u0162\u0163"+
		"\7/\2\2\u0163\u0164\7/\2\2\u0164n\3\2\2\2\u0165\u0166\7*\2\2\u0166p\3"+
		"\2\2\2\u0167\u0168\7+\2\2\u0168r\3\2\2\2\u0169\u016a\7}\2\2\u016at\3\2"+
		"\2\2\u016b\u016c\7\177\2\2\u016cv\3\2\2\2\u016d\u016e\7]\2\2\u016ex\3"+
		"\2\2\2\u016f\u0170\7_\2\2\u0170z\3\2\2\2\u0171\u0172\7=\2\2\u0172|\3\2"+
		"\2\2\u0173\u0174\7<\2\2\u0174~\3\2\2\2\u0175\u0176\7.\2\2\u0176\u0080"+
		"\3\2\2\2\u0177\u0178\7\60\2\2\u0178\u0082\3\2\2\2\u0179\u017b\t\2\2\2"+
		"\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d"+
		"\3\2\2\2\u017d\u0084\3\2\2\2\u017e\u0180\t\2\2\2\u017f\u017e\3\2\2\2\u0180"+
		"\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\3\2"+
		"\2\2\u0183\u0187\7\60\2\2\u0184\u0186\t\2\2\2\u0185\u0184\3\2\2\2\u0186"+
		"\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0191\3\2"+
		"\2\2\u0189\u0187\3\2\2\2\u018a\u018c\7\60\2\2\u018b\u018d\t\2\2\2\u018c"+
		"\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2"+
		"\2\2\u018f\u0191\3\2\2\2\u0190\u017f\3\2\2\2\u0190\u018a\3\2\2\2\u0191"+
		"\u0086\3\2\2\2\u0192\u0196\7)\2\2\u0193\u0197\n\3\2\2\u0194\u0195\7^\2"+
		"\2\u0195\u0197\13\2\2\2\u0196\u0193\3\2\2\2\u0196\u0194\3\2\2\2\u0197"+
		"\u0198\3\2\2\2\u0198\u0199\7)\2\2\u0199\u0088\3\2\2\2\u019a\u019e\7b\2"+
		"\2\u019b\u019d\n\4\2\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c"+
		"\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1"+
		"\u01a2\7b\2\2\u01a2\u008a\3\2\2\2\u01a3\u01a9\7$\2\2\u01a4\u01a8\n\5\2"+
		"\2\u01a5\u01a6\7^\2\2\u01a6\u01a8\13\2\2\2\u01a7\u01a4\3\2\2\2\u01a7\u01a5"+
		"\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa"+
		"\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\7$\2\2\u01ad\u008c\3\2"+
		"\2\2\u01ae\u01b2\t\6\2\2\u01af\u01b1\t\7\2\2\u01b0\u01af\3\2\2\2\u01b1"+
		"\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u008e\3\2"+
		"\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b7\t\b\2\2\u01b6\u01b5\3\2\2\2\u01b7"+
		"\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3\2"+
		"\2\2\u01ba\u01bb\bH\2\2\u01bb\u0090\3\2\2\2\u01bc\u01bd\7\61\2\2\u01bd"+
		"\u01be\7\61\2\2\u01be\u01c2\3\2\2\2\u01bf\u01c1\n\t\2\2\u01c0\u01bf\3"+
		"\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3"+
		"\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\bI\2\2\u01c6\u0092\3\2"+
		"\2\2\u01c7\u01c8\7\61\2\2\u01c8\u01c9\7,\2\2\u01c9\u01cd\3\2\2\2\u01ca"+
		"\u01cc\13\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01ce\3"+
		"\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0"+
		"\u01d1\7,\2\2\u01d1\u01d2\7\61\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\bJ"+
		"\2\2\u01d4\u0094\3\2\2\2\20\2\u017c\u0181\u0187\u018e\u0190\u0196\u019e"+
		"\u01a7\u01a9\u01b2\u01b8\u01c2\u01cd\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}