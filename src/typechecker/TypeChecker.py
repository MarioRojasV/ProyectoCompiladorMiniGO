from antlr4 import ParserRuleContext
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generated.MiniGOParser import MiniGOParser
from generated.MiniGOVisitor import MiniGOVisitor
from typechecker.TablaSimbolos import TablaSimbolos
from typechecker.Decoraciones import Decoraciones

# Constantes de tipos — usamos strings en vez de ints
# porque MiniGO tiene tipos más complejos que Alpha
INT      = "int"
FLOAT64  = "float64"
STRING   = "string"
BOOL     = "bool"
RUNE     = "rune"
VOID     = "void"

def arrayType(size, elemType):
    return ("array", size, elemType)

def sliceType(elemType):
    return ("slice", elemType)

def structType(name):
    return ("struct", name)

class TypeCheckerException(Exception):
    pass

class MiniGOTypeChecker(MiniGOVisitor):

    def __init__(self, decoraciones: Decoraciones):
        self.errorList = []
        self.symbolTable = TablaSimbolos()
        self.decoraciones = decoraciones
        self.currentFuncReturnType = None  # None = fuera de función

    def hasErrors(self):
        return len(self.errorList) > 0

    def getErrorList(self):
        return self.errorList

    def reportError(self, msg, token):
        self.errorList.append(
            f"TYPE ERROR: {msg} \"{token.text}\""
            f" (line: {token.line}, column: {token.column + 1})"
        )

    def reportErrorWithTypes(self, msg, token, expected, actual):
        self.errorList.append(
            f"TYPE ERROR: {msg} \"{token.text}\""
            f" expected: {expected}"
            f" but got: {actual}"
            f" (line: {token.line}, column: {token.column + 1})"
        )

    def resolverTipo(self, ctx):
        if isinstance(ctx, MiniGOParser.SimpleTypeContext):
            nombre = ctx.IDENTIFIER().getText()
            # Si es un tipo primitivo, retornarlo directo
            if nombre in (INT, FLOAT64, STRING, BOOL, RUNE):
                return nombre
            # Si no, buscar en la tabla de símbolos si es un struct
            ident = self.symbolTable.buscar(nombre)
            if ident is not None and isinstance(ident, TablaSimbolos.StructIdent):
                return structType(nombre)
            # Si no es struct, retornar el nombre igual (puede ser un tipo alias)
            return nombre
        elif isinstance(ctx, MiniGOParser.ArrayTypeContext):
            size = int(ctx.arrayDeclType().INTLITERAL().getText())
            elemType = self.resolverTipo(ctx.arrayDeclType().declType())
            return arrayType(size, elemType)
        elif isinstance(ctx, MiniGOParser.SliceTypeContext):
            elemType = self.resolverTipo(ctx.sliceDeclType().declType())
            return sliceType(elemType)
        elif isinstance(ctx, MiniGOParser.StructTypeContext):
            return "struct_anon"
        elif isinstance(ctx, MiniGOParser.GroupedTypeContext):
            return self.resolverTipo(ctx.declType())
        return None
    
    # ═══════════════════════════════
    #  REGLA RAÍZ Y DECLARACIONES
    # ═══════════════════════════════

    def visitRoot(self, ctx: MiniGOParser.RootContext):
        self.symbolTable.openScope()
        self.visitChildren(ctx)
        self.symbolTable.closeScope()
        return None

    def visitVariableDecl(self, ctx: MiniGOParser.VariableDeclContext):
        self.visitChildren(ctx)
        return None

    def visitInnerVarDecls(self, ctx: MiniGOParser.InnerVarDeclsContext):
        self.visitChildren(ctx)
        return None

    def visitVarDeclWithTypeAndValue(self, ctx: MiniGOParser.VarDeclWithTypeAndValueContext):
        try:
            tipo = self.resolverTipo(ctx.declType())
            exprTypes = self.visit(ctx.expressionList())

            for exprType in exprTypes:
                if tipo != exprType:
                    self.reportErrorWithTypes(
                        "Incompatible types in variable declaration!",
                        ctx.declType().start, tipo, exprType
                    )

            for idNode in ctx.identifierList().IDENTIFIER():
                existing = self.symbolTable.buscarNivelActual(idNode.getText())
                if existing is None:
                    self.symbolTable.insertarVar(idNode.getSymbol(), tipo, ctx)
                else:
                    self.reportError("Variable already declared!", idNode.getSymbol())

        except TypeCheckerException:
            pass
        return None

    def visitVarDeclWithValue(self, ctx: MiniGOParser.VarDeclWithValueContext):
        try:
            exprTypes = self.visit(ctx.expressionList())
            ids = ctx.identifierList().IDENTIFIER()

            for i, idNode in enumerate(ids):
                tipo = exprTypes[i] if i < len(exprTypes) else None
                existing = self.symbolTable.buscarNivelActual(idNode.getText())
                if existing is None:
                    self.symbolTable.insertarVar(idNode.getSymbol(), tipo, ctx)
                else:
                    self.reportError("Variable already declared!", idNode.getSymbol())

        except TypeCheckerException:
            pass
        return None

    def visitVarDeclNoExps(self, ctx: MiniGOParser.VarDeclNoExpsContext):
        self.visit(ctx.singleVarDeclNoExps())
        return None

    def visitSingleVarDeclNoExps(self, ctx: MiniGOParser.SingleVarDeclNoExpsContext):
        tipo = self.resolverTipo(ctx.declType())
        for idNode in ctx.identifierList().IDENTIFIER():
            existing = self.symbolTable.buscarNivelActual(idNode.getText())
            if existing is None:
                self.symbolTable.insertarVar(idNode.getSymbol(), tipo, ctx)
            else:
                self.reportError("Variable already declared!", idNode.getSymbol())
        return tipo

    # ═══════════════════════════════
    #  TYPE DECLARATIONS (structs)
    # ═══════════════════════════════

    def visitTypeDecl(self, ctx: MiniGOParser.TypeDeclContext):
        self.visitChildren(ctx)
        return None

    def visitSingleTypeDecl(self, ctx: MiniGOParser.SingleTypeDeclContext):
        nombre = ctx.IDENTIFIER().getText()
        token = ctx.IDENTIFIER().getSymbol()
        if isinstance(ctx.declType(), MiniGOParser.StructTypeContext):
            campos = {}
            structCtx = ctx.declType().structDeclType()  # ← bajar un nivel
            if structCtx.structMemDecls() is not None:
                for miembro in structCtx.structMemDecls().singleVarDeclNoExps():
                    tipoMiembro = self.resolverTipo(miembro.declType())
                    for idNode in miembro.identifierList().IDENTIFIER():
                        campos[idNode.getText()] = tipoMiembro
            existing = self.symbolTable.buscarNivelActual(nombre)
            if existing is None:
                self.symbolTable.insertarStruct(token, campos, ctx)
            else:
                self.reportError("Type already declared!", token)
        else:
            tipo = self.resolverTipo(ctx.declType())
            existing = self.symbolTable.buscarNivelActual(nombre)
            if existing is None:
                self.symbolTable.insertarVar(token, tipo, ctx)
            else:
                self.reportError("Type already declared!", token)
        return None

    # ═══════════════════════════════
    #  FUNCTION DECLARATIONS
    # ═══════════════════════════════

    def visitFuncDecl(self, ctx: MiniGOParser.FuncDeclContext):
        front = ctx.funcFrontDecl()
        nombre = front.IDENTIFIER().getText()
        token = front.IDENTIFIER().getSymbol()

        # Resolver tipo de retorno
        if front.declType() is not None:
            returnType = self.resolverTipo(front.declType())
        else:
            returnType = VOID

        # Resolver parámetros
        params = []
        if front.funcArgDecls() is not None:
            for argDecl in front.funcArgDecls().singleVarDeclNoExps():
                tipoParam = self.resolverTipo(argDecl.declType())
                for _ in argDecl.identifierList().IDENTIFIER():
                    params.append(tipoParam)

        # Insertar función en tabla de símbolos
        existing = self.symbolTable.buscarNivelActual(nombre)
        if existing is None:
            self.symbolTable.insertarMethod(token, returnType, params, ctx)
        else:
            self.reportError("Function already declared!", token)

        # Abrir scope e insertar parámetros
        self.symbolTable.openScope()
        if front.funcArgDecls() is not None:
            for argDecl in front.funcArgDecls().singleVarDeclNoExps():
                tipoParam = self.resolverTipo(argDecl.declType())
                for idNode in argDecl.identifierList().IDENTIFIER():
                    self.symbolTable.insertarVar(idNode.getSymbol(), tipoParam, argDecl)

        # Guardar return type anterior y entrar a la función
        prevReturnType = self.currentFuncReturnType
        self.currentFuncReturnType = returnType

        self.visit(ctx.block())

        # Restaurar estado anterior
        self.currentFuncReturnType = prevReturnType
        self.symbolTable.closeScope()
        return None

        # ═══════════════════════════════
    #  STATEMENTS
    # ═══════════════════════════════

    def visitBlockStatement(self, ctx: MiniGOParser.BlockStatementContext):
        self.symbolTable.openScope()
        self.visitChildren(ctx)
        self.symbolTable.closeScope()
        return None

    def visitReturnStatement(self, ctx: MiniGOParser.ReturnStatementContext):
        if self.currentFuncReturnType is None:
            self.reportError("'return' outside of a function!", ctx.RETURN().getSymbol())
            return None

        if ctx.expression() is not None:
            try:
                exprType = self.visit(ctx.expression())
                if self.currentFuncReturnType == VOID:
                    self.reportError("Cannot return a value from a void function!", ctx.RETURN().getSymbol())
                elif exprType != self.currentFuncReturnType:
                    self.reportErrorWithTypes(
                        "Incompatible return type!",
                        ctx.RETURN().getSymbol(),
                        self.currentFuncReturnType,
                        exprType
                    )
            except TypeCheckerException:
                pass
        else:
            if self.currentFuncReturnType != VOID:
                self.reportError("Non-void function must return a value!", ctx.RETURN().getSymbol())
        return None

    def visitPrintStatement(self, ctx: MiniGOParser.PrintStatementContext):
        if ctx.expressionList() is not None:
            self.visit(ctx.expressionList())
        return None

    def visitPrintlnStatement(self, ctx: MiniGOParser.PrintlnStatementContext):
        if ctx.expressionList() is not None:
            self.visit(ctx.expressionList())
        return None

    def visitBreakStatement(self, ctx: MiniGOParser.BreakStatementContext):
        return None

    def visitContinueStatement(self, ctx: MiniGOParser.ContinueStatementContext):
        return None

    def visitVarDeclStatement(self, ctx: MiniGOParser.VarDeclStatementContext):
        self.visit(ctx.variableDecl())
        return None

    def visitTypeDeclStatement(self, ctx: MiniGOParser.TypeDeclStatementContext):
        self.visit(ctx.typeDecl())
        return None

    # ═══════════════════════════════
    #  SIMPLE STATEMENTS
    # ═══════════════════════════════

    def visitEmptyStatement(self, ctx: MiniGOParser.EmptyStatementContext):
        return None

    def visitIncDecStatement(self, ctx: MiniGOParser.IncDecStatementContext):
        try:
            exprType = self.visit(ctx.expression())
            if exprType != INT:
                self.reportError("'++/--' only applicable to int!", ctx.expression().start)
        except TypeCheckerException:
            pass
        return None

    def visitShortVarDecl(self, ctx: MiniGOParser.ShortVarDeclContext):
        try:
            exprTypes = self.visit(ctx.expressionList(1))
            ids = ctx.expressionList(0).expression()

            for i, exprCtx in enumerate(ids):
                tipo = exprTypes[i] if i < len(exprTypes) else None
                # El lado izquierdo debe ser un identificador
                idText = exprCtx.getText()
                existing = self.symbolTable.buscarNivelActual(idText)
                if existing is None:
                    self.symbolTable.insertarVar(exprCtx.start, tipo, ctx)
                else:
                    self.reportError("Variable already declared!", exprCtx.start)
        except TypeCheckerException:
            pass
        return None

    def visitExpressionStatement(self, ctx: MiniGOParser.ExpressionStatementContext):
        try:
            self.visit(ctx.expression())
        except TypeCheckerException:
            pass
        return None

    # ═══════════════════════════════
    #  ASSIGNMENT
    # ═══════════════════════════════

    def visitSimpleAssign(self, ctx: MiniGOParser.SimpleAssignContext):
        try:
            rightTypes = self.visit(ctx.expressionList(1))
            leftTypes = self.visit(ctx.expressionList(0))

            for i in range(len(leftTypes)):
                if i < len(rightTypes):
                    if leftTypes[i] != rightTypes[i]:
                        self.reportErrorWithTypes(
                            "Incompatible types in assignment!",
                            ctx.start, leftTypes[i], rightTypes[i]
                        )
        except TypeCheckerException:
            pass
        return None

    def visitPlusAssign(self, ctx: MiniGOParser.PlusAssignContext):
        self._checkCompoundAssign(ctx, "+=" )
        return None

    def visitMinusAssign(self, ctx: MiniGOParser.MinusAssignContext):
        self._checkCompoundAssign(ctx, "-=")
        return None

    def visitMultAssign(self, ctx: MiniGOParser.MultAssignContext):
        self._checkCompoundAssign(ctx, "*=")
        return None

    def visitDivAssign(self, ctx: MiniGOParser.DivAssignContext):
        self._checkCompoundAssign(ctx, "/=")
        return None

    def visitModAssign(self, ctx: MiniGOParser.ModAssignContext):
        self._checkCompoundAssign(ctx, "%=")
        return None

    def visitAmpAssign(self, ctx: MiniGOParser.AmpAssignContext):
        self._checkCompoundAssign(ctx, "&=")
        return None

    def visitPipeAssign(self, ctx: MiniGOParser.PipeAssignContext):
        self._checkCompoundAssign(ctx, "|=")
        return None

    def visitXorAssign(self, ctx: MiniGOParser.XorAssignContext):
        self._checkCompoundAssign(ctx, "^=")
        return None

    def visitLshiftAssign(self, ctx: MiniGOParser.LshiftAssignContext):
        self._checkCompoundAssign(ctx, "<<=")
        return None

    def visitRshiftAssign(self, ctx: MiniGOParser.RshiftAssignContext):
        self._checkCompoundAssign(ctx, ">>=")
        return None

    def visitAmpxorAssign(self, ctx: MiniGOParser.AmpxorAssignContext):
        self._checkCompoundAssign(ctx, "&^=")
        return None

    def _checkCompoundAssign(self, ctx, op):
        """Verifica asignaciones compuestas como +=, -=, etc."""
        try:
            leftType = self.visit(ctx.expression(0))
            rightType = self.visit(ctx.expression(1))
            if leftType != rightType:
                self.reportErrorWithTypes(
                    f"Incompatible types in '{op}' assignment!",
                    ctx.start, leftType, rightType
                )
        except TypeCheckerException:
            pass

    # ═══════════════════════════════
    #  CONTROL FLOW
    # ═══════════════════════════════

    def visitSimpleIf(self, ctx: MiniGOParser.SimpleIfContext):
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'if' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.symbolTable.openScope()
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        return None

    def visitIfElse(self, ctx: MiniGOParser.IfElseContext):
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'if' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.symbolTable.openScope()
        self.visit(ctx.block(0))
        self.symbolTable.closeScope()
        self.symbolTable.openScope()
        self.visit(ctx.block(1))
        self.symbolTable.closeScope()
        return None

    def visitIfElseIf(self, ctx: MiniGOParser.IfElseIfContext):
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'if' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.symbolTable.openScope()
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        self.visit(ctx.ifStatement())
        return None

    def visitIfWithInit(self, ctx: MiniGOParser.IfWithInitContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement())
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'if' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        return None

    def visitIfWithInitElse(self, ctx: MiniGOParser.IfWithInitElseContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement())
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'if' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.visit(ctx.block(0))
        self.symbolTable.closeScope()
        self.symbolTable.openScope()
        self.visit(ctx.block(1))
        self.symbolTable.closeScope()
        return None

    def visitIfWithInitElseIf(self, ctx: MiniGOParser.IfWithInitElseIfContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement())
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'if' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        self.visit(ctx.ifStatement())
        return None

    def visitInfiniteLoop(self, ctx: MiniGOParser.InfiniteLoopContext):
        self.symbolTable.openScope()
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        return None

    def visitWhileLoop(self, ctx: MiniGOParser.WhileLoopContext):
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'for' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.symbolTable.openScope()
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        return None

    def visitForLoop(self, ctx: MiniGOParser.ForLoopContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement(0))
        try:
            condType = self.visit(ctx.expression())
            if condType != BOOL:
                self.reportError("Condition in 'for' must be bool!", ctx.expression().start)
        except TypeCheckerException:
            pass
        self.visit(ctx.simpleStatement(1))
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        return None

    def visitForLoopNoCondition(self, ctx: MiniGOParser.ForLoopNoConditionContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement(0))
        self.visit(ctx.simpleStatement(1))
        self.visit(ctx.block())
        self.symbolTable.closeScope()
        return None

    # ═══════════════════════════════
    #  SWITCH
    # ═══════════════════════════════

    def visitSwitchWithExpr(self, ctx: MiniGOParser.SwitchWithExprContext):
        try:
            self.visit(ctx.expression())
        except TypeCheckerException:
            pass
        self.visit(ctx.expressionCaseClauseList())
        return None

    def visitSwitchWithInitAndExpr(self, ctx: MiniGOParser.SwitchWithInitAndExprContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement())
        try:
            self.visit(ctx.expression())
        except TypeCheckerException:
            pass
        self.visit(ctx.expressionCaseClauseList())
        self.symbolTable.closeScope()
        return None

    def visitSwitchWithInit(self, ctx: MiniGOParser.SwitchWithInitContext):
        self.symbolTable.openScope()
        self.visit(ctx.simpleStatement())
        self.visit(ctx.expressionCaseClauseList())
        self.symbolTable.closeScope()
        return None

    def visitSwitchEmpty(self, ctx: MiniGOParser.SwitchEmptyContext):
        self.visit(ctx.expressionCaseClauseList())
        return None

    def visitExpressionCaseClause(self, ctx: MiniGOParser.ExpressionCaseClauseContext):
        self.symbolTable.openScope()
        self.visit(ctx.expressionSwitchCase())
        self.visit(ctx.statementList())
        self.symbolTable.closeScope()
        return None

    def visitCaseClause(self, ctx: MiniGOParser.CaseClauseContext):
        try:
            self.visit(ctx.expressionList())
        except TypeCheckerException:
            pass
        return None

    def visitDefaultClause(self, ctx: MiniGOParser.DefaultClauseContext):
        return None
    
    # ═══════════════════════════════
    #  EXPRESIONES
    # ═══════════════════════════════

    def visitExpressionList(self, ctx: MiniGOParser.ExpressionListContext):
        tipos = []
        for exprCtx in ctx.expression():
            try:
                tipo = self.visit(exprCtx)
                tipos.append(tipo)
            except TypeCheckerException:
                tipos.append(None)
        return tipos

    # Expresiones binarias
    def visitAddExpr(self, ctx: MiniGOParser.AddExprContext):
        return self._checkBinaryNumericOrString(ctx, "+")

    def visitSubExpr(self, ctx: MiniGOParser.SubExprContext):
        return self._checkBinaryNumeric(ctx, "-")

    def visitMultExpr(self, ctx: MiniGOParser.MultExprContext):
        return self._checkBinaryNumeric(ctx, "*")

    def visitDivExpr(self, ctx: MiniGOParser.DivExprContext):
        return self._checkBinaryNumeric(ctx, "/")

    def visitModExpr(self, ctx: MiniGOParser.ModExprContext):
        return self._checkBinaryInt(ctx, "%")

    def visitLshiftExpr(self, ctx: MiniGOParser.LshiftExprContext):
        return self._checkBinaryInt(ctx, "<<")

    def visitRshiftExpr(self, ctx: MiniGOParser.RshiftExprContext):
        return self._checkBinaryInt(ctx, ">>")

    def visitAmpExpr(self, ctx: MiniGOParser.AmpExprContext):
        return self._checkBinaryInt(ctx, "&")

    def visitAmpxorExpr(self, ctx: MiniGOParser.AmpxorExprContext):
        return self._checkBinaryInt(ctx, "&^")

    def visitPipeExpr(self, ctx: MiniGOParser.PipeExprContext):
        return self._checkBinaryInt(ctx, "|")

    def visitXorExpr(self, ctx: MiniGOParser.XorExprContext):
        return self._checkBinaryInt(ctx, "^")

    def visitEqExpr(self, ctx: MiniGOParser.EqExprContext):
        return self._checkComparison(ctx, "==")

    def visitNeqExpr(self, ctx: MiniGOParser.NeqExprContext):
        return self._checkComparison(ctx, "!=")

    def visitLtExpr(self, ctx: MiniGOParser.LtExprContext):
        return self._checkOrderedComparison(ctx, "<")

    def visitLeqExpr(self, ctx: MiniGOParser.LeqExprContext):
        return self._checkOrderedComparison(ctx, "<=")

    def visitGtExpr(self, ctx: MiniGOParser.GtExprContext):
        return self._checkOrderedComparison(ctx, ">")

    def visitGeqExpr(self, ctx: MiniGOParser.GeqExprContext):
        return self._checkOrderedComparison(ctx, ">=")

    def visitAndExpr(self, ctx: MiniGOParser.AndExprContext):
        return self._checkBinaryBool(ctx, "&&")

    def visitOrExpr(self, ctx: MiniGOParser.OrExprContext):
        return self._checkBinaryBool(ctx, "||")

    # Expresiones unarias
    def visitUnaryPlusExpr(self, ctx: MiniGOParser.UnaryPlusExprContext):
        try:
            exprType = self.visit(ctx.expression())
            if exprType not in (INT, FLOAT64):
                self.reportError("Unary '+' only applicable to numeric types!", ctx.expression().start)
                raise TypeCheckerException()
            return exprType
        except TypeCheckerException:
            raise

    def visitUnaryMinusExpr(self, ctx: MiniGOParser.UnaryMinusExprContext):
        try:
            exprType = self.visit(ctx.expression())
            if exprType not in (INT, FLOAT64):
                self.reportError("Unary '-' only applicable to numeric types!", ctx.expression().start)
                raise TypeCheckerException()
            return exprType
        except TypeCheckerException:
            raise

    def visitNotExpr(self, ctx: MiniGOParser.NotExprContext):
        try:
            exprType = self.visit(ctx.expression())
            if exprType != BOOL:
                self.reportError("'!' only applicable to bool!", ctx.expression().start)
                raise TypeCheckerException()
            return BOOL
        except TypeCheckerException:
            raise

    def visitXorUnaryExpr(self, ctx: MiniGOParser.XorUnaryExprContext):
        try:
            exprType = self.visit(ctx.expression())
            if exprType != INT:
                self.reportError("'^' only applicable to int!", ctx.expression().start)
                raise TypeCheckerException()
            return INT
        except TypeCheckerException:
            raise

    # ═══════════════════════════════
    #  HELPERS PARA EXPRESIONES
    # ═══════════════════════════════

    def _checkBinaryNumeric(self, ctx, op):
        try:
            t1 = self.visit(ctx.expression(0))
            t2 = self.visit(ctx.expression(1))
            if t1 in (INT, FLOAT64) and t1 == t2:
                self.decoraciones.setTipo(ctx, t1)
                return t1
            self.reportErrorWithTypes(f"Incompatible types for '{op}'!", ctx.start, t1, t2)
            raise TypeCheckerException()
        except TypeCheckerException:
            raise

    def _checkBinaryNumericOrString(self, ctx, op):
        try:
            t1 = self.visit(ctx.expression(0))
            t2 = self.visit(ctx.expression(1))
            if t1 == t2 and t1 in (INT, FLOAT64, STRING):
                self.decoraciones.setTipo(ctx, t1)
                return t1
            self.reportErrorWithTypes(f"Incompatible types for '{op}'!", ctx.start, t1, t2)
            raise TypeCheckerException()
        except TypeCheckerException:
            raise

    def _checkBinaryInt(self, ctx, op):
        try:
            t1 = self.visit(ctx.expression(0))
            t2 = self.visit(ctx.expression(1))
            if t1 == INT and t2 == INT:
                self.decoraciones.setTipo(ctx, INT)
                return INT
            self.reportErrorWithTypes(f"Incompatible types for '{op}'!", ctx.start, t1, t2)
            raise TypeCheckerException()
        except TypeCheckerException:
            raise

    def _checkBinaryBool(self, ctx, op):
        try:
            t1 = self.visit(ctx.expression(0))
            t2 = self.visit(ctx.expression(1))
            if t1 == BOOL and t2 == BOOL:
                self.decoraciones.setTipo(ctx, BOOL)
                return BOOL
            self.reportErrorWithTypes(f"Incompatible types for '{op}'!", ctx.start, t1, t2)
            raise TypeCheckerException()
        except TypeCheckerException:
            raise

    def _checkComparison(self, ctx, op):
        """Para == y != — cualquier tipo siempre que sean iguales"""
        try:
            t1 = self.visit(ctx.expression(0))
            t2 = self.visit(ctx.expression(1))
            if t1 == t2:
                self.decoraciones.setTipo(ctx, BOOL)
                return BOOL
            self.reportErrorWithTypes(f"Incompatible types for '{op}'!", ctx.start, t1, t2)
            raise TypeCheckerException()
        except TypeCheckerException:
            raise

    def _checkOrderedComparison(self, ctx, op):
        """Para <, <=, >, >= — solo tipos ordenables"""
        try:
            t1 = self.visit(ctx.expression(0))
            t2 = self.visit(ctx.expression(1))
            if t1 == t2 and t1 in (INT, FLOAT64, STRING, RUNE):
                self.decoraciones.setTipo(ctx, BOOL)
                return BOOL
            self.reportErrorWithTypes(f"Incompatible types for '{op}'!", ctx.start, t1, t2)
            raise TypeCheckerException()
        except TypeCheckerException:
            raise

    # ═══════════════════════════════
    #  PRIMARY EXPRESSIONS
    # ═══════════════════════════════

    def visitPrimaryExpr(self, ctx: MiniGOParser.PrimaryExprContext):
        return self.visit(ctx.primaryExpression())

    def visitOperandExpr(self, ctx: MiniGOParser.OperandExprContext):
        return self.visit(ctx.operand())

    def visitSelectorExpr(self, ctx: MiniGOParser.SelectorExprContext):
        try:
            baseType = self.visit(ctx.primaryExpression())
            fieldName = ctx.selector().IDENTIFIER().getText()

            # El tipo base debe ser un struct
            if not isinstance(baseType, tuple) or baseType[0] != "struct":
                self.reportError("Selector '.' only applicable to struct types!", ctx.selector().IDENTIFIER().getSymbol())
                raise TypeCheckerException()

            structName = baseType[1]
            structIdent = self.symbolTable.buscar(structName)
            if structIdent is None or not isinstance(structIdent, TablaSimbolos.StructIdent):
                self.reportError("Undefined struct type!", ctx.selector().IDENTIFIER().getSymbol())
                raise TypeCheckerException()

            if fieldName not in structIdent.campos:
                self.reportError(f"Undefined field '{fieldName}' in struct!", ctx.selector().IDENTIFIER().getSymbol())
                raise TypeCheckerException()

            tipo = structIdent.campos[fieldName]
            self.decoraciones.setTipo(ctx, tipo)
            return tipo
        except TypeCheckerException:
            raise

    def visitIndexExpr(self, ctx: MiniGOParser.IndexExprContext):
        try:
            baseType = self.visit(ctx.primaryExpression())
            indexType = self.visit(ctx.index().expression())

            if indexType != INT:
                self.reportError("Index must be of type int!", ctx.index().expression().start)
                raise TypeCheckerException()

            if isinstance(baseType, tuple) and baseType[0] == "array":
                elemType = baseType[2]
                self.decoraciones.setTipo(ctx, elemType)
                return elemType
            elif isinstance(baseType, tuple) and baseType[0] == "slice":
                elemType = baseType[1]
                self.decoraciones.setTipo(ctx, elemType)
                return elemType
            else:
                self.reportError("Index operator only applicable to arrays and slices!", ctx.start)
                raise TypeCheckerException()
        except TypeCheckerException:
            raise

    def visitCallExpr(self, ctx: MiniGOParser.CallExprContext):
        try:
            # Obtener el nombre de la función desde la expresión base
            baseCtx = ctx.primaryExpression()
            funcIdent = None

            # Buscar el identificador de la función en la tabla de símbolos
            if isinstance(baseCtx, MiniGOParser.OperandExprContext):
                operand = baseCtx.operand()
                if isinstance(operand, MiniGOParser.IdentifierOperandContext):
                    nombre = operand.IDENTIFIER().getText()
                    funcIdent = self.symbolTable.buscar(nombre)

            if funcIdent is None:
                # No pudimos resolver la función, visitamos igual sin verificar
                return self.visit(baseCtx)

            if not isinstance(funcIdent, TablaSimbolos.MethodIdent):
                self.reportError("Not a function!", baseCtx.start)
                raise TypeCheckerException()

            # Verificar argumentos
            argTypes = []
            if ctx.arguments().expressionList() is not None:
                argTypes = self.visit(ctx.arguments().expressionList())

            if len(argTypes) != len(funcIdent.params):
                self.reportError(
                    f"Wrong number of arguments — expected {len(funcIdent.params)} but got {len(argTypes)}!",
                    baseCtx.start
                )
            else:
                for i in range(len(argTypes)):
                    if argTypes[i] != funcIdent.params[i]:
                        self.reportErrorWithTypes(
                            f"Incompatible argument type at position {i + 1}!",
                            baseCtx.start,
                            funcIdent.params[i],
                            argTypes[i]
                        )

            self.decoraciones.setRef(ctx, funcIdent)
            return funcIdent.tipo

        except TypeCheckerException:
            raise

    def visitAppendExpr(self, ctx: MiniGOParser.AppendExprContext):
        try:
            sliceType = self.visit(ctx.appendExpression().expression(0))
            elemType = self.visit(ctx.appendExpression().expression(1))

            if not isinstance(sliceType, tuple) or sliceType[0] != "slice":
                self.reportError("First argument of 'append' must be a slice!", ctx.start)
                raise TypeCheckerException()

            if sliceType[1] != elemType:
                self.reportErrorWithTypes(
                    "Element type mismatch in 'append'!",
                    ctx.start, sliceType[1], elemType
                )
                raise TypeCheckerException()

            self.decoraciones.setTipo(ctx, sliceType)
            return sliceType
        except TypeCheckerException:
            raise

    def visitLengthExpr(self, ctx: MiniGOParser.LengthExprContext):
        try:
            exprType = self.visit(ctx.lengthExpression().expression())
            if not isinstance(exprType, tuple) or exprType[0] not in ("array", "slice"):
                self.reportError("'len' only applicable to arrays and slices!", ctx.start)
                raise TypeCheckerException()
            self.decoraciones.setTipo(ctx, INT)
            return INT
        except TypeCheckerException:
            raise

    def visitCapExpr(self, ctx: MiniGOParser.CapExprContext):
        try:
            exprType = self.visit(ctx.capExpression().expression())
            if not isinstance(exprType, tuple) or exprType[0] not in ("array", "slice"):
                self.reportError("'cap' only applicable to arrays and slices!", ctx.start)
                raise TypeCheckerException()
            self.decoraciones.setTipo(ctx, INT)
            return INT
        except TypeCheckerException:
            raise

    # ═══════════════════════════════
    #  OPERANDS Y LITERALES
    # ═══════════════════════════════

    def visitLiteralOperand(self, ctx: MiniGOParser.LiteralOperandContext):
        return self.visit(ctx.literal())

    def visitIdentifierOperand(self, ctx: MiniGOParser.IdentifierOperandContext):
        nombre = ctx.IDENTIFIER().getText()
        token = ctx.IDENTIFIER().getSymbol()

        # 'true' y 'false' son literales bool (el lexer los trata como IDENTIFIER)
        if nombre in ("true", "false"):
            self.decoraciones.setTipo(ctx, BOOL)
            return BOOL

        ident = self.symbolTable.buscar(nombre)

        if ident is None:
            self.reportError("Undefined identifier!", token)
            raise TypeCheckerException()

        if isinstance(ident, TablaSimbolos.MethodIdent):
            # Es una función siendo llamada sin argumentos
            self.decoraciones.setRef(ctx, ident)
            return ident.tipo

        self.decoraciones.setRef(ctx, ident)
        self.decoraciones.setTipo(ctx, ident.tipo)
        return ident.tipo

    def visitGroupedExpr(self, ctx: MiniGOParser.GroupedExprContext):
        try:
            tipo = self.visit(ctx.expression())
            self.decoraciones.setTipo(ctx, tipo)
            return tipo
        except TypeCheckerException:
            raise

    def visitIntLit(self, ctx: MiniGOParser.IntLitContext):
        self.decoraciones.setTipo(ctx, INT)
        return INT

    def visitFloatLit(self, ctx: MiniGOParser.FloatLitContext):
        self.decoraciones.setTipo(ctx, FLOAT64)
        return FLOAT64

    def visitRuneLit(self, ctx: MiniGOParser.RuneLitContext):
        self.decoraciones.setTipo(ctx, RUNE)
        return RUNE

    def visitRawStringLit(self, ctx: MiniGOParser.RawStringLitContext):
        self.decoraciones.setTipo(ctx, STRING)
        return STRING

    def visitInterpretedStringLit(self, ctx: MiniGOParser.InterpretedStringLitContext):
        self.decoraciones.setTipo(ctx, STRING)
        return STRING