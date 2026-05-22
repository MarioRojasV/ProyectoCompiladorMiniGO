# Generated from MiniGO.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniGOParser import MiniGOParser
else:
    from MiniGOParser import MiniGOParser

# This class defines a complete generic visitor for a parse tree produced by MiniGOParser.

class MiniGOVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGOParser#root.
    def visitRoot(self, ctx:MiniGOParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#topDeclarationList.
    def visitTopDeclarationList(self, ctx:MiniGOParser.TopDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#variableDecl.
    def visitVariableDecl(self, ctx:MiniGOParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#innerVarDecls.
    def visitInnerVarDecls(self, ctx:MiniGOParser.InnerVarDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#varDeclWithTypeAndValue.
    def visitVarDeclWithTypeAndValue(self, ctx:MiniGOParser.VarDeclWithTypeAndValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#varDeclWithValue.
    def visitVarDeclWithValue(self, ctx:MiniGOParser.VarDeclWithValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#varDeclNoExps.
    def visitVarDeclNoExps(self, ctx:MiniGOParser.VarDeclNoExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#singleVarDeclNoExps.
    def visitSingleVarDeclNoExps(self, ctx:MiniGOParser.SingleVarDeclNoExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#identifierList.
    def visitIdentifierList(self, ctx:MiniGOParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#typeDecl.
    def visitTypeDecl(self, ctx:MiniGOParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#innerTypeDecls.
    def visitInnerTypeDecls(self, ctx:MiniGOParser.InnerTypeDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#singleTypeDecl.
    def visitSingleTypeDecl(self, ctx:MiniGOParser.SingleTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#groupedType.
    def visitGroupedType(self, ctx:MiniGOParser.GroupedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#simpleType.
    def visitSimpleType(self, ctx:MiniGOParser.SimpleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#sliceType.
    def visitSliceType(self, ctx:MiniGOParser.SliceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#arrayType.
    def visitArrayType(self, ctx:MiniGOParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#structType.
    def visitStructType(self, ctx:MiniGOParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#sliceDeclType.
    def visitSliceDeclType(self, ctx:MiniGOParser.SliceDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#arrayDeclType.
    def visitArrayDeclType(self, ctx:MiniGOParser.ArrayDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#structDeclType.
    def visitStructDeclType(self, ctx:MiniGOParser.StructDeclTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#structMemDecls.
    def visitStructMemDecls(self, ctx:MiniGOParser.StructMemDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGOParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#funcFrontDecl.
    def visitFuncFrontDecl(self, ctx:MiniGOParser.FuncFrontDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#funcArgDecls.
    def visitFuncArgDecls(self, ctx:MiniGOParser.FuncArgDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#expressionList.
    def visitExpressionList(self, ctx:MiniGOParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#pipeExpr.
    def visitPipeExpr(self, ctx:MiniGOParser.PipeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#modExpr.
    def visitModExpr(self, ctx:MiniGOParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#gtExpr.
    def visitGtExpr(self, ctx:MiniGOParser.GtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#xorUnaryExpr.
    def visitXorUnaryExpr(self, ctx:MiniGOParser.XorUnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#rshiftExpr.
    def visitRshiftExpr(self, ctx:MiniGOParser.RshiftExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#orExpr.
    def visitOrExpr(self, ctx:MiniGOParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#subExpr.
    def visitSubExpr(self, ctx:MiniGOParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#multExpr.
    def visitMultExpr(self, ctx:MiniGOParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#xorExpr.
    def visitXorExpr(self, ctx:MiniGOParser.XorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#neqExpr.
    def visitNeqExpr(self, ctx:MiniGOParser.NeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ampExpr.
    def visitAmpExpr(self, ctx:MiniGOParser.AmpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#eqExpr.
    def visitEqExpr(self, ctx:MiniGOParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ltExpr.
    def visitLtExpr(self, ctx:MiniGOParser.LtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#notExpr.
    def visitNotExpr(self, ctx:MiniGOParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGOParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MiniGOParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ampxorExpr.
    def visitAmpxorExpr(self, ctx:MiniGOParser.AmpxorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#addExpr.
    def visitAddExpr(self, ctx:MiniGOParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#unaryPlusExpr.
    def visitUnaryPlusExpr(self, ctx:MiniGOParser.UnaryPlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#leqExpr.
    def visitLeqExpr(self, ctx:MiniGOParser.LeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#divExpr.
    def visitDivExpr(self, ctx:MiniGOParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#geqExpr.
    def visitGeqExpr(self, ctx:MiniGOParser.GeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#lshiftExpr.
    def visitLshiftExpr(self, ctx:MiniGOParser.LshiftExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#andExpr.
    def visitAndExpr(self, ctx:MiniGOParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#lengthExpr.
    def visitLengthExpr(self, ctx:MiniGOParser.LengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#indexExpr.
    def visitIndexExpr(self, ctx:MiniGOParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#selectorExpr.
    def visitSelectorExpr(self, ctx:MiniGOParser.SelectorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#operandExpr.
    def visitOperandExpr(self, ctx:MiniGOParser.OperandExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#appendExpr.
    def visitAppendExpr(self, ctx:MiniGOParser.AppendExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#callExpr.
    def visitCallExpr(self, ctx:MiniGOParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#capExpr.
    def visitCapExpr(self, ctx:MiniGOParser.CapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#literalOperand.
    def visitLiteralOperand(self, ctx:MiniGOParser.LiteralOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#identifierOperand.
    def visitIdentifierOperand(self, ctx:MiniGOParser.IdentifierOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#groupedExpr.
    def visitGroupedExpr(self, ctx:MiniGOParser.GroupedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#intLit.
    def visitIntLit(self, ctx:MiniGOParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#floatLit.
    def visitFloatLit(self, ctx:MiniGOParser.FloatLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#runeLit.
    def visitRuneLit(self, ctx:MiniGOParser.RuneLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#rawStringLit.
    def visitRawStringLit(self, ctx:MiniGOParser.RawStringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#interpretedStringLit.
    def visitInterpretedStringLit(self, ctx:MiniGOParser.InterpretedStringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#selector.
    def visitSelector(self, ctx:MiniGOParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#index.
    def visitIndex(self, ctx:MiniGOParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#arguments.
    def visitArguments(self, ctx:MiniGOParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#appendExpression.
    def visitAppendExpression(self, ctx:MiniGOParser.AppendExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#lengthExpression.
    def visitLengthExpression(self, ctx:MiniGOParser.LengthExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#capExpression.
    def visitCapExpression(self, ctx:MiniGOParser.CapExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#block.
    def visitBlock(self, ctx:MiniGOParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#statementList.
    def visitStatementList(self, ctx:MiniGOParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#printStatement.
    def visitPrintStatement(self, ctx:MiniGOParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#printlnStatement.
    def visitPrintlnStatement(self, ctx:MiniGOParser.PrintlnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGOParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGOParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGOParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#simpleStmt.
    def visitSimpleStmt(self, ctx:MiniGOParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#blockStatement.
    def visitBlockStatement(self, ctx:MiniGOParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#switchStmt.
    def visitSwitchStmt(self, ctx:MiniGOParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ifStmt.
    def visitIfStmt(self, ctx:MiniGOParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#loopStmt.
    def visitLoopStmt(self, ctx:MiniGOParser.LoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#typeDeclStatement.
    def visitTypeDeclStatement(self, ctx:MiniGOParser.TypeDeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#varDeclStatement.
    def visitVarDeclStatement(self, ctx:MiniGOParser.VarDeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#incDecStatement.
    def visitIncDecStatement(self, ctx:MiniGOParser.IncDecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MiniGOParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#assignStmt.
    def visitAssignStmt(self, ctx:MiniGOParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:MiniGOParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#emptyStatement.
    def visitEmptyStatement(self, ctx:MiniGOParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#simpleAssign.
    def visitSimpleAssign(self, ctx:MiniGOParser.SimpleAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#plusAssign.
    def visitPlusAssign(self, ctx:MiniGOParser.PlusAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#minusAssign.
    def visitMinusAssign(self, ctx:MiniGOParser.MinusAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#multAssign.
    def visitMultAssign(self, ctx:MiniGOParser.MultAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#divAssign.
    def visitDivAssign(self, ctx:MiniGOParser.DivAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#modAssign.
    def visitModAssign(self, ctx:MiniGOParser.ModAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ampAssign.
    def visitAmpAssign(self, ctx:MiniGOParser.AmpAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#pipeAssign.
    def visitPipeAssign(self, ctx:MiniGOParser.PipeAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#xorAssign.
    def visitXorAssign(self, ctx:MiniGOParser.XorAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#lshiftAssign.
    def visitLshiftAssign(self, ctx:MiniGOParser.LshiftAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#rshiftAssign.
    def visitRshiftAssign(self, ctx:MiniGOParser.RshiftAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ampxorAssign.
    def visitAmpxorAssign(self, ctx:MiniGOParser.AmpxorAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#simpleIf.
    def visitSimpleIf(self, ctx:MiniGOParser.SimpleIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ifElseIf.
    def visitIfElseIf(self, ctx:MiniGOParser.IfElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ifElse.
    def visitIfElse(self, ctx:MiniGOParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ifWithInit.
    def visitIfWithInit(self, ctx:MiniGOParser.IfWithInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ifWithInitElseIf.
    def visitIfWithInitElseIf(self, ctx:MiniGOParser.IfWithInitElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#ifWithInitElse.
    def visitIfWithInitElse(self, ctx:MiniGOParser.IfWithInitElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#infiniteLoop.
    def visitInfiniteLoop(self, ctx:MiniGOParser.InfiniteLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#whileLoop.
    def visitWhileLoop(self, ctx:MiniGOParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#forLoop.
    def visitForLoop(self, ctx:MiniGOParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#forLoopNoCondition.
    def visitForLoopNoCondition(self, ctx:MiniGOParser.ForLoopNoConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#switchWithInitAndExpr.
    def visitSwitchWithInitAndExpr(self, ctx:MiniGOParser.SwitchWithInitAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#switchWithExpr.
    def visitSwitchWithExpr(self, ctx:MiniGOParser.SwitchWithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#switchWithInit.
    def visitSwitchWithInit(self, ctx:MiniGOParser.SwitchWithInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#switchEmpty.
    def visitSwitchEmpty(self, ctx:MiniGOParser.SwitchEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#expressionCaseClauseList.
    def visitExpressionCaseClauseList(self, ctx:MiniGOParser.ExpressionCaseClauseListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#expressionCaseClause.
    def visitExpressionCaseClause(self, ctx:MiniGOParser.ExpressionCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#caseClause.
    def visitCaseClause(self, ctx:MiniGOParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGOParser#defaultClause.
    def visitDefaultClause(self, ctx:MiniGOParser.DefaultClauseContext):
        return self.visitChildren(ctx)



del MiniGOParser