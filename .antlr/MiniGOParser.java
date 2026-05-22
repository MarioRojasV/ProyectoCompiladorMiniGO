// Generated from /home/mario-rojas/Documents/Universidad/Trabajos_TEC/2026/Semestre_5/Compiladores/ProyectoEvaluado/ProyectoMario_Jeff/MiniGO.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiniGOParser extends Parser {
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
	public static final int
		RULE_root = 0, RULE_topDeclarationList = 1, RULE_variableDecl = 2, RULE_innerVarDecls = 3, 
		RULE_singleVarDecl = 4, RULE_singleVarDeclNoExps = 5, RULE_identifierList = 6, 
		RULE_typeDecl = 7, RULE_innerTypeDecls = 8, RULE_singleTypeDecl = 9, RULE_declType = 10, 
		RULE_sliceDeclType = 11, RULE_arrayDeclType = 12, RULE_structDeclType = 13, 
		RULE_structMemDecls = 14, RULE_funcDecl = 15, RULE_funcFrontDecl = 16, 
		RULE_funcArgDecls = 17, RULE_expressionList = 18, RULE_expression = 19, 
		RULE_primaryExpression = 20, RULE_operand = 21, RULE_literal = 22, RULE_selector = 23, 
		RULE_index = 24, RULE_arguments = 25, RULE_appendExpression = 26, RULE_lengthExpression = 27, 
		RULE_capExpression = 28, RULE_block = 29, RULE_statementList = 30, RULE_statement = 31, 
		RULE_simpleStatement = 32, RULE_assignmentStatement = 33, RULE_ifStatement = 34, 
		RULE_loop = 35, RULE_switchStatement = 36, RULE_expressionCaseClauseList = 37, 
		RULE_expressionCaseClause = 38, RULE_expressionSwitchCase = 39;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "topDeclarationList", "variableDecl", "innerVarDecls", "singleVarDecl", 
			"singleVarDeclNoExps", "identifierList", "typeDecl", "innerTypeDecls", 
			"singleTypeDecl", "declType", "sliceDeclType", "arrayDeclType", "structDeclType", 
			"structMemDecls", "funcDecl", "funcFrontDecl", "funcArgDecls", "expressionList", 
			"expression", "primaryExpression", "operand", "literal", "selector", 
			"index", "arguments", "appendExpression", "lengthExpression", "capExpression", 
			"block", "statementList", "statement", "simpleStatement", "assignmentStatement", 
			"ifStatement", "loop", "switchStatement", "expressionCaseClauseList", 
			"expressionCaseClause", "expressionSwitchCase"
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

	@Override
	public String getGrammarFileName() { return "MiniGO.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniGOParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public TerminalNode PACKAGE() { return getToken(MiniGOParser.PACKAGE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(MiniGOParser.IDENTIFIER, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public TopDeclarationListContext topDeclarationList() {
			return getRuleContext(TopDeclarationListContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MiniGOParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(PACKAGE);
			setState(81);
			match(IDENTIFIER);
			setState(82);
			match(SEMICOLON);
			setState(83);
			topDeclarationList();
			setState(84);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TopDeclarationListContext extends ParserRuleContext {
		public List<VariableDeclContext> variableDecl() {
			return getRuleContexts(VariableDeclContext.class);
		}
		public VariableDeclContext variableDecl(int i) {
			return getRuleContext(VariableDeclContext.class,i);
		}
		public List<TypeDeclContext> typeDecl() {
			return getRuleContexts(TypeDeclContext.class);
		}
		public TypeDeclContext typeDecl(int i) {
			return getRuleContext(TypeDeclContext.class,i);
		}
		public List<FuncDeclContext> funcDecl() {
			return getRuleContexts(FuncDeclContext.class);
		}
		public FuncDeclContext funcDecl(int i) {
			return getRuleContext(FuncDeclContext.class,i);
		}
		public TopDeclarationListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topDeclarationList; }
	}

	public final TopDeclarationListContext topDeclarationList() throws RecognitionException {
		TopDeclarationListContext _localctx = new TopDeclarationListContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_topDeclarationList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << TYPE) | (1L << FUNC))) != 0)) {
				{
				setState(89);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case VAR:
					{
					setState(86);
					variableDecl();
					}
					break;
				case TYPE:
					{
					setState(87);
					typeDecl();
					}
					break;
				case FUNC:
					{
					setState(88);
					funcDecl();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(MiniGOParser.VAR, 0); }
		public SingleVarDeclContext singleVarDecl() {
			return getRuleContext(SingleVarDeclContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public InnerVarDeclsContext innerVarDecls() {
			return getRuleContext(InnerVarDeclsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public VariableDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDecl; }
	}

	public final VariableDeclContext variableDecl() throws RecognitionException {
		VariableDeclContext _localctx = new VariableDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variableDecl);
		try {
			setState(108);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(VAR);
				setState(95);
				singleVarDecl();
				setState(96);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(98);
				match(VAR);
				setState(99);
				match(LPAREN);
				setState(100);
				innerVarDecls();
				setState(101);
				match(RPAREN);
				setState(102);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(104);
				match(VAR);
				setState(105);
				match(LPAREN);
				setState(106);
				match(RPAREN);
				setState(107);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InnerVarDeclsContext extends ParserRuleContext {
		public List<SingleVarDeclContext> singleVarDecl() {
			return getRuleContexts(SingleVarDeclContext.class);
		}
		public SingleVarDeclContext singleVarDecl(int i) {
			return getRuleContext(SingleVarDeclContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(MiniGOParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiniGOParser.SEMICOLON, i);
		}
		public InnerVarDeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_innerVarDecls; }
	}

	public final InnerVarDeclsContext innerVarDecls() throws RecognitionException {
		InnerVarDeclsContext _localctx = new InnerVarDeclsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_innerVarDecls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			singleVarDecl();
			setState(111);
			match(SEMICOLON);
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(112);
				singleVarDecl();
				setState(113);
				match(SEMICOLON);
				}
				}
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SingleVarDeclContext extends ParserRuleContext {
		public SingleVarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleVarDecl; }
	 
		public SingleVarDeclContext() { }
		public void copyFrom(SingleVarDeclContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VarDeclNoExpsContext extends SingleVarDeclContext {
		public SingleVarDeclNoExpsContext singleVarDeclNoExps() {
			return getRuleContext(SingleVarDeclNoExpsContext.class,0);
		}
		public VarDeclNoExpsContext(SingleVarDeclContext ctx) { copyFrom(ctx); }
	}
	public static class VarDeclWithTypeAndValueContext extends SingleVarDeclContext {
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(MiniGOParser.ASSIGN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public VarDeclWithTypeAndValueContext(SingleVarDeclContext ctx) { copyFrom(ctx); }
	}
	public static class VarDeclWithValueContext extends SingleVarDeclContext {
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(MiniGOParser.ASSIGN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public VarDeclWithValueContext(SingleVarDeclContext ctx) { copyFrom(ctx); }
	}

	public final SingleVarDeclContext singleVarDecl() throws RecognitionException {
		SingleVarDeclContext _localctx = new SingleVarDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_singleVarDecl);
		try {
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				_localctx = new VarDeclWithTypeAndValueContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				identifierList();
				setState(121);
				declType();
				setState(122);
				match(ASSIGN);
				setState(123);
				expressionList();
				}
				break;
			case 2:
				_localctx = new VarDeclWithValueContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(125);
				identifierList();
				setState(126);
				match(ASSIGN);
				setState(127);
				expressionList();
				}
				break;
			case 3:
				_localctx = new VarDeclNoExpsContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(129);
				singleVarDeclNoExps();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SingleVarDeclNoExpsContext extends ParserRuleContext {
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public SingleVarDeclNoExpsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleVarDeclNoExps; }
	}

	public final SingleVarDeclNoExpsContext singleVarDeclNoExps() throws RecognitionException {
		SingleVarDeclNoExpsContext _localctx = new SingleVarDeclNoExpsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_singleVarDeclNoExps);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			identifierList();
			setState(133);
			declType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierListContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(MiniGOParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(MiniGOParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGOParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGOParser.COMMA, i);
		}
		public IdentifierListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierList; }
	}

	public final IdentifierListContext identifierList() throws RecognitionException {
		IdentifierListContext _localctx = new IdentifierListContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_identifierList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(IDENTIFIER);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(136);
				match(COMMA);
				setState(137);
				match(IDENTIFIER);
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeDeclContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(MiniGOParser.TYPE, 0); }
		public SingleTypeDeclContext singleTypeDecl() {
			return getRuleContext(SingleTypeDeclContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public InnerTypeDeclsContext innerTypeDecls() {
			return getRuleContext(InnerTypeDeclsContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public TypeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeDecl; }
	}

	public final TypeDeclContext typeDecl() throws RecognitionException {
		TypeDeclContext _localctx = new TypeDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_typeDecl);
		try {
			setState(157);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(143);
				match(TYPE);
				setState(144);
				singleTypeDecl();
				setState(145);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				match(TYPE);
				setState(148);
				match(LPAREN);
				setState(149);
				innerTypeDecls();
				setState(150);
				match(RPAREN);
				setState(151);
				match(SEMICOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(153);
				match(TYPE);
				setState(154);
				match(LPAREN);
				setState(155);
				match(RPAREN);
				setState(156);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InnerTypeDeclsContext extends ParserRuleContext {
		public List<SingleTypeDeclContext> singleTypeDecl() {
			return getRuleContexts(SingleTypeDeclContext.class);
		}
		public SingleTypeDeclContext singleTypeDecl(int i) {
			return getRuleContext(SingleTypeDeclContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(MiniGOParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiniGOParser.SEMICOLON, i);
		}
		public InnerTypeDeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_innerTypeDecls; }
	}

	public final InnerTypeDeclsContext innerTypeDecls() throws RecognitionException {
		InnerTypeDeclsContext _localctx = new InnerTypeDeclsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_innerTypeDecls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			singleTypeDecl();
			setState(160);
			match(SEMICOLON);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(161);
				singleTypeDecl();
				setState(162);
				match(SEMICOLON);
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SingleTypeDeclContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MiniGOParser.IDENTIFIER, 0); }
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public SingleTypeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleTypeDecl; }
	}

	public final SingleTypeDeclContext singleTypeDecl() throws RecognitionException {
		SingleTypeDeclContext _localctx = new SingleTypeDeclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_singleTypeDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(IDENTIFIER);
			setState(170);
			declType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclTypeContext extends ParserRuleContext {
		public DeclTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declType; }
	 
		public DeclTypeContext() { }
		public void copyFrom(DeclTypeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SimpleTypeContext extends DeclTypeContext {
		public TerminalNode IDENTIFIER() { return getToken(MiniGOParser.IDENTIFIER, 0); }
		public SimpleTypeContext(DeclTypeContext ctx) { copyFrom(ctx); }
	}
	public static class GroupedTypeContext extends DeclTypeContext {
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public GroupedTypeContext(DeclTypeContext ctx) { copyFrom(ctx); }
	}
	public static class ArrayTypeContext extends DeclTypeContext {
		public ArrayDeclTypeContext arrayDeclType() {
			return getRuleContext(ArrayDeclTypeContext.class,0);
		}
		public ArrayTypeContext(DeclTypeContext ctx) { copyFrom(ctx); }
	}
	public static class StructTypeContext extends DeclTypeContext {
		public StructDeclTypeContext structDeclType() {
			return getRuleContext(StructDeclTypeContext.class,0);
		}
		public StructTypeContext(DeclTypeContext ctx) { copyFrom(ctx); }
	}
	public static class SliceTypeContext extends DeclTypeContext {
		public SliceDeclTypeContext sliceDeclType() {
			return getRuleContext(SliceDeclTypeContext.class,0);
		}
		public SliceTypeContext(DeclTypeContext ctx) { copyFrom(ctx); }
	}

	public final DeclTypeContext declType() throws RecognitionException {
		DeclTypeContext _localctx = new DeclTypeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_declType);
		try {
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				_localctx = new GroupedTypeContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(172);
				match(LPAREN);
				setState(173);
				declType();
				setState(174);
				match(RPAREN);
				}
				break;
			case 2:
				_localctx = new SimpleTypeContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(176);
				match(IDENTIFIER);
				}
				break;
			case 3:
				_localctx = new SliceTypeContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(177);
				sliceDeclType();
				}
				break;
			case 4:
				_localctx = new ArrayTypeContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(178);
				arrayDeclType();
				}
				break;
			case 5:
				_localctx = new StructTypeContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(179);
				structDeclType();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SliceDeclTypeContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(MiniGOParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(MiniGOParser.RBRACKET, 0); }
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public SliceDeclTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sliceDeclType; }
	}

	public final SliceDeclTypeContext sliceDeclType() throws RecognitionException {
		SliceDeclTypeContext _localctx = new SliceDeclTypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_sliceDeclType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(LBRACKET);
			setState(183);
			match(RBRACKET);
			setState(184);
			declType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayDeclTypeContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(MiniGOParser.LBRACKET, 0); }
		public TerminalNode INTLITERAL() { return getToken(MiniGOParser.INTLITERAL, 0); }
		public TerminalNode RBRACKET() { return getToken(MiniGOParser.RBRACKET, 0); }
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public ArrayDeclTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayDeclType; }
	}

	public final ArrayDeclTypeContext arrayDeclType() throws RecognitionException {
		ArrayDeclTypeContext _localctx = new ArrayDeclTypeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_arrayDeclType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			match(LBRACKET);
			setState(187);
			match(INTLITERAL);
			setState(188);
			match(RBRACKET);
			setState(189);
			declType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StructDeclTypeContext extends ParserRuleContext {
		public TerminalNode STRUCT() { return getToken(MiniGOParser.STRUCT, 0); }
		public TerminalNode LBRACE() { return getToken(MiniGOParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(MiniGOParser.RBRACE, 0); }
		public StructMemDeclsContext structMemDecls() {
			return getRuleContext(StructMemDeclsContext.class,0);
		}
		public StructDeclTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structDeclType; }
	}

	public final StructDeclTypeContext structDeclType() throws RecognitionException {
		StructDeclTypeContext _localctx = new StructDeclTypeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_structDeclType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(STRUCT);
			setState(192);
			match(LBRACE);
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(193);
				structMemDecls();
				}
			}

			setState(196);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StructMemDeclsContext extends ParserRuleContext {
		public List<SingleVarDeclNoExpsContext> singleVarDeclNoExps() {
			return getRuleContexts(SingleVarDeclNoExpsContext.class);
		}
		public SingleVarDeclNoExpsContext singleVarDeclNoExps(int i) {
			return getRuleContext(SingleVarDeclNoExpsContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(MiniGOParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiniGOParser.SEMICOLON, i);
		}
		public StructMemDeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structMemDecls; }
	}

	public final StructMemDeclsContext structMemDecls() throws RecognitionException {
		StructMemDeclsContext _localctx = new StructMemDeclsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_structMemDecls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			singleVarDeclNoExps();
			setState(199);
			match(SEMICOLON);
			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(200);
				singleVarDeclNoExps();
				setState(201);
				match(SEMICOLON);
				}
				}
				setState(207);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncDeclContext extends ParserRuleContext {
		public FuncFrontDeclContext funcFrontDecl() {
			return getRuleContext(FuncFrontDeclContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public FuncDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcDecl; }
	}

	public final FuncDeclContext funcDecl() throws RecognitionException {
		FuncDeclContext _localctx = new FuncDeclContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_funcDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			funcFrontDecl();
			setState(209);
			block();
			setState(210);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncFrontDeclContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(MiniGOParser.FUNC, 0); }
		public TerminalNode IDENTIFIER() { return getToken(MiniGOParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public FuncArgDeclsContext funcArgDecls() {
			return getRuleContext(FuncArgDeclsContext.class,0);
		}
		public DeclTypeContext declType() {
			return getRuleContext(DeclTypeContext.class,0);
		}
		public FuncFrontDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcFrontDecl; }
	}

	public final FuncFrontDeclContext funcFrontDecl() throws RecognitionException {
		FuncFrontDeclContext _localctx = new FuncFrontDeclContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_funcFrontDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(FUNC);
			setState(213);
			match(IDENTIFIER);
			setState(214);
			match(LPAREN);
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(215);
				funcArgDecls();
				}
			}

			setState(218);
			match(RPAREN);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STRUCT) | (1L << LPAREN) | (1L << LBRACKET))) != 0) || _la==IDENTIFIER) {
				{
				setState(219);
				declType();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncArgDeclsContext extends ParserRuleContext {
		public List<SingleVarDeclNoExpsContext> singleVarDeclNoExps() {
			return getRuleContexts(SingleVarDeclNoExpsContext.class);
		}
		public SingleVarDeclNoExpsContext singleVarDeclNoExps(int i) {
			return getRuleContext(SingleVarDeclNoExpsContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGOParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGOParser.COMMA, i);
		}
		public FuncArgDeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcArgDecls; }
	}

	public final FuncArgDeclsContext funcArgDecls() throws RecognitionException {
		FuncArgDeclsContext _localctx = new FuncArgDeclsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_funcArgDecls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			singleVarDeclNoExps();
			setState(227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(223);
				match(COMMA);
				setState(224);
				singleVarDeclNoExps();
				}
				}
				setState(229);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MiniGOParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MiniGOParser.COMMA, i);
		}
		public ExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionList; }
	}

	public final ExpressionListContext expressionList() throws RecognitionException {
		ExpressionListContext _localctx = new ExpressionListContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_expressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			expression(0);
			setState(235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(231);
				match(COMMA);
				setState(232);
				expression(0);
				}
				}
				setState(237);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PipeExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PIPE() { return getToken(MiniGOParser.PIPE, 0); }
		public PipeExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class ModExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MOD() { return getToken(MiniGOParser.MOD, 0); }
		public ModExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class GtExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GT() { return getToken(MiniGOParser.GT, 0); }
		public GtExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class XorUnaryExprContext extends ExpressionContext {
		public TerminalNode XOR() { return getToken(MiniGOParser.XOR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public XorUnaryExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class RshiftExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RSHIFT() { return getToken(MiniGOParser.RSHIFT, 0); }
		public RshiftExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class OrExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(MiniGOParser.OR, 0); }
		public OrExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class SubExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(MiniGOParser.MINUS, 0); }
		public SubExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class MultExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MULT() { return getToken(MiniGOParser.MULT, 0); }
		public MultExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class XorExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode XOR() { return getToken(MiniGOParser.XOR, 0); }
		public XorExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NeqExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode NEQ() { return getToken(MiniGOParser.NEQ, 0); }
		public NeqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AmpExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AMP() { return getToken(MiniGOParser.AMP, 0); }
		public AmpExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class EqExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(MiniGOParser.EQ, 0); }
		public EqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LtExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LT() { return getToken(MiniGOParser.LT, 0); }
		public LtExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class NotExprContext extends ExpressionContext {
		public TerminalNode NOT() { return getToken(MiniGOParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NotExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class PrimaryExprContext extends ExpressionContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public PrimaryExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class UnaryMinusExprContext extends ExpressionContext {
		public TerminalNode MINUS() { return getToken(MiniGOParser.MINUS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public UnaryMinusExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AmpxorExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AMPXOR() { return getToken(MiniGOParser.AMPXOR, 0); }
		public AmpxorExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AddExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(MiniGOParser.PLUS, 0); }
		public AddExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class UnaryPlusExprContext extends ExpressionContext {
		public TerminalNode PLUS() { return getToken(MiniGOParser.PLUS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public UnaryPlusExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LeqExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LEQ() { return getToken(MiniGOParser.LEQ, 0); }
		public LeqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class DivExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode DIV() { return getToken(MiniGOParser.DIV, 0); }
		public DivExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class GeqExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GEQ() { return getToken(MiniGOParser.GEQ, 0); }
		public GeqExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class LshiftExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LSHIFT() { return getToken(MiniGOParser.LSHIFT, 0); }
		public LshiftExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AndExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(MiniGOParser.AND, 0); }
		public AndExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case APPEND:
			case LEN:
			case CAP:
			case LPAREN:
			case INTLITERAL:
			case FLOATLITERAL:
			case RUNELITERAL:
			case RAWSTRINGLITERAL:
			case INTERPRETEDSTRINGLITERAL:
			case IDENTIFIER:
				{
				_localctx = new PrimaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(239);
				primaryExpression(0);
				}
				break;
			case PLUS:
				{
				_localctx = new UnaryPlusExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(240);
				match(PLUS);
				setState(241);
				expression(4);
				}
				break;
			case MINUS:
				{
				_localctx = new UnaryMinusExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(242);
				match(MINUS);
				setState(243);
				expression(3);
				}
				break;
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(244);
				match(NOT);
				setState(245);
				expression(2);
				}
				break;
			case XOR:
				{
				_localctx = new XorUnaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(246);
				match(XOR);
				setState(247);
				expression(1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(309);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(307);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new MultExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(250);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(251);
						match(MULT);
						setState(252);
						expression(24);
						}
						break;
					case 2:
						{
						_localctx = new DivExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(253);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(254);
						match(DIV);
						setState(255);
						expression(23);
						}
						break;
					case 3:
						{
						_localctx = new ModExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(256);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(257);
						match(MOD);
						setState(258);
						expression(22);
						}
						break;
					case 4:
						{
						_localctx = new LshiftExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(259);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(260);
						match(LSHIFT);
						setState(261);
						expression(21);
						}
						break;
					case 5:
						{
						_localctx = new RshiftExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(262);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(263);
						match(RSHIFT);
						setState(264);
						expression(20);
						}
						break;
					case 6:
						{
						_localctx = new AmpExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(265);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(266);
						match(AMP);
						setState(267);
						expression(19);
						}
						break;
					case 7:
						{
						_localctx = new AmpxorExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(268);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(269);
						match(AMPXOR);
						setState(270);
						expression(18);
						}
						break;
					case 8:
						{
						_localctx = new AddExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(271);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(272);
						match(PLUS);
						setState(273);
						expression(17);
						}
						break;
					case 9:
						{
						_localctx = new SubExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(274);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(275);
						match(MINUS);
						setState(276);
						expression(16);
						}
						break;
					case 10:
						{
						_localctx = new PipeExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(277);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(278);
						match(PIPE);
						setState(279);
						expression(15);
						}
						break;
					case 11:
						{
						_localctx = new XorExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(280);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(281);
						match(XOR);
						setState(282);
						expression(14);
						}
						break;
					case 12:
						{
						_localctx = new EqExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(283);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(284);
						match(EQ);
						setState(285);
						expression(13);
						}
						break;
					case 13:
						{
						_localctx = new NeqExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(286);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(287);
						match(NEQ);
						setState(288);
						expression(12);
						}
						break;
					case 14:
						{
						_localctx = new LtExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(289);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(290);
						match(LT);
						setState(291);
						expression(11);
						}
						break;
					case 15:
						{
						_localctx = new LeqExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(292);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(293);
						match(LEQ);
						setState(294);
						expression(10);
						}
						break;
					case 16:
						{
						_localctx = new GtExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(295);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(296);
						match(GT);
						setState(297);
						expression(9);
						}
						break;
					case 17:
						{
						_localctx = new GeqExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(298);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(299);
						match(GEQ);
						setState(300);
						expression(8);
						}
						break;
					case 18:
						{
						_localctx = new AndExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(301);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(302);
						match(AND);
						setState(303);
						expression(7);
						}
						break;
					case 19:
						{
						_localctx = new OrExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(304);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(305);
						match(OR);
						setState(306);
						expression(6);
						}
						break;
					}
					} 
				}
				setState(311);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PrimaryExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	 
		public PrimaryExpressionContext() { }
		public void copyFrom(PrimaryExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LengthExprContext extends PrimaryExpressionContext {
		public LengthExpressionContext lengthExpression() {
			return getRuleContext(LengthExpressionContext.class,0);
		}
		public LengthExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class IndexExprContext extends PrimaryExpressionContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public IndexContext index() {
			return getRuleContext(IndexContext.class,0);
		}
		public IndexExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class SelectorExprContext extends PrimaryExpressionContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public SelectorContext selector() {
			return getRuleContext(SelectorContext.class,0);
		}
		public SelectorExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class OperandExprContext extends PrimaryExpressionContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public OperandExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class AppendExprContext extends PrimaryExpressionContext {
		public AppendExpressionContext appendExpression() {
			return getRuleContext(AppendExpressionContext.class,0);
		}
		public AppendExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CallExprContext extends PrimaryExpressionContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public CallExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class CapExprContext extends PrimaryExpressionContext {
		public CapExpressionContext capExpression() {
			return getRuleContext(CapExpressionContext.class,0);
		}
		public CapExprContext(PrimaryExpressionContext ctx) { copyFrom(ctx); }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		return primaryExpression(0);
	}

	private PrimaryExpressionContext primaryExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, _parentState);
		PrimaryExpressionContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_primaryExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
			case INTLITERAL:
			case FLOATLITERAL:
			case RUNELITERAL:
			case RAWSTRINGLITERAL:
			case INTERPRETEDSTRINGLITERAL:
			case IDENTIFIER:
				{
				_localctx = new OperandExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(313);
				operand();
				}
				break;
			case APPEND:
				{
				_localctx = new AppendExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(314);
				appendExpression();
				}
				break;
			case LEN:
				{
				_localctx = new LengthExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(315);
				lengthExpression();
				}
				break;
			case CAP:
				{
				_localctx = new CapExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(316);
				capExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(327);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(325);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						_localctx = new SelectorExprContext(new PrimaryExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(319);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(320);
						selector();
						}
						break;
					case 2:
						{
						_localctx = new IndexExprContext(new PrimaryExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(321);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(322);
						index();
						}
						break;
					case 3:
						{
						_localctx = new CallExprContext(new PrimaryExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(323);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(324);
						arguments();
						}
						break;
					}
					} 
				}
				setState(329);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class OperandContext extends ParserRuleContext {
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	 
		public OperandContext() { }
		public void copyFrom(OperandContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class GroupedExprContext extends OperandContext {
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public GroupedExprContext(OperandContext ctx) { copyFrom(ctx); }
	}
	public static class LiteralOperandContext extends OperandContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public LiteralOperandContext(OperandContext ctx) { copyFrom(ctx); }
	}
	public static class IdentifierOperandContext extends OperandContext {
		public TerminalNode IDENTIFIER() { return getToken(MiniGOParser.IDENTIFIER, 0); }
		public IdentifierOperandContext(OperandContext ctx) { copyFrom(ctx); }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_operand);
		try {
			setState(336);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTLITERAL:
			case FLOATLITERAL:
			case RUNELITERAL:
			case RAWSTRINGLITERAL:
			case INTERPRETEDSTRINGLITERAL:
				_localctx = new LiteralOperandContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(330);
				literal();
				}
				break;
			case IDENTIFIER:
				_localctx = new IdentifierOperandContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(331);
				match(IDENTIFIER);
				}
				break;
			case LPAREN:
				_localctx = new GroupedExprContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(332);
				match(LPAREN);
				setState(333);
				expression(0);
				setState(334);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	 
		public LiteralContext() { }
		public void copyFrom(LiteralContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FloatLitContext extends LiteralContext {
		public TerminalNode FLOATLITERAL() { return getToken(MiniGOParser.FLOATLITERAL, 0); }
		public FloatLitContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class RuneLitContext extends LiteralContext {
		public TerminalNode RUNELITERAL() { return getToken(MiniGOParser.RUNELITERAL, 0); }
		public RuneLitContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class IntLitContext extends LiteralContext {
		public TerminalNode INTLITERAL() { return getToken(MiniGOParser.INTLITERAL, 0); }
		public IntLitContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class InterpretedStringLitContext extends LiteralContext {
		public TerminalNode INTERPRETEDSTRINGLITERAL() { return getToken(MiniGOParser.INTERPRETEDSTRINGLITERAL, 0); }
		public InterpretedStringLitContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	public static class RawStringLitContext extends LiteralContext {
		public TerminalNode RAWSTRINGLITERAL() { return getToken(MiniGOParser.RAWSTRINGLITERAL, 0); }
		public RawStringLitContext(LiteralContext ctx) { copyFrom(ctx); }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_literal);
		try {
			setState(343);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTLITERAL:
				_localctx = new IntLitContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				match(INTLITERAL);
				}
				break;
			case FLOATLITERAL:
				_localctx = new FloatLitContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(339);
				match(FLOATLITERAL);
				}
				break;
			case RUNELITERAL:
				_localctx = new RuneLitContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(340);
				match(RUNELITERAL);
				}
				break;
			case RAWSTRINGLITERAL:
				_localctx = new RawStringLitContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(341);
				match(RAWSTRINGLITERAL);
				}
				break;
			case INTERPRETEDSTRINGLITERAL:
				_localctx = new InterpretedStringLitContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(342);
				match(INTERPRETEDSTRINGLITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectorContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(MiniGOParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(MiniGOParser.IDENTIFIER, 0); }
		public SelectorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selector; }
	}

	public final SelectorContext selector() throws RecognitionException {
		SelectorContext _localctx = new SelectorContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_selector);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			match(DOT);
			setState(346);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IndexContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(MiniGOParser.LBRACKET, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(MiniGOParser.RBRACKET, 0); }
		public IndexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index; }
	}

	public final IndexContext index() throws RecognitionException {
		IndexContext _localctx = new IndexContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_index);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(LBRACKET);
			setState(349);
			expression(0);
			setState(350);
			match(RBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentsContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(352);
			match(LPAREN);
			setState(354);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 17)) & ~0x3f) == 0 && ((1L << (_la - 17)) & ((1L << (APPEND - 17)) | (1L << (LEN - 17)) | (1L << (CAP - 17)) | (1L << (PLUS - 17)) | (1L << (MINUS - 17)) | (1L << (XOR - 17)) | (1L << (NOT - 17)) | (1L << (LPAREN - 17)) | (1L << (INTLITERAL - 17)) | (1L << (FLOATLITERAL - 17)) | (1L << (RUNELITERAL - 17)) | (1L << (RAWSTRINGLITERAL - 17)) | (1L << (INTERPRETEDSTRINGLITERAL - 17)) | (1L << (IDENTIFIER - 17)))) != 0)) {
				{
				setState(353);
				expressionList();
				}
			}

			setState(356);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AppendExpressionContext extends ParserRuleContext {
		public TerminalNode APPEND() { return getToken(MiniGOParser.APPEND, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(MiniGOParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public AppendExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_appendExpression; }
	}

	public final AppendExpressionContext appendExpression() throws RecognitionException {
		AppendExpressionContext _localctx = new AppendExpressionContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_appendExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(358);
			match(APPEND);
			setState(359);
			match(LPAREN);
			setState(360);
			expression(0);
			setState(361);
			match(COMMA);
			setState(362);
			expression(0);
			setState(363);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LengthExpressionContext extends ParserRuleContext {
		public TerminalNode LEN() { return getToken(MiniGOParser.LEN, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public LengthExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lengthExpression; }
	}

	public final LengthExpressionContext lengthExpression() throws RecognitionException {
		LengthExpressionContext _localctx = new LengthExpressionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_lengthExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			match(LEN);
			setState(366);
			match(LPAREN);
			setState(367);
			expression(0);
			setState(368);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CapExpressionContext extends ParserRuleContext {
		public TerminalNode CAP() { return getToken(MiniGOParser.CAP, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public CapExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_capExpression; }
	}

	public final CapExpressionContext capExpression() throws RecognitionException {
		CapExpressionContext _localctx = new CapExpressionContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_capExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			match(CAP);
			setState(371);
			match(LPAREN);
			setState(372);
			expression(0);
			setState(373);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(MiniGOParser.LBRACE, 0); }
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(MiniGOParser.RBRACE, 0); }
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			match(LBRACE);
			setState(376);
			statementList();
			setState(377);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementListContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public StatementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementList; }
	}

	public final StatementListContext statementList() throws RecognitionException {
		StatementListContext _localctx = new StatementListContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_statementList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << TYPE) | (1L << IF) | (1L << FOR) | (1L << SWITCH) | (1L << RETURN) | (1L << BREAK) | (1L << CONTINUE) | (1L << PRINT) | (1L << PRINTLN) | (1L << APPEND) | (1L << LEN) | (1L << CAP) | (1L << PLUS) | (1L << MINUS) | (1L << XOR) | (1L << NOT) | (1L << LPAREN) | (1L << LBRACE) | (1L << SEMICOLON))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (INTLITERAL - 65)) | (1L << (FLOATLITERAL - 65)) | (1L << (RUNELITERAL - 65)) | (1L << (RAWSTRINGLITERAL - 65)) | (1L << (INTERPRETEDSTRINGLITERAL - 65)) | (1L << (IDENTIFIER - 65)))) != 0)) {
				{
				{
				setState(379);
				statement();
				}
				}
				setState(384);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SwitchStmtContext extends StatementContext {
		public SwitchStatementContext switchStatement() {
			return getRuleContext(SwitchStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public SwitchStmtContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class PrintStatementContext extends StatementContext {
		public TerminalNode PRINT() { return getToken(MiniGOParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public PrintStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class SimpleStmtContext extends StatementContext {
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public SimpleStmtContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class LoopStmtContext extends StatementContext {
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public LoopStmtContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class BlockStatementContext extends StatementContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public BlockStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class VarDeclStatementContext extends StatementContext {
		public VariableDeclContext variableDecl() {
			return getRuleContext(VariableDeclContext.class,0);
		}
		public VarDeclStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfStmtContext extends StatementContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public IfStmtContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class TypeDeclStatementContext extends StatementContext {
		public TypeDeclContext typeDecl() {
			return getRuleContext(TypeDeclContext.class,0);
		}
		public TypeDeclStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class BreakStatementContext extends StatementContext {
		public TerminalNode BREAK() { return getToken(MiniGOParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public BreakStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ContinueStatementContext extends StatementContext {
		public TerminalNode CONTINUE() { return getToken(MiniGOParser.CONTINUE, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ContinueStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class ReturnStatementContext extends StatementContext {
		public TerminalNode RETURN() { return getToken(MiniGOParser.RETURN, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class PrintlnStatementContext extends StatementContext {
		public TerminalNode PRINTLN() { return getToken(MiniGOParser.PRINTLN, 0); }
		public TerminalNode LPAREN() { return getToken(MiniGOParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(MiniGOParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public PrintlnStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_statement);
		int _la;
		try {
			setState(425);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				_localctx = new PrintStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(385);
				match(PRINT);
				setState(386);
				match(LPAREN);
				setState(388);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 17)) & ~0x3f) == 0 && ((1L << (_la - 17)) & ((1L << (APPEND - 17)) | (1L << (LEN - 17)) | (1L << (CAP - 17)) | (1L << (PLUS - 17)) | (1L << (MINUS - 17)) | (1L << (XOR - 17)) | (1L << (NOT - 17)) | (1L << (LPAREN - 17)) | (1L << (INTLITERAL - 17)) | (1L << (FLOATLITERAL - 17)) | (1L << (RUNELITERAL - 17)) | (1L << (RAWSTRINGLITERAL - 17)) | (1L << (INTERPRETEDSTRINGLITERAL - 17)) | (1L << (IDENTIFIER - 17)))) != 0)) {
					{
					setState(387);
					expressionList();
					}
				}

				setState(390);
				match(RPAREN);
				setState(391);
				match(SEMICOLON);
				}
				break;
			case PRINTLN:
				_localctx = new PrintlnStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(392);
				match(PRINTLN);
				setState(393);
				match(LPAREN);
				setState(395);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 17)) & ~0x3f) == 0 && ((1L << (_la - 17)) & ((1L << (APPEND - 17)) | (1L << (LEN - 17)) | (1L << (CAP - 17)) | (1L << (PLUS - 17)) | (1L << (MINUS - 17)) | (1L << (XOR - 17)) | (1L << (NOT - 17)) | (1L << (LPAREN - 17)) | (1L << (INTLITERAL - 17)) | (1L << (FLOATLITERAL - 17)) | (1L << (RUNELITERAL - 17)) | (1L << (RAWSTRINGLITERAL - 17)) | (1L << (INTERPRETEDSTRINGLITERAL - 17)) | (1L << (IDENTIFIER - 17)))) != 0)) {
					{
					setState(394);
					expressionList();
					}
				}

				setState(397);
				match(RPAREN);
				setState(398);
				match(SEMICOLON);
				}
				break;
			case RETURN:
				_localctx = new ReturnStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(399);
				match(RETURN);
				setState(401);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 17)) & ~0x3f) == 0 && ((1L << (_la - 17)) & ((1L << (APPEND - 17)) | (1L << (LEN - 17)) | (1L << (CAP - 17)) | (1L << (PLUS - 17)) | (1L << (MINUS - 17)) | (1L << (XOR - 17)) | (1L << (NOT - 17)) | (1L << (LPAREN - 17)) | (1L << (INTLITERAL - 17)) | (1L << (FLOATLITERAL - 17)) | (1L << (RUNELITERAL - 17)) | (1L << (RAWSTRINGLITERAL - 17)) | (1L << (INTERPRETEDSTRINGLITERAL - 17)) | (1L << (IDENTIFIER - 17)))) != 0)) {
					{
					setState(400);
					expression(0);
					}
				}

				setState(403);
				match(SEMICOLON);
				}
				break;
			case BREAK:
				_localctx = new BreakStatementContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(404);
				match(BREAK);
				setState(405);
				match(SEMICOLON);
				}
				break;
			case CONTINUE:
				_localctx = new ContinueStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(406);
				match(CONTINUE);
				setState(407);
				match(SEMICOLON);
				}
				break;
			case APPEND:
			case LEN:
			case CAP:
			case PLUS:
			case MINUS:
			case XOR:
			case NOT:
			case LPAREN:
			case SEMICOLON:
			case INTLITERAL:
			case FLOATLITERAL:
			case RUNELITERAL:
			case RAWSTRINGLITERAL:
			case INTERPRETEDSTRINGLITERAL:
			case IDENTIFIER:
				_localctx = new SimpleStmtContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(408);
				simpleStatement();
				setState(409);
				match(SEMICOLON);
				}
				break;
			case LBRACE:
				_localctx = new BlockStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(411);
				block();
				setState(412);
				match(SEMICOLON);
				}
				break;
			case SWITCH:
				_localctx = new SwitchStmtContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(414);
				switchStatement();
				setState(415);
				match(SEMICOLON);
				}
				break;
			case IF:
				_localctx = new IfStmtContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(417);
				ifStatement();
				setState(418);
				match(SEMICOLON);
				}
				break;
			case FOR:
				_localctx = new LoopStmtContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(420);
				loop();
				setState(421);
				match(SEMICOLON);
				}
				break;
			case TYPE:
				_localctx = new TypeDeclStatementContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(423);
				typeDecl();
				}
				break;
			case VAR:
				_localctx = new VarDeclStatementContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(424);
				variableDecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SimpleStatementContext extends ParserRuleContext {
		public SimpleStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStatement; }
	 
		public SimpleStatementContext() { }
		public void copyFrom(SimpleStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ShortVarDeclContext extends SimpleStatementContext {
		public List<ExpressionListContext> expressionList() {
			return getRuleContexts(ExpressionListContext.class);
		}
		public ExpressionListContext expressionList(int i) {
			return getRuleContext(ExpressionListContext.class,i);
		}
		public TerminalNode DECLARE_ASSIGN() { return getToken(MiniGOParser.DECLARE_ASSIGN, 0); }
		public ShortVarDeclContext(SimpleStatementContext ctx) { copyFrom(ctx); }
	}
	public static class EmptyStatementContext extends SimpleStatementContext {
		public EmptyStatementContext(SimpleStatementContext ctx) { copyFrom(ctx); }
	}
	public static class AssignStmtContext extends SimpleStatementContext {
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public AssignStmtContext(SimpleStatementContext ctx) { copyFrom(ctx); }
	}
	public static class IncDecStatementContext extends SimpleStatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode INC() { return getToken(MiniGOParser.INC, 0); }
		public TerminalNode DEC() { return getToken(MiniGOParser.DEC, 0); }
		public IncDecStatementContext(SimpleStatementContext ctx) { copyFrom(ctx); }
	}
	public static class ExpressionStatementContext extends SimpleStatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionStatementContext(SimpleStatementContext ctx) { copyFrom(ctx); }
	}

	public final SimpleStatementContext simpleStatement() throws RecognitionException {
		SimpleStatementContext _localctx = new SimpleStatementContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_simpleStatement);
		int _la;
		try {
			setState(437);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				_localctx = new IncDecStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(427);
				expression(0);
				setState(428);
				_la = _input.LA(1);
				if ( !(_la==INC || _la==DEC) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				_localctx = new ExpressionStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(430);
				expression(0);
				}
				break;
			case 3:
				_localctx = new AssignStmtContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(431);
				assignmentStatement();
				}
				break;
			case 4:
				_localctx = new ShortVarDeclContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(432);
				expressionList();
				setState(433);
				match(DECLARE_ASSIGN);
				setState(434);
				expressionList();
				}
				break;
			case 5:
				_localctx = new EmptyStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentStatementContext extends ParserRuleContext {
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
	 
		public AssignmentStatementContext() { }
		public void copyFrom(AssignmentStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LshiftAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LSHIFT_ASSIGN() { return getToken(MiniGOParser.LSHIFT_ASSIGN, 0); }
		public LshiftAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class RshiftAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RSHIFT_ASSIGN() { return getToken(MiniGOParser.RSHIFT_ASSIGN, 0); }
		public RshiftAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class PlusAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS_ASSIGN() { return getToken(MiniGOParser.PLUS_ASSIGN, 0); }
		public PlusAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class AmpxorAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AMPXOR_ASSIGN() { return getToken(MiniGOParser.AMPXOR_ASSIGN, 0); }
		public AmpxorAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class XorAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode XOR_ASSIGN() { return getToken(MiniGOParser.XOR_ASSIGN, 0); }
		public XorAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class SimpleAssignContext extends AssignmentStatementContext {
		public List<ExpressionListContext> expressionList() {
			return getRuleContexts(ExpressionListContext.class);
		}
		public ExpressionListContext expressionList(int i) {
			return getRuleContext(ExpressionListContext.class,i);
		}
		public TerminalNode ASSIGN() { return getToken(MiniGOParser.ASSIGN, 0); }
		public SimpleAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class DivAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode DIV_ASSIGN() { return getToken(MiniGOParser.DIV_ASSIGN, 0); }
		public DivAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class ModAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MOD_ASSIGN() { return getToken(MiniGOParser.MOD_ASSIGN, 0); }
		public ModAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class MultAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MULT_ASSIGN() { return getToken(MiniGOParser.MULT_ASSIGN, 0); }
		public MultAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class PipeAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PIPE_ASSIGN() { return getToken(MiniGOParser.PIPE_ASSIGN, 0); }
		public PipeAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class MinusAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MINUS_ASSIGN() { return getToken(MiniGOParser.MINUS_ASSIGN, 0); }
		public MinusAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}
	public static class AmpAssignContext extends AssignmentStatementContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AMP_ASSIGN() { return getToken(MiniGOParser.AMP_ASSIGN, 0); }
		public AmpAssignContext(AssignmentStatementContext ctx) { copyFrom(ctx); }
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_assignmentStatement);
		try {
			setState(487);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				_localctx = new SimpleAssignContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(439);
				expressionList();
				setState(440);
				match(ASSIGN);
				setState(441);
				expressionList();
				}
				break;
			case 2:
				_localctx = new PlusAssignContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(443);
				expression(0);
				setState(444);
				match(PLUS_ASSIGN);
				setState(445);
				expression(0);
				}
				break;
			case 3:
				_localctx = new MinusAssignContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(447);
				expression(0);
				setState(448);
				match(MINUS_ASSIGN);
				setState(449);
				expression(0);
				}
				break;
			case 4:
				_localctx = new MultAssignContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(451);
				expression(0);
				setState(452);
				match(MULT_ASSIGN);
				setState(453);
				expression(0);
				}
				break;
			case 5:
				_localctx = new DivAssignContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(455);
				expression(0);
				setState(456);
				match(DIV_ASSIGN);
				setState(457);
				expression(0);
				}
				break;
			case 6:
				_localctx = new ModAssignContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(459);
				expression(0);
				setState(460);
				match(MOD_ASSIGN);
				setState(461);
				expression(0);
				}
				break;
			case 7:
				_localctx = new AmpAssignContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(463);
				expression(0);
				setState(464);
				match(AMP_ASSIGN);
				setState(465);
				expression(0);
				}
				break;
			case 8:
				_localctx = new PipeAssignContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(467);
				expression(0);
				setState(468);
				match(PIPE_ASSIGN);
				setState(469);
				expression(0);
				}
				break;
			case 9:
				_localctx = new XorAssignContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(471);
				expression(0);
				setState(472);
				match(XOR_ASSIGN);
				setState(473);
				expression(0);
				}
				break;
			case 10:
				_localctx = new LshiftAssignContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(475);
				expression(0);
				setState(476);
				match(LSHIFT_ASSIGN);
				setState(477);
				expression(0);
				}
				break;
			case 11:
				_localctx = new RshiftAssignContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(479);
				expression(0);
				setState(480);
				match(RSHIFT_ASSIGN);
				setState(481);
				expression(0);
				}
				break;
			case 12:
				_localctx = new AmpxorAssignContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(483);
				expression(0);
				setState(484);
				match(AMPXOR_ASSIGN);
				setState(485);
				expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStatementContext extends ParserRuleContext {
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	 
		public IfStatementContext() { }
		public void copyFrom(IfStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IfWithInitContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(MiniGOParser.IF, 0); }
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfWithInitContext(IfStatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfWithInitElseIfContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(MiniGOParser.IF, 0); }
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode ELSE() { return getToken(MiniGOParser.ELSE, 0); }
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public IfWithInitElseIfContext(IfStatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfWithInitElseContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(MiniGOParser.IF, 0); }
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MiniGOParser.ELSE, 0); }
		public IfWithInitElseContext(IfStatementContext ctx) { copyFrom(ctx); }
	}
	public static class SimpleIfContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(MiniGOParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public SimpleIfContext(IfStatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfElseContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(MiniGOParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MiniGOParser.ELSE, 0); }
		public IfElseContext(IfStatementContext ctx) { copyFrom(ctx); }
	}
	public static class IfElseIfContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(MiniGOParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode ELSE() { return getToken(MiniGOParser.ELSE, 0); }
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public IfElseIfContext(IfStatementContext ctx) { copyFrom(ctx); }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_ifStatement);
		try {
			setState(527);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				_localctx = new SimpleIfContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(489);
				match(IF);
				setState(490);
				expression(0);
				setState(491);
				block();
				}
				break;
			case 2:
				_localctx = new IfElseIfContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(493);
				match(IF);
				setState(494);
				expression(0);
				setState(495);
				block();
				setState(496);
				match(ELSE);
				setState(497);
				ifStatement();
				}
				break;
			case 3:
				_localctx = new IfElseContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(499);
				match(IF);
				setState(500);
				expression(0);
				setState(501);
				block();
				setState(502);
				match(ELSE);
				setState(503);
				block();
				}
				break;
			case 4:
				_localctx = new IfWithInitContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(505);
				match(IF);
				setState(506);
				simpleStatement();
				setState(507);
				match(SEMICOLON);
				setState(508);
				expression(0);
				setState(509);
				block();
				}
				break;
			case 5:
				_localctx = new IfWithInitElseIfContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(511);
				match(IF);
				setState(512);
				simpleStatement();
				setState(513);
				match(SEMICOLON);
				setState(514);
				expression(0);
				setState(515);
				block();
				setState(516);
				match(ELSE);
				setState(517);
				ifStatement();
				}
				break;
			case 6:
				_localctx = new IfWithInitElseContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(519);
				match(IF);
				setState(520);
				simpleStatement();
				setState(521);
				match(SEMICOLON);
				setState(522);
				expression(0);
				setState(523);
				block();
				setState(524);
				match(ELSE);
				setState(525);
				block();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LoopContext extends ParserRuleContext {
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
	 
		public LoopContext() { }
		public void copyFrom(LoopContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class WhileLoopContext extends LoopContext {
		public TerminalNode FOR() { return getToken(MiniGOParser.FOR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileLoopContext(LoopContext ctx) { copyFrom(ctx); }
	}
	public static class InfiniteLoopContext extends LoopContext {
		public TerminalNode FOR() { return getToken(MiniGOParser.FOR, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public InfiniteLoopContext(LoopContext ctx) { copyFrom(ctx); }
	}
	public static class ForLoopNoConditionContext extends LoopContext {
		public TerminalNode FOR() { return getToken(MiniGOParser.FOR, 0); }
		public List<SimpleStatementContext> simpleStatement() {
			return getRuleContexts(SimpleStatementContext.class);
		}
		public SimpleStatementContext simpleStatement(int i) {
			return getRuleContext(SimpleStatementContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(MiniGOParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiniGOParser.SEMICOLON, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForLoopNoConditionContext(LoopContext ctx) { copyFrom(ctx); }
	}
	public static class ForLoopContext extends LoopContext {
		public TerminalNode FOR() { return getToken(MiniGOParser.FOR, 0); }
		public List<SimpleStatementContext> simpleStatement() {
			return getRuleContexts(SimpleStatementContext.class);
		}
		public SimpleStatementContext simpleStatement(int i) {
			return getRuleContext(SimpleStatementContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(MiniGOParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiniGOParser.SEMICOLON, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForLoopContext(LoopContext ctx) { copyFrom(ctx); }
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_loop);
		try {
			setState(550);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				_localctx = new InfiniteLoopContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(529);
				match(FOR);
				setState(530);
				block();
				}
				break;
			case 2:
				_localctx = new WhileLoopContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(531);
				match(FOR);
				setState(532);
				expression(0);
				setState(533);
				block();
				}
				break;
			case 3:
				_localctx = new ForLoopContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(535);
				match(FOR);
				setState(536);
				simpleStatement();
				setState(537);
				match(SEMICOLON);
				setState(538);
				expression(0);
				setState(539);
				match(SEMICOLON);
				setState(540);
				simpleStatement();
				setState(541);
				block();
				}
				break;
			case 4:
				_localctx = new ForLoopNoConditionContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(543);
				match(FOR);
				setState(544);
				simpleStatement();
				setState(545);
				match(SEMICOLON);
				setState(546);
				match(SEMICOLON);
				setState(547);
				simpleStatement();
				setState(548);
				block();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SwitchStatementContext extends ParserRuleContext {
		public SwitchStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatement; }
	 
		public SwitchStatementContext() { }
		public void copyFrom(SwitchStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class SwitchWithExprContext extends SwitchStatementContext {
		public TerminalNode SWITCH() { return getToken(MiniGOParser.SWITCH, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(MiniGOParser.LBRACE, 0); }
		public ExpressionCaseClauseListContext expressionCaseClauseList() {
			return getRuleContext(ExpressionCaseClauseListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(MiniGOParser.RBRACE, 0); }
		public SwitchWithExprContext(SwitchStatementContext ctx) { copyFrom(ctx); }
	}
	public static class SwitchEmptyContext extends SwitchStatementContext {
		public TerminalNode SWITCH() { return getToken(MiniGOParser.SWITCH, 0); }
		public TerminalNode LBRACE() { return getToken(MiniGOParser.LBRACE, 0); }
		public ExpressionCaseClauseListContext expressionCaseClauseList() {
			return getRuleContext(ExpressionCaseClauseListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(MiniGOParser.RBRACE, 0); }
		public SwitchEmptyContext(SwitchStatementContext ctx) { copyFrom(ctx); }
	}
	public static class SwitchWithInitContext extends SwitchStatementContext {
		public TerminalNode SWITCH() { return getToken(MiniGOParser.SWITCH, 0); }
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public TerminalNode LBRACE() { return getToken(MiniGOParser.LBRACE, 0); }
		public ExpressionCaseClauseListContext expressionCaseClauseList() {
			return getRuleContext(ExpressionCaseClauseListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(MiniGOParser.RBRACE, 0); }
		public SwitchWithInitContext(SwitchStatementContext ctx) { copyFrom(ctx); }
	}
	public static class SwitchWithInitAndExprContext extends SwitchStatementContext {
		public TerminalNode SWITCH() { return getToken(MiniGOParser.SWITCH, 0); }
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MiniGOParser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(MiniGOParser.LBRACE, 0); }
		public ExpressionCaseClauseListContext expressionCaseClauseList() {
			return getRuleContext(ExpressionCaseClauseListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(MiniGOParser.RBRACE, 0); }
		public SwitchWithInitAndExprContext(SwitchStatementContext ctx) { copyFrom(ctx); }
	}

	public final SwitchStatementContext switchStatement() throws RecognitionException {
		SwitchStatementContext _localctx = new SwitchStatementContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_switchStatement);
		try {
			setState(578);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				_localctx = new SwitchWithInitAndExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(552);
				match(SWITCH);
				setState(553);
				simpleStatement();
				setState(554);
				match(SEMICOLON);
				setState(555);
				expression(0);
				setState(556);
				match(LBRACE);
				setState(557);
				expressionCaseClauseList();
				setState(558);
				match(RBRACE);
				}
				break;
			case 2:
				_localctx = new SwitchWithExprContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(560);
				match(SWITCH);
				setState(561);
				expression(0);
				setState(562);
				match(LBRACE);
				setState(563);
				expressionCaseClauseList();
				setState(564);
				match(RBRACE);
				}
				break;
			case 3:
				_localctx = new SwitchWithInitContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(566);
				match(SWITCH);
				setState(567);
				simpleStatement();
				setState(568);
				match(SEMICOLON);
				setState(569);
				match(LBRACE);
				setState(570);
				expressionCaseClauseList();
				setState(571);
				match(RBRACE);
				}
				break;
			case 4:
				_localctx = new SwitchEmptyContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(573);
				match(SWITCH);
				setState(574);
				match(LBRACE);
				setState(575);
				expressionCaseClauseList();
				setState(576);
				match(RBRACE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionCaseClauseListContext extends ParserRuleContext {
		public List<ExpressionCaseClauseContext> expressionCaseClause() {
			return getRuleContexts(ExpressionCaseClauseContext.class);
		}
		public ExpressionCaseClauseContext expressionCaseClause(int i) {
			return getRuleContext(ExpressionCaseClauseContext.class,i);
		}
		public ExpressionCaseClauseListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionCaseClauseList; }
	}

	public final ExpressionCaseClauseListContext expressionCaseClauseList() throws RecognitionException {
		ExpressionCaseClauseListContext _localctx = new ExpressionCaseClauseListContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_expressionCaseClauseList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(583);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(580);
				expressionCaseClause();
				}
				}
				setState(585);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionCaseClauseContext extends ParserRuleContext {
		public ExpressionSwitchCaseContext expressionSwitchCase() {
			return getRuleContext(ExpressionSwitchCaseContext.class,0);
		}
		public TerminalNode COLON() { return getToken(MiniGOParser.COLON, 0); }
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public ExpressionCaseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionCaseClause; }
	}

	public final ExpressionCaseClauseContext expressionCaseClause() throws RecognitionException {
		ExpressionCaseClauseContext _localctx = new ExpressionCaseClauseContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_expressionCaseClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(586);
			expressionSwitchCase();
			setState(587);
			match(COLON);
			setState(588);
			statementList();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionSwitchCaseContext extends ParserRuleContext {
		public ExpressionSwitchCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionSwitchCase; }
	 
		public ExpressionSwitchCaseContext() { }
		public void copyFrom(ExpressionSwitchCaseContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class DefaultClauseContext extends ExpressionSwitchCaseContext {
		public TerminalNode DEFAULT() { return getToken(MiniGOParser.DEFAULT, 0); }
		public DefaultClauseContext(ExpressionSwitchCaseContext ctx) { copyFrom(ctx); }
	}
	public static class CaseClauseContext extends ExpressionSwitchCaseContext {
		public TerminalNode CASE() { return getToken(MiniGOParser.CASE, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public CaseClauseContext(ExpressionSwitchCaseContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionSwitchCaseContext expressionSwitchCase() throws RecognitionException {
		ExpressionSwitchCaseContext _localctx = new ExpressionSwitchCaseContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_expressionSwitchCase);
		try {
			setState(593);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				_localctx = new CaseClauseContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(590);
				match(CASE);
				setState(591);
				expressionList();
				}
				break;
			case DEFAULT:
				_localctx = new DefaultClauseContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(592);
				match(DEFAULT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 19:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 20:
			return primaryExpression_sempred((PrimaryExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 23);
		case 1:
			return precpred(_ctx, 22);
		case 2:
			return precpred(_ctx, 21);
		case 3:
			return precpred(_ctx, 20);
		case 4:
			return precpred(_ctx, 19);
		case 5:
			return precpred(_ctx, 18);
		case 6:
			return precpred(_ctx, 17);
		case 7:
			return precpred(_ctx, 16);
		case 8:
			return precpred(_ctx, 15);
		case 9:
			return precpred(_ctx, 14);
		case 10:
			return precpred(_ctx, 13);
		case 11:
			return precpred(_ctx, 12);
		case 12:
			return precpred(_ctx, 11);
		case 13:
			return precpred(_ctx, 10);
		case 14:
			return precpred(_ctx, 9);
		case 15:
			return precpred(_ctx, 8);
		case 16:
			return precpred(_ctx, 7);
		case 17:
			return precpred(_ctx, 6);
		case 18:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean primaryExpression_sempred(PrimaryExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 19:
			return precpred(_ctx, 6);
		case 20:
			return precpred(_ctx, 5);
		case 21:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K\u0256\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\3\3\3\3\3\7\3\\\n\3\f\3\16\3_\13\3\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4o\n\4\3\5\3\5\3\5\3\5\3\5\7\5v\n"+
		"\5\f\5\16\5y\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0085\n"+
		"\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u008d\n\b\f\b\16\b\u0090\13\b\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n\3"+
		"\n\3\n\3\n\7\n\u00a7\n\n\f\n\16\n\u00aa\13\n\3\13\3\13\3\13\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b7\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3"+
		"\16\3\16\3\17\3\17\3\17\5\17\u00c5\n\17\3\17\3\17\3\20\3\20\3\20\3\20"+
		"\3\20\7\20\u00ce\n\20\f\20\16\20\u00d1\13\20\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\5\22\u00db\n\22\3\22\3\22\5\22\u00df\n\22\3\23\3\23\3"+
		"\23\7\23\u00e4\n\23\f\23\16\23\u00e7\13\23\3\24\3\24\3\24\7\24\u00ec\n"+
		"\24\f\24\16\24\u00ef\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\5\25\u00fb\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\7\25\u0136\n\25\f\25\16\25\u0139\13\25\3\26"+
		"\3\26\3\26\3\26\3\26\5\26\u0140\n\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26"+
		"\u0148\n\26\f\26\16\26\u014b\13\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27"+
		"\u0153\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u015a\n\30\3\31\3\31\3\31\3"+
		"\32\3\32\3\32\3\32\3\33\3\33\5\33\u0165\n\33\3\33\3\33\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36"+
		"\3\37\3\37\3\37\3\37\3 \7 \u017f\n \f \16 \u0182\13 \3!\3!\3!\5!\u0187"+
		"\n!\3!\3!\3!\3!\3!\5!\u018e\n!\3!\3!\3!\3!\5!\u0194\n!\3!\3!\3!\3!\3!"+
		"\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01ac\n!\3\"\3"+
		"\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01b8\n\"\3#\3#\3#\3#\3#\3#\3#"+
		"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#"+
		"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01ea\n#\3$"+
		"\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$"+
		"\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0212\n$\3%\3%\3%\3%\3%"+
		"\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0229\n%\3&\3&\3&"+
		"\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&"+
		"\5&\u0245\n&\3\'\7\'\u0248\n\'\f\'\16\'\u024b\13\'\3(\3(\3(\3(\3)\3)\3"+
		")\5)\u0254\n)\3)\2\4(**\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*"+
		",.\60\62\64\668:<>@BDFHJLNP\2\3\3\2\678\2\u0292\2R\3\2\2\2\4]\3\2\2\2"+
		"\6n\3\2\2\2\bp\3\2\2\2\n\u0084\3\2\2\2\f\u0086\3\2\2\2\16\u0089\3\2\2"+
		"\2\20\u009f\3\2\2\2\22\u00a1\3\2\2\2\24\u00ab\3\2\2\2\26\u00b6\3\2\2\2"+
		"\30\u00b8\3\2\2\2\32\u00bc\3\2\2\2\34\u00c1\3\2\2\2\36\u00c8\3\2\2\2 "+
		"\u00d2\3\2\2\2\"\u00d6\3\2\2\2$\u00e0\3\2\2\2&\u00e8\3\2\2\2(\u00fa\3"+
		"\2\2\2*\u013f\3\2\2\2,\u0152\3\2\2\2.\u0159\3\2\2\2\60\u015b\3\2\2\2\62"+
		"\u015e\3\2\2\2\64\u0162\3\2\2\2\66\u0168\3\2\2\28\u016f\3\2\2\2:\u0174"+
		"\3\2\2\2<\u0179\3\2\2\2>\u0180\3\2\2\2@\u01ab\3\2\2\2B\u01b7\3\2\2\2D"+
		"\u01e9\3\2\2\2F\u0211\3\2\2\2H\u0228\3\2\2\2J\u0244\3\2\2\2L\u0249\3\2"+
		"\2\2N\u024c\3\2\2\2P\u0253\3\2\2\2RS\7\3\2\2ST\7H\2\2TU\7?\2\2UV\5\4\3"+
		"\2VW\7\2\2\3W\3\3\2\2\2X\\\5\6\4\2Y\\\5\20\t\2Z\\\5 \21\2[X\3\2\2\2[Y"+
		"\3\2\2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\5\3\2\2\2_]\3\2\2\2"+
		"`a\7\4\2\2ab\5\n\6\2bc\7?\2\2co\3\2\2\2de\7\4\2\2ef\79\2\2fg\5\b\5\2g"+
		"h\7:\2\2hi\7?\2\2io\3\2\2\2jk\7\4\2\2kl\79\2\2lm\7:\2\2mo\7?\2\2n`\3\2"+
		"\2\2nd\3\2\2\2nj\3\2\2\2o\7\3\2\2\2pq\5\n\6\2qw\7?\2\2rs\5\n\6\2st\7?"+
		"\2\2tv\3\2\2\2ur\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\t\3\2\2\2yw\3"+
		"\2\2\2z{\5\16\b\2{|\5\26\f\2|}\7*\2\2}~\5&\24\2~\u0085\3\2\2\2\177\u0080"+
		"\5\16\b\2\u0080\u0081\7*\2\2\u0081\u0082\5&\24\2\u0082\u0085\3\2\2\2\u0083"+
		"\u0085\5\f\7\2\u0084z\3\2\2\2\u0084\177\3\2\2\2\u0084\u0083\3\2\2\2\u0085"+
		"\13\3\2\2\2\u0086\u0087\5\16\b\2\u0087\u0088\5\26\f\2\u0088\r\3\2\2\2"+
		"\u0089\u008e\7H\2\2\u008a\u008b\7A\2\2\u008b\u008d\7H\2\2\u008c\u008a"+
		"\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f"+
		"\17\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7\5\2\2\u0092\u0093\5\24\13"+
		"\2\u0093\u0094\7?\2\2\u0094\u00a0\3\2\2\2\u0095\u0096\7\5\2\2\u0096\u0097"+
		"\79\2\2\u0097\u0098\5\22\n\2\u0098\u0099\7:\2\2\u0099\u009a\7?\2\2\u009a"+
		"\u00a0\3\2\2\2\u009b\u009c\7\5\2\2\u009c\u009d\79\2\2\u009d\u009e\7:\2"+
		"\2\u009e\u00a0\7?\2\2\u009f\u0091\3\2\2\2\u009f\u0095\3\2\2\2\u009f\u009b"+
		"\3\2\2\2\u00a0\21\3\2\2\2\u00a1\u00a2\5\24\13\2\u00a2\u00a8\7?\2\2\u00a3"+
		"\u00a4\5\24\13\2\u00a4\u00a5\7?\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a3\3"+
		"\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9"+
		"\23\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\7H\2\2\u00ac\u00ad\5\26\f"+
		"\2\u00ad\25\3\2\2\2\u00ae\u00af\79\2\2\u00af\u00b0\5\26\f\2\u00b0\u00b1"+
		"\7:\2\2\u00b1\u00b7\3\2\2\2\u00b2\u00b7\7H\2\2\u00b3\u00b7\5\30\r\2\u00b4"+
		"\u00b7\5\32\16\2\u00b5\u00b7\5\34\17\2\u00b6\u00ae\3\2\2\2\u00b6\u00b2"+
		"\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7"+
		"\27\3\2\2\2\u00b8\u00b9\7=\2\2\u00b9\u00ba\7>\2\2\u00ba\u00bb\5\26\f\2"+
		"\u00bb\31\3\2\2\2\u00bc\u00bd\7=\2\2\u00bd\u00be\7C\2\2\u00be\u00bf\7"+
		">\2\2\u00bf\u00c0\5\26\f\2\u00c0\33\3\2\2\2\u00c1\u00c2\7\7\2\2\u00c2"+
		"\u00c4\7;\2\2\u00c3\u00c5\5\36\20\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3"+
		"\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\7<\2\2\u00c7\35\3\2\2\2\u00c8\u00c9"+
		"\5\f\7\2\u00c9\u00cf\7?\2\2\u00ca\u00cb\5\f\7\2\u00cb\u00cc\7?\2\2\u00cc"+
		"\u00ce\3\2\2\2\u00cd\u00ca\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2"+
		"\2\2\u00cf\u00d0\3\2\2\2\u00d0\37\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3"+
		"\5\"\22\2\u00d3\u00d4\5<\37\2\u00d4\u00d5\7?\2\2\u00d5!\3\2\2\2\u00d6"+
		"\u00d7\7\6\2\2\u00d7\u00d8\7H\2\2\u00d8\u00da\79\2\2\u00d9\u00db\5$\23"+
		"\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de"+
		"\7:\2\2\u00dd\u00df\5\26\f\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df"+
		"#\3\2\2\2\u00e0\u00e5\5\f\7\2\u00e1\u00e2\7A\2\2\u00e2\u00e4\5\f\7\2\u00e3"+
		"\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2"+
		"\2\2\u00e6%\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00ed\5(\25\2\u00e9\u00ea"+
		"\7A\2\2\u00ea\u00ec\5(\25\2\u00eb\u00e9\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed"+
		"\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\'\3\2\2\2\u00ef\u00ed\3\2\2\2"+
		"\u00f0\u00f1\b\25\1\2\u00f1\u00fb\5*\26\2\u00f2\u00f3\7\26\2\2\u00f3\u00fb"+
		"\5(\25\6\u00f4\u00f5\7\27\2\2\u00f5\u00fb\5(\25\5\u00f6\u00f7\7)\2\2\u00f7"+
		"\u00fb\5(\25\4\u00f8\u00f9\7 \2\2\u00f9\u00fb\5(\25\3\u00fa\u00f0\3\2"+
		"\2\2\u00fa\u00f2\3\2\2\2\u00fa\u00f4\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fa"+
		"\u00f8\3\2\2\2\u00fb\u0137\3\2\2\2\u00fc\u00fd\f\31\2\2\u00fd\u00fe\7"+
		"\30\2\2\u00fe\u0136\5(\25\32\u00ff\u0100\f\30\2\2\u0100\u0101\7\31\2\2"+
		"\u0101\u0136\5(\25\31\u0102\u0103\f\27\2\2\u0103\u0104\7\32\2\2\u0104"+
		"\u0136\5(\25\30\u0105\u0106\f\26\2\2\u0106\u0107\7\33\2\2\u0107\u0136"+
		"\5(\25\27\u0108\u0109\f\25\2\2\u0109\u010a\7\34\2\2\u010a\u0136\5(\25"+
		"\26\u010b\u010c\f\24\2\2\u010c\u010d\7\35\2\2\u010d\u0136\5(\25\25\u010e"+
		"\u010f\f\23\2\2\u010f\u0110\7\36\2\2\u0110\u0136\5(\25\24\u0111\u0112"+
		"\f\22\2\2\u0112\u0113\7\26\2\2\u0113\u0136\5(\25\23\u0114\u0115\f\21\2"+
		"\2\u0115\u0116\7\27\2\2\u0116\u0136\5(\25\22\u0117\u0118\f\20\2\2\u0118"+
		"\u0119\7\37\2\2\u0119\u0136\5(\25\21\u011a\u011b\f\17\2\2\u011b\u011c"+
		"\7 \2\2\u011c\u0136\5(\25\20\u011d\u011e\f\16\2\2\u011e\u011f\7!\2\2\u011f"+
		"\u0136\5(\25\17\u0120\u0121\f\r\2\2\u0121\u0122\7\"\2\2\u0122\u0136\5"+
		"(\25\16\u0123\u0124\f\f\2\2\u0124\u0125\7#\2\2\u0125\u0136\5(\25\r\u0126"+
		"\u0127\f\13\2\2\u0127\u0128\7%\2\2\u0128\u0136\5(\25\f\u0129\u012a\f\n"+
		"\2\2\u012a\u012b\7$\2\2\u012b\u0136\5(\25\13\u012c\u012d\f\t\2\2\u012d"+
		"\u012e\7&\2\2\u012e\u0136\5(\25\n\u012f\u0130\f\b\2\2\u0130\u0131\7\'"+
		"\2\2\u0131\u0136\5(\25\t\u0132\u0133\f\7\2\2\u0133\u0134\7(\2\2\u0134"+
		"\u0136\5(\25\b\u0135\u00fc\3\2\2\2\u0135\u00ff\3\2\2\2\u0135\u0102\3\2"+
		"\2\2\u0135\u0105\3\2\2\2\u0135\u0108\3\2\2\2\u0135\u010b\3\2\2\2\u0135"+
		"\u010e\3\2\2\2\u0135\u0111\3\2\2\2\u0135\u0114\3\2\2\2\u0135\u0117\3\2"+
		"\2\2\u0135\u011a\3\2\2\2\u0135\u011d\3\2\2\2\u0135\u0120\3\2\2\2\u0135"+
		"\u0123\3\2\2\2\u0135\u0126\3\2\2\2\u0135\u0129\3\2\2\2\u0135\u012c\3\2"+
		"\2\2\u0135\u012f\3\2\2\2\u0135\u0132\3\2\2\2\u0136\u0139\3\2\2\2\u0137"+
		"\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138)\3\2\2\2\u0139\u0137\3\2\2\2"+
		"\u013a\u013b\b\26\1\2\u013b\u0140\5,\27\2\u013c\u0140\5\66\34\2\u013d"+
		"\u0140\58\35\2\u013e\u0140\5:\36\2\u013f\u013a\3\2\2\2\u013f\u013c\3\2"+
		"\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2\u0140\u0149\3\2\2\2\u0141"+
		"\u0142\f\b\2\2\u0142\u0148\5\60\31\2\u0143\u0144\f\7\2\2\u0144\u0148\5"+
		"\62\32\2\u0145\u0146\f\6\2\2\u0146\u0148\5\64\33\2\u0147\u0141\3\2\2\2"+
		"\u0147\u0143\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147"+
		"\3\2\2\2\u0149\u014a\3\2\2\2\u014a+\3\2\2\2\u014b\u0149\3\2\2\2\u014c"+
		"\u0153\5.\30\2\u014d\u0153\7H\2\2\u014e\u014f\79\2\2\u014f\u0150\5(\25"+
		"\2\u0150\u0151\7:\2\2\u0151\u0153\3\2\2\2\u0152\u014c\3\2\2\2\u0152\u014d"+
		"\3\2\2\2\u0152\u014e\3\2\2\2\u0153-\3\2\2\2\u0154\u015a\7C\2\2\u0155\u015a"+
		"\7D\2\2\u0156\u015a\7E\2\2\u0157\u015a\7F\2\2\u0158\u015a\7G\2\2\u0159"+
		"\u0154\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0156\3\2\2\2\u0159\u0157\3\2"+
		"\2\2\u0159\u0158\3\2\2\2\u015a/\3\2\2\2\u015b\u015c\7B\2\2\u015c\u015d"+
		"\7H\2\2\u015d\61\3\2\2\2\u015e\u015f\7=\2\2\u015f\u0160\5(\25\2\u0160"+
		"\u0161\7>\2\2\u0161\63\3\2\2\2\u0162\u0164\79\2\2\u0163\u0165\5&\24\2"+
		"\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167"+
		"\7:\2\2\u0167\65\3\2\2\2\u0168\u0169\7\23\2\2\u0169\u016a\79\2\2\u016a"+
		"\u016b\5(\25\2\u016b\u016c\7A\2\2\u016c\u016d\5(\25\2\u016d\u016e\7:\2"+
		"\2\u016e\67\3\2\2\2\u016f\u0170\7\24\2\2\u0170\u0171\79\2\2\u0171\u0172"+
		"\5(\25\2\u0172\u0173\7:\2\2\u01739\3\2\2\2\u0174\u0175\7\25\2\2\u0175"+
		"\u0176\79\2\2\u0176\u0177\5(\25\2\u0177\u0178\7:\2\2\u0178;\3\2\2\2\u0179"+
		"\u017a\7;\2\2\u017a\u017b\5> \2\u017b\u017c\7<\2\2\u017c=\3\2\2\2\u017d"+
		"\u017f\5@!\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2"+
		"\2\u0180\u0181\3\2\2\2\u0181?\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184"+
		"\7\21\2\2\u0184\u0186\79\2\2\u0185\u0187\5&\24\2\u0186\u0185\3\2\2\2\u0186"+
		"\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7:\2\2\u0189\u01ac\7?\2"+
		"\2\u018a\u018b\7\22\2\2\u018b\u018d\79\2\2\u018c\u018e\5&\24\2\u018d\u018c"+
		"\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7:\2\2\u0190"+
		"\u01ac\7?\2\2\u0191\u0193\7\16\2\2\u0192\u0194\5(\25\2\u0193\u0192\3\2"+
		"\2\2\u0193\u0194\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u01ac\7?\2\2\u0196"+
		"\u0197\7\17\2\2\u0197\u01ac\7?\2\2\u0198\u0199\7\20\2\2\u0199\u01ac\7"+
		"?\2\2\u019a\u019b\5B\"\2\u019b\u019c\7?\2\2\u019c\u01ac\3\2\2\2\u019d"+
		"\u019e\5<\37\2\u019e\u019f\7?\2\2\u019f\u01ac\3\2\2\2\u01a0\u01a1\5J&"+
		"\2\u01a1\u01a2\7?\2\2\u01a2\u01ac\3\2\2\2\u01a3\u01a4\5F$\2\u01a4\u01a5"+
		"\7?\2\2\u01a5\u01ac\3\2\2\2\u01a6\u01a7\5H%\2\u01a7\u01a8\7?\2\2\u01a8"+
		"\u01ac\3\2\2\2\u01a9\u01ac\5\20\t\2\u01aa\u01ac\5\6\4\2\u01ab\u0183\3"+
		"\2\2\2\u01ab\u018a\3\2\2\2\u01ab\u0191\3\2\2\2\u01ab\u0196\3\2\2\2\u01ab"+
		"\u0198\3\2\2\2\u01ab\u019a\3\2\2\2\u01ab\u019d\3\2\2\2\u01ab\u01a0\3\2"+
		"\2\2\u01ab\u01a3\3\2\2\2\u01ab\u01a6\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab"+
		"\u01aa\3\2\2\2\u01acA\3\2\2\2\u01ad\u01ae\5(\25\2\u01ae\u01af\t\2\2\2"+
		"\u01af\u01b8\3\2\2\2\u01b0\u01b8\5(\25\2\u01b1\u01b8\5D#\2\u01b2\u01b3"+
		"\5&\24\2\u01b3\u01b4\7+\2\2\u01b4\u01b5\5&\24\2\u01b5\u01b8\3\2\2\2\u01b6"+
		"\u01b8\3\2\2\2\u01b7\u01ad\3\2\2\2\u01b7\u01b0\3\2\2\2\u01b7\u01b1\3\2"+
		"\2\2\u01b7\u01b2\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8C\3\2\2\2\u01b9\u01ba"+
		"\5&\24\2\u01ba\u01bb\7*\2\2\u01bb\u01bc\5&\24\2\u01bc\u01ea\3\2\2\2\u01bd"+
		"\u01be\5(\25\2\u01be\u01bf\7,\2\2\u01bf\u01c0\5(\25\2\u01c0\u01ea\3\2"+
		"\2\2\u01c1\u01c2\5(\25\2\u01c2\u01c3\7-\2\2\u01c3\u01c4\5(\25\2\u01c4"+
		"\u01ea\3\2\2\2\u01c5\u01c6\5(\25\2\u01c6\u01c7\7.\2\2\u01c7\u01c8\5(\25"+
		"\2\u01c8\u01ea\3\2\2\2\u01c9\u01ca\5(\25\2\u01ca\u01cb\7/\2\2\u01cb\u01cc"+
		"\5(\25\2\u01cc\u01ea\3\2\2\2\u01cd\u01ce\5(\25\2\u01ce\u01cf\7\60\2\2"+
		"\u01cf\u01d0\5(\25\2\u01d0\u01ea\3\2\2\2\u01d1\u01d2\5(\25\2\u01d2\u01d3"+
		"\7\61\2\2\u01d3\u01d4\5(\25\2\u01d4\u01ea\3\2\2\2\u01d5\u01d6\5(\25\2"+
		"\u01d6\u01d7\7\62\2\2\u01d7\u01d8\5(\25\2\u01d8\u01ea\3\2\2\2\u01d9\u01da"+
		"\5(\25\2\u01da\u01db\7\63\2\2\u01db\u01dc\5(\25\2\u01dc\u01ea\3\2\2\2"+
		"\u01dd\u01de\5(\25\2\u01de\u01df\7\64\2\2\u01df\u01e0\5(\25\2\u01e0\u01ea"+
		"\3\2\2\2\u01e1\u01e2\5(\25\2\u01e2\u01e3\7\65\2\2\u01e3\u01e4\5(\25\2"+
		"\u01e4\u01ea\3\2\2\2\u01e5\u01e6\5(\25\2\u01e6\u01e7\7\66\2\2\u01e7\u01e8"+
		"\5(\25\2\u01e8\u01ea\3\2\2\2\u01e9\u01b9\3\2\2\2\u01e9\u01bd\3\2\2\2\u01e9"+
		"\u01c1\3\2\2\2\u01e9\u01c5\3\2\2\2\u01e9\u01c9\3\2\2\2\u01e9\u01cd\3\2"+
		"\2\2\u01e9\u01d1\3\2\2\2\u01e9\u01d5\3\2\2\2\u01e9\u01d9\3\2\2\2\u01e9"+
		"\u01dd\3\2\2\2\u01e9\u01e1\3\2\2\2\u01e9\u01e5\3\2\2\2\u01eaE\3\2\2\2"+
		"\u01eb\u01ec\7\b\2\2\u01ec\u01ed\5(\25\2\u01ed\u01ee\5<\37\2\u01ee\u0212"+
		"\3\2\2\2\u01ef\u01f0\7\b\2\2\u01f0\u01f1\5(\25\2\u01f1\u01f2\5<\37\2\u01f2"+
		"\u01f3\7\t\2\2\u01f3\u01f4\5F$\2\u01f4\u0212\3\2\2\2\u01f5\u01f6\7\b\2"+
		"\2\u01f6\u01f7\5(\25\2\u01f7\u01f8\5<\37\2\u01f8\u01f9\7\t\2\2\u01f9\u01fa"+
		"\5<\37\2\u01fa\u0212\3\2\2\2\u01fb\u01fc\7\b\2\2\u01fc\u01fd\5B\"\2\u01fd"+
		"\u01fe\7?\2\2\u01fe\u01ff\5(\25\2\u01ff\u0200\5<\37\2\u0200\u0212\3\2"+
		"\2\2\u0201\u0202\7\b\2\2\u0202\u0203\5B\"\2\u0203\u0204\7?\2\2\u0204\u0205"+
		"\5(\25\2\u0205\u0206\5<\37\2\u0206\u0207\7\t\2\2\u0207\u0208\5F$\2\u0208"+
		"\u0212\3\2\2\2\u0209\u020a\7\b\2\2\u020a\u020b\5B\"\2\u020b\u020c\7?\2"+
		"\2\u020c\u020d\5(\25\2\u020d\u020e\5<\37\2\u020e\u020f\7\t\2\2\u020f\u0210"+
		"\5<\37\2\u0210\u0212\3\2\2\2\u0211\u01eb\3\2\2\2\u0211\u01ef\3\2\2\2\u0211"+
		"\u01f5\3\2\2\2\u0211\u01fb\3\2\2\2\u0211\u0201\3\2\2\2\u0211\u0209\3\2"+
		"\2\2\u0212G\3\2\2\2\u0213\u0214\7\n\2\2\u0214\u0229\5<\37\2\u0215\u0216"+
		"\7\n\2\2\u0216\u0217\5(\25\2\u0217\u0218\5<\37\2\u0218\u0229\3\2\2\2\u0219"+
		"\u021a\7\n\2\2\u021a\u021b\5B\"\2\u021b\u021c\7?\2\2\u021c\u021d\5(\25"+
		"\2\u021d\u021e\7?\2\2\u021e\u021f\5B\"\2\u021f\u0220\5<\37\2\u0220\u0229"+
		"\3\2\2\2\u0221\u0222\7\n\2\2\u0222\u0223\5B\"\2\u0223\u0224\7?\2\2\u0224"+
		"\u0225\7?\2\2\u0225\u0226\5B\"\2\u0226\u0227\5<\37\2\u0227\u0229\3\2\2"+
		"\2\u0228\u0213\3\2\2\2\u0228\u0215\3\2\2\2\u0228\u0219\3\2\2\2\u0228\u0221"+
		"\3\2\2\2\u0229I\3\2\2\2\u022a\u022b\7\13\2\2\u022b\u022c\5B\"\2\u022c"+
		"\u022d\7?\2\2\u022d\u022e\5(\25\2\u022e\u022f\7;\2\2\u022f\u0230\5L\'"+
		"\2\u0230\u0231\7<\2\2\u0231\u0245\3\2\2\2\u0232\u0233\7\13\2\2\u0233\u0234"+
		"\5(\25\2\u0234\u0235\7;\2\2\u0235\u0236\5L\'\2\u0236\u0237\7<\2\2\u0237"+
		"\u0245\3\2\2\2\u0238\u0239\7\13\2\2\u0239\u023a\5B\"\2\u023a\u023b\7?"+
		"\2\2\u023b\u023c\7;\2\2\u023c\u023d\5L\'\2\u023d\u023e\7<\2\2\u023e\u0245"+
		"\3\2\2\2\u023f\u0240\7\13\2\2\u0240\u0241\7;\2\2\u0241\u0242\5L\'\2\u0242"+
		"\u0243\7<\2\2\u0243\u0245\3\2\2\2\u0244\u022a\3\2\2\2\u0244\u0232\3\2"+
		"\2\2\u0244\u0238\3\2\2\2\u0244\u023f\3\2\2\2\u0245K\3\2\2\2\u0246\u0248"+
		"\5N(\2\u0247\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2\u0249"+
		"\u024a\3\2\2\2\u024aM\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\5P)\2\u024d"+
		"\u024e\7@\2\2\u024e\u024f\5> \2\u024fO\3\2\2\2\u0250\u0251\7\f\2\2\u0251"+
		"\u0254\5&\24\2\u0252\u0254\7\r\2\2\u0253\u0250\3\2\2\2\u0253\u0252\3\2"+
		"\2\2\u0254Q\3\2\2\2&[]nw\u0084\u008e\u009f\u00a8\u00b6\u00c4\u00cf\u00da"+
		"\u00de\u00e5\u00ed\u00fa\u0135\u0137\u013f\u0147\u0149\u0152\u0159\u0164"+
		"\u0180\u0186\u018d\u0193\u01ab\u01b7\u01e9\u0211\u0228\u0244\u0249\u0253";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}