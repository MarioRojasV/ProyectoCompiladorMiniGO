grammar MiniGO;

// ═══════════════════════════════ PARSER RULES ═══════════════════════════════

// Regla principal
root: PACKAGE IDENTIFIER SEMICOLON topDeclarationList EOF;

// Declaraciones a nivel global
topDeclarationList: ( variableDecl | typeDecl | funcDecl)*;

// Declaración de variables
variableDecl:
	VAR singleVarDecl SEMICOLON
	| VAR LPAREN innerVarDecls RPAREN SEMICOLON
	| VAR LPAREN RPAREN SEMICOLON;

innerVarDecls:
	singleVarDecl SEMICOLON (singleVarDecl SEMICOLON)*;

singleVarDecl
    : identifierList declType ASSIGN expressionList   #varDeclWithTypeAndValue
    | identifierList ASSIGN expressionList             #varDeclWithValue
    | singleVarDeclNoExps                              #varDeclNoExps
    ;

singleVarDeclNoExps: identifierList declType;

identifierList: IDENTIFIER ( COMMA IDENTIFIER)*;

// Declaración de tipos
typeDecl:
	TYPE singleTypeDecl SEMICOLON
	| TYPE LPAREN innerTypeDecls RPAREN SEMICOLON
	| TYPE LPAREN RPAREN SEMICOLON;

innerTypeDecls:
	singleTypeDecl SEMICOLON (singleTypeDecl SEMICOLON)*;

singleTypeDecl: IDENTIFIER declType;

// Tipos posibles
declType
    : LPAREN declType RPAREN   #groupedType
    | IDENTIFIER               #simpleType
    | sliceDeclType            #sliceType
    | arrayDeclType            #arrayType
    | structDeclType           #structType
    ;

sliceDeclType: LBRACKET RBRACKET declType;

arrayDeclType: LBRACKET INTLITERAL RBRACKET declType;

structDeclType: STRUCT LBRACE structMemDecls? RBRACE;

structMemDecls:
	singleVarDeclNoExps SEMICOLON (singleVarDeclNoExps SEMICOLON)*;

// Declaración de funciones
funcDecl: funcFrontDecl block SEMICOLON;

funcFrontDecl:
	FUNC IDENTIFIER LPAREN funcArgDecls? RPAREN declType?;

funcArgDecls: singleVarDeclNoExps ( COMMA singleVarDeclNoExps)*;

// ═══════════════════════════════ EXPRESIONES ═══════════════════════════════

expressionList: expression ( COMMA expression)*;

expression
    : primaryExpression                         #primaryExpr
    | expression MULT expression                #multExpr
    | expression DIV expression                 #divExpr
    | expression MOD expression                 #modExpr
    | expression LSHIFT expression              #lshiftExpr
    | expression RSHIFT expression              #rshiftExpr
    | expression AMP expression                 #ampExpr
    | expression AMPXOR expression              #ampxorExpr
    | expression PLUS expression                #addExpr
    | expression MINUS expression               #subExpr
    | expression PIPE expression                #pipeExpr
    | expression XOR expression                 #xorExpr
    | expression EQ expression                  #eqExpr
    | expression NEQ expression                 #neqExpr
    | expression LT expression                  #ltExpr
    | expression LEQ expression                 #leqExpr
    | expression GT expression                  #gtExpr
    | expression GEQ expression                 #geqExpr
    | expression AND expression                 #andExpr
    | expression OR expression                  #orExpr
    | PLUS expression                           #unaryPlusExpr
    | MINUS expression                          #unaryMinusExpr
    | NOT expression                            #notExpr
    | XOR expression                            #xorUnaryExpr
    ;

primaryExpression
    : operand                                   #operandExpr
    | primaryExpression selector                #selectorExpr
    | primaryExpression index                   #indexExpr
    | primaryExpression arguments               #callExpr
    | appendExpression                          #appendExpr
    | lengthExpression                          #lengthExpr
    | capExpression                             #capExpr
    ;

operand
    : literal                                   #literalOperand
    | IDENTIFIER                                #identifierOperand
    | LPAREN expression RPAREN                  #groupedExpr
    ;

literal
    : INTLITERAL                                #intLit
    | FLOATLITERAL                              #floatLit
    | RUNELITERAL                               #runeLit
    | RAWSTRINGLITERAL                          #rawStringLit
    | INTERPRETEDSTRINGLITERAL                  #interpretedStringLit
    ;

selector: DOT IDENTIFIER;

index: LBRACKET expression RBRACKET;

arguments: LPAREN expressionList? RPAREN;

appendExpression:
	APPEND LPAREN expression COMMA expression RPAREN;

lengthExpression: LEN LPAREN expression RPAREN;

capExpression: CAP LPAREN expression RPAREN;

// ═══════════════════════════════ STATEMENTS ═══════════════════════════════

block: LBRACE statementList RBRACE;

statementList: statement*;

statement
    : PRINT LPAREN expressionList? RPAREN SEMICOLON    #printStatement
    | PRINTLN LPAREN expressionList? RPAREN SEMICOLON  #printlnStatement
    | RETURN expression? SEMICOLON                     #returnStatement
    | BREAK SEMICOLON                                  #breakStatement
    | CONTINUE SEMICOLON                               #continueStatement
    | simpleStatement SEMICOLON                        #simpleStmt
    | block SEMICOLON                                  #blockStatement
    | switchStatement SEMICOLON                        #switchStmt
    | ifStatement SEMICOLON                            #ifStmt
    | loop SEMICOLON                                   #loopStmt
    | typeDecl                                         #typeDeclStatement
    | variableDecl                                     #varDeclStatement
    ;

simpleStatement
    : expression ( INC | DEC )   #incDecStatement
    | expression                  #expressionStatement
    | assignmentStatement         #assignStmt
    | expressionList DECLARE_ASSIGN expressionList  #shortVarDecl
    |                             #emptyStatement
    ;

assignmentStatement
    : expressionList ASSIGN expressionList      #simpleAssign
    | expression PLUS_ASSIGN expression         #plusAssign
    | expression MINUS_ASSIGN expression        #minusAssign
    | expression MULT_ASSIGN expression         #multAssign
    | expression DIV_ASSIGN expression          #divAssign
    | expression MOD_ASSIGN expression          #modAssign
    | expression AMP_ASSIGN expression          #ampAssign
    | expression PIPE_ASSIGN expression         #pipeAssign
    | expression XOR_ASSIGN expression          #xorAssign
    | expression LSHIFT_ASSIGN expression       #lshiftAssign
    | expression RSHIFT_ASSIGN expression       #rshiftAssign
    | expression AMPXOR_ASSIGN expression       #ampxorAssign
    ;

ifStatement
    : IF expression block                                          #simpleIf
    | IF expression block ELSE ifStatement                         #ifElseIf
    | IF expression block ELSE block                               #ifElse
    | IF simpleStatement SEMICOLON expression block                #ifWithInit
    | IF simpleStatement SEMICOLON expression block ELSE ifStatement #ifWithInitElseIf
    | IF simpleStatement SEMICOLON expression block ELSE block     #ifWithInitElse
    ;

loop
    : FOR block                                                           #infiniteLoop
    | FOR expression block                                                #whileLoop
    | FOR simpleStatement SEMICOLON expression SEMICOLON simpleStatement block #forLoop
    | FOR simpleStatement SEMICOLON SEMICOLON simpleStatement block       #forLoopNoCondition
    ;

switchStatement
    : SWITCH simpleStatement SEMICOLON expression LBRACE expressionCaseClauseList RBRACE  #switchWithInitAndExpr
    | SWITCH expression LBRACE expressionCaseClauseList RBRACE                            #switchWithExpr
    | SWITCH simpleStatement SEMICOLON LBRACE expressionCaseClauseList RBRACE             #switchWithInit
    | SWITCH LBRACE expressionCaseClauseList RBRACE                                       #switchEmpty
    ;

expressionCaseClauseList: expressionCaseClause*;

expressionCaseClause: expressionSwitchCase COLON statementList;

expressionSwitchCase
    : CASE expressionList   #caseClause
    | DEFAULT               #defaultClause
    ;

// ═══════════════════════════════ LEXER RULES ═══════════════════════════════

// Palabras reservadas
PACKAGE: 'package';
VAR: 'var';
TYPE: 'type';
FUNC: 'func';
STRUCT: 'struct';
IF: 'if';
ELSE: 'else';
FOR: 'for';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
PRINT: 'print';
PRINTLN: 'println';
APPEND: 'append';
LEN: 'len';
CAP: 'cap';

// Operadores aritméticos
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
LSHIFT: '<<';
RSHIFT: '>>';
AMP: '&';
AMPXOR: '&^';
PIPE: '|';
XOR: '^';

// Operadores de comparación
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';

// Operadores lógicos
AND: '&&';
OR: '||';
NOT: '!';

// Asignación simple
ASSIGN: '=';
DECLARE_ASSIGN: ':=';

// Asignación compuesta
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULT_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
AMP_ASSIGN: '&=';
PIPE_ASSIGN: '|=';
XOR_ASSIGN: '^=';
LSHIFT_ASSIGN: '<<=';
RSHIFT_ASSIGN: '>>=';
AMPXOR_ASSIGN: '&^=';

// Incremento / Decremento
INC: '++';
DEC: '--';

// Puntuación y delimitadores
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
SEMICOLON: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

// ═══════════════════════════════ LITERALES ═══════════════════════════════

// Enteros
INTLITERAL: [0-9]+;

// Flotantes
FLOATLITERAL: [0-9]+ '.' [0-9]* | '.' [0-9]+;

// Rune literal: carácter entre comillas simples, ej: 'a', '\n'
RUNELITERAL: '\'' (~['\\\r\n] | '\\' .) '\'';

// Raw string: entre backticks, puede tener cualquier cosa menos backtick
RAWSTRINGLITERAL: '`' ~[`]* '`';

// Interpreted string: entre comillas dobles, soporta escapes
INTERPRETEDSTRINGLITERAL: '"' (~["\\\r\n] | '\\' .)* '"';

// Identificadores
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// ═══════════════════════════════ IGNORAR ═══════════════════════════════

WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;