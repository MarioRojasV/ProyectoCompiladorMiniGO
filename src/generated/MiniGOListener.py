# Generated from MiniGO.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniGOParser import MiniGOParser
else:
    from MiniGOParser import MiniGOParser

# This class defines a complete listener for a parse tree produced by MiniGOParser.
class MiniGOListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGOParser#root.
    def enterRoot(self, ctx:MiniGOParser.RootContext):
        pass

    # Exit a parse tree produced by MiniGOParser#root.
    def exitRoot(self, ctx:MiniGOParser.RootContext):
        pass


    # Enter a parse tree produced by MiniGOParser#topDeclarationList.
    def enterTopDeclarationList(self, ctx:MiniGOParser.TopDeclarationListContext):
        pass

    # Exit a parse tree produced by MiniGOParser#topDeclarationList.
    def exitTopDeclarationList(self, ctx:MiniGOParser.TopDeclarationListContext):
        pass


    # Enter a parse tree produced by MiniGOParser#variableDecl.
    def enterVariableDecl(self, ctx:MiniGOParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by MiniGOParser#variableDecl.
    def exitVariableDecl(self, ctx:MiniGOParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by MiniGOParser#innerVarDecls.
    def enterInnerVarDecls(self, ctx:MiniGOParser.InnerVarDeclsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#innerVarDecls.
    def exitInnerVarDecls(self, ctx:MiniGOParser.InnerVarDeclsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#varDeclWithTypeAndValue.
    def enterVarDeclWithTypeAndValue(self, ctx:MiniGOParser.VarDeclWithTypeAndValueContext):
        pass

    # Exit a parse tree produced by MiniGOParser#varDeclWithTypeAndValue.
    def exitVarDeclWithTypeAndValue(self, ctx:MiniGOParser.VarDeclWithTypeAndValueContext):
        pass


    # Enter a parse tree produced by MiniGOParser#varDeclWithValue.
    def enterVarDeclWithValue(self, ctx:MiniGOParser.VarDeclWithValueContext):
        pass

    # Exit a parse tree produced by MiniGOParser#varDeclWithValue.
    def exitVarDeclWithValue(self, ctx:MiniGOParser.VarDeclWithValueContext):
        pass


    # Enter a parse tree produced by MiniGOParser#varDeclNoExps.
    def enterVarDeclNoExps(self, ctx:MiniGOParser.VarDeclNoExpsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#varDeclNoExps.
    def exitVarDeclNoExps(self, ctx:MiniGOParser.VarDeclNoExpsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#singleVarDeclNoExps.
    def enterSingleVarDeclNoExps(self, ctx:MiniGOParser.SingleVarDeclNoExpsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#singleVarDeclNoExps.
    def exitSingleVarDeclNoExps(self, ctx:MiniGOParser.SingleVarDeclNoExpsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#identifierList.
    def enterIdentifierList(self, ctx:MiniGOParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by MiniGOParser#identifierList.
    def exitIdentifierList(self, ctx:MiniGOParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by MiniGOParser#typeDecl.
    def enterTypeDecl(self, ctx:MiniGOParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by MiniGOParser#typeDecl.
    def exitTypeDecl(self, ctx:MiniGOParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by MiniGOParser#innerTypeDecls.
    def enterInnerTypeDecls(self, ctx:MiniGOParser.InnerTypeDeclsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#innerTypeDecls.
    def exitInnerTypeDecls(self, ctx:MiniGOParser.InnerTypeDeclsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#singleTypeDecl.
    def enterSingleTypeDecl(self, ctx:MiniGOParser.SingleTypeDeclContext):
        pass

    # Exit a parse tree produced by MiniGOParser#singleTypeDecl.
    def exitSingleTypeDecl(self, ctx:MiniGOParser.SingleTypeDeclContext):
        pass


    # Enter a parse tree produced by MiniGOParser#groupedType.
    def enterGroupedType(self, ctx:MiniGOParser.GroupedTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#groupedType.
    def exitGroupedType(self, ctx:MiniGOParser.GroupedTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#simpleType.
    def enterSimpleType(self, ctx:MiniGOParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#simpleType.
    def exitSimpleType(self, ctx:MiniGOParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#sliceType.
    def enterSliceType(self, ctx:MiniGOParser.SliceTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#sliceType.
    def exitSliceType(self, ctx:MiniGOParser.SliceTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#arrayType.
    def enterArrayType(self, ctx:MiniGOParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#arrayType.
    def exitArrayType(self, ctx:MiniGOParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#structType.
    def enterStructType(self, ctx:MiniGOParser.StructTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#structType.
    def exitStructType(self, ctx:MiniGOParser.StructTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#sliceDeclType.
    def enterSliceDeclType(self, ctx:MiniGOParser.SliceDeclTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#sliceDeclType.
    def exitSliceDeclType(self, ctx:MiniGOParser.SliceDeclTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#arrayDeclType.
    def enterArrayDeclType(self, ctx:MiniGOParser.ArrayDeclTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#arrayDeclType.
    def exitArrayDeclType(self, ctx:MiniGOParser.ArrayDeclTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#structDeclType.
    def enterStructDeclType(self, ctx:MiniGOParser.StructDeclTypeContext):
        pass

    # Exit a parse tree produced by MiniGOParser#structDeclType.
    def exitStructDeclType(self, ctx:MiniGOParser.StructDeclTypeContext):
        pass


    # Enter a parse tree produced by MiniGOParser#structMemDecls.
    def enterStructMemDecls(self, ctx:MiniGOParser.StructMemDeclsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#structMemDecls.
    def exitStructMemDecls(self, ctx:MiniGOParser.StructMemDeclsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#funcDecl.
    def enterFuncDecl(self, ctx:MiniGOParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by MiniGOParser#funcDecl.
    def exitFuncDecl(self, ctx:MiniGOParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by MiniGOParser#funcFrontDecl.
    def enterFuncFrontDecl(self, ctx:MiniGOParser.FuncFrontDeclContext):
        pass

    # Exit a parse tree produced by MiniGOParser#funcFrontDecl.
    def exitFuncFrontDecl(self, ctx:MiniGOParser.FuncFrontDeclContext):
        pass


    # Enter a parse tree produced by MiniGOParser#funcArgDecls.
    def enterFuncArgDecls(self, ctx:MiniGOParser.FuncArgDeclsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#funcArgDecls.
    def exitFuncArgDecls(self, ctx:MiniGOParser.FuncArgDeclsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#expressionList.
    def enterExpressionList(self, ctx:MiniGOParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MiniGOParser#expressionList.
    def exitExpressionList(self, ctx:MiniGOParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MiniGOParser#pipeExpr.
    def enterPipeExpr(self, ctx:MiniGOParser.PipeExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#pipeExpr.
    def exitPipeExpr(self, ctx:MiniGOParser.PipeExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#modExpr.
    def enterModExpr(self, ctx:MiniGOParser.ModExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#modExpr.
    def exitModExpr(self, ctx:MiniGOParser.ModExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#gtExpr.
    def enterGtExpr(self, ctx:MiniGOParser.GtExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#gtExpr.
    def exitGtExpr(self, ctx:MiniGOParser.GtExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#xorUnaryExpr.
    def enterXorUnaryExpr(self, ctx:MiniGOParser.XorUnaryExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#xorUnaryExpr.
    def exitXorUnaryExpr(self, ctx:MiniGOParser.XorUnaryExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#rshiftExpr.
    def enterRshiftExpr(self, ctx:MiniGOParser.RshiftExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#rshiftExpr.
    def exitRshiftExpr(self, ctx:MiniGOParser.RshiftExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#orExpr.
    def enterOrExpr(self, ctx:MiniGOParser.OrExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#orExpr.
    def exitOrExpr(self, ctx:MiniGOParser.OrExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#subExpr.
    def enterSubExpr(self, ctx:MiniGOParser.SubExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#subExpr.
    def exitSubExpr(self, ctx:MiniGOParser.SubExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#multExpr.
    def enterMultExpr(self, ctx:MiniGOParser.MultExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#multExpr.
    def exitMultExpr(self, ctx:MiniGOParser.MultExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#xorExpr.
    def enterXorExpr(self, ctx:MiniGOParser.XorExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#xorExpr.
    def exitXorExpr(self, ctx:MiniGOParser.XorExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#neqExpr.
    def enterNeqExpr(self, ctx:MiniGOParser.NeqExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#neqExpr.
    def exitNeqExpr(self, ctx:MiniGOParser.NeqExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ampExpr.
    def enterAmpExpr(self, ctx:MiniGOParser.AmpExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ampExpr.
    def exitAmpExpr(self, ctx:MiniGOParser.AmpExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#eqExpr.
    def enterEqExpr(self, ctx:MiniGOParser.EqExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#eqExpr.
    def exitEqExpr(self, ctx:MiniGOParser.EqExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ltExpr.
    def enterLtExpr(self, ctx:MiniGOParser.LtExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ltExpr.
    def exitLtExpr(self, ctx:MiniGOParser.LtExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#notExpr.
    def enterNotExpr(self, ctx:MiniGOParser.NotExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#notExpr.
    def exitNotExpr(self, ctx:MiniGOParser.NotExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:MiniGOParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:MiniGOParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:MiniGOParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:MiniGOParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ampxorExpr.
    def enterAmpxorExpr(self, ctx:MiniGOParser.AmpxorExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ampxorExpr.
    def exitAmpxorExpr(self, ctx:MiniGOParser.AmpxorExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#addExpr.
    def enterAddExpr(self, ctx:MiniGOParser.AddExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#addExpr.
    def exitAddExpr(self, ctx:MiniGOParser.AddExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#unaryPlusExpr.
    def enterUnaryPlusExpr(self, ctx:MiniGOParser.UnaryPlusExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#unaryPlusExpr.
    def exitUnaryPlusExpr(self, ctx:MiniGOParser.UnaryPlusExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#leqExpr.
    def enterLeqExpr(self, ctx:MiniGOParser.LeqExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#leqExpr.
    def exitLeqExpr(self, ctx:MiniGOParser.LeqExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#divExpr.
    def enterDivExpr(self, ctx:MiniGOParser.DivExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#divExpr.
    def exitDivExpr(self, ctx:MiniGOParser.DivExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#geqExpr.
    def enterGeqExpr(self, ctx:MiniGOParser.GeqExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#geqExpr.
    def exitGeqExpr(self, ctx:MiniGOParser.GeqExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#lshiftExpr.
    def enterLshiftExpr(self, ctx:MiniGOParser.LshiftExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#lshiftExpr.
    def exitLshiftExpr(self, ctx:MiniGOParser.LshiftExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#andExpr.
    def enterAndExpr(self, ctx:MiniGOParser.AndExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#andExpr.
    def exitAndExpr(self, ctx:MiniGOParser.AndExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#lengthExpr.
    def enterLengthExpr(self, ctx:MiniGOParser.LengthExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#lengthExpr.
    def exitLengthExpr(self, ctx:MiniGOParser.LengthExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#indexExpr.
    def enterIndexExpr(self, ctx:MiniGOParser.IndexExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#indexExpr.
    def exitIndexExpr(self, ctx:MiniGOParser.IndexExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#selectorExpr.
    def enterSelectorExpr(self, ctx:MiniGOParser.SelectorExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#selectorExpr.
    def exitSelectorExpr(self, ctx:MiniGOParser.SelectorExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#operandExpr.
    def enterOperandExpr(self, ctx:MiniGOParser.OperandExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#operandExpr.
    def exitOperandExpr(self, ctx:MiniGOParser.OperandExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#appendExpr.
    def enterAppendExpr(self, ctx:MiniGOParser.AppendExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#appendExpr.
    def exitAppendExpr(self, ctx:MiniGOParser.AppendExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#callExpr.
    def enterCallExpr(self, ctx:MiniGOParser.CallExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#callExpr.
    def exitCallExpr(self, ctx:MiniGOParser.CallExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#capExpr.
    def enterCapExpr(self, ctx:MiniGOParser.CapExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#capExpr.
    def exitCapExpr(self, ctx:MiniGOParser.CapExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#literalOperand.
    def enterLiteralOperand(self, ctx:MiniGOParser.LiteralOperandContext):
        pass

    # Exit a parse tree produced by MiniGOParser#literalOperand.
    def exitLiteralOperand(self, ctx:MiniGOParser.LiteralOperandContext):
        pass


    # Enter a parse tree produced by MiniGOParser#identifierOperand.
    def enterIdentifierOperand(self, ctx:MiniGOParser.IdentifierOperandContext):
        pass

    # Exit a parse tree produced by MiniGOParser#identifierOperand.
    def exitIdentifierOperand(self, ctx:MiniGOParser.IdentifierOperandContext):
        pass


    # Enter a parse tree produced by MiniGOParser#groupedExpr.
    def enterGroupedExpr(self, ctx:MiniGOParser.GroupedExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#groupedExpr.
    def exitGroupedExpr(self, ctx:MiniGOParser.GroupedExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#intLit.
    def enterIntLit(self, ctx:MiniGOParser.IntLitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#intLit.
    def exitIntLit(self, ctx:MiniGOParser.IntLitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#floatLit.
    def enterFloatLit(self, ctx:MiniGOParser.FloatLitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#floatLit.
    def exitFloatLit(self, ctx:MiniGOParser.FloatLitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#runeLit.
    def enterRuneLit(self, ctx:MiniGOParser.RuneLitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#runeLit.
    def exitRuneLit(self, ctx:MiniGOParser.RuneLitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#rawStringLit.
    def enterRawStringLit(self, ctx:MiniGOParser.RawStringLitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#rawStringLit.
    def exitRawStringLit(self, ctx:MiniGOParser.RawStringLitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#interpretedStringLit.
    def enterInterpretedStringLit(self, ctx:MiniGOParser.InterpretedStringLitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#interpretedStringLit.
    def exitInterpretedStringLit(self, ctx:MiniGOParser.InterpretedStringLitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#selector.
    def enterSelector(self, ctx:MiniGOParser.SelectorContext):
        pass

    # Exit a parse tree produced by MiniGOParser#selector.
    def exitSelector(self, ctx:MiniGOParser.SelectorContext):
        pass


    # Enter a parse tree produced by MiniGOParser#index.
    def enterIndex(self, ctx:MiniGOParser.IndexContext):
        pass

    # Exit a parse tree produced by MiniGOParser#index.
    def exitIndex(self, ctx:MiniGOParser.IndexContext):
        pass


    # Enter a parse tree produced by MiniGOParser#arguments.
    def enterArguments(self, ctx:MiniGOParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MiniGOParser#arguments.
    def exitArguments(self, ctx:MiniGOParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MiniGOParser#appendExpression.
    def enterAppendExpression(self, ctx:MiniGOParser.AppendExpressionContext):
        pass

    # Exit a parse tree produced by MiniGOParser#appendExpression.
    def exitAppendExpression(self, ctx:MiniGOParser.AppendExpressionContext):
        pass


    # Enter a parse tree produced by MiniGOParser#lengthExpression.
    def enterLengthExpression(self, ctx:MiniGOParser.LengthExpressionContext):
        pass

    # Exit a parse tree produced by MiniGOParser#lengthExpression.
    def exitLengthExpression(self, ctx:MiniGOParser.LengthExpressionContext):
        pass


    # Enter a parse tree produced by MiniGOParser#capExpression.
    def enterCapExpression(self, ctx:MiniGOParser.CapExpressionContext):
        pass

    # Exit a parse tree produced by MiniGOParser#capExpression.
    def exitCapExpression(self, ctx:MiniGOParser.CapExpressionContext):
        pass


    # Enter a parse tree produced by MiniGOParser#block.
    def enterBlock(self, ctx:MiniGOParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniGOParser#block.
    def exitBlock(self, ctx:MiniGOParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniGOParser#statementList.
    def enterStatementList(self, ctx:MiniGOParser.StatementListContext):
        pass

    # Exit a parse tree produced by MiniGOParser#statementList.
    def exitStatementList(self, ctx:MiniGOParser.StatementListContext):
        pass


    # Enter a parse tree produced by MiniGOParser#printStatement.
    def enterPrintStatement(self, ctx:MiniGOParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#printStatement.
    def exitPrintStatement(self, ctx:MiniGOParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#printlnStatement.
    def enterPrintlnStatement(self, ctx:MiniGOParser.PrintlnStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#printlnStatement.
    def exitPrintlnStatement(self, ctx:MiniGOParser.PrintlnStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#returnStatement.
    def enterReturnStatement(self, ctx:MiniGOParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#returnStatement.
    def exitReturnStatement(self, ctx:MiniGOParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#breakStatement.
    def enterBreakStatement(self, ctx:MiniGOParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#breakStatement.
    def exitBreakStatement(self, ctx:MiniGOParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#continueStatement.
    def enterContinueStatement(self, ctx:MiniGOParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#continueStatement.
    def exitContinueStatement(self, ctx:MiniGOParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#simpleStmt.
    def enterSimpleStmt(self, ctx:MiniGOParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by MiniGOParser#simpleStmt.
    def exitSimpleStmt(self, ctx:MiniGOParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by MiniGOParser#blockStatement.
    def enterBlockStatement(self, ctx:MiniGOParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#blockStatement.
    def exitBlockStatement(self, ctx:MiniGOParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#switchStmt.
    def enterSwitchStmt(self, ctx:MiniGOParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by MiniGOParser#switchStmt.
    def exitSwitchStmt(self, ctx:MiniGOParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ifStmt.
    def enterIfStmt(self, ctx:MiniGOParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ifStmt.
    def exitIfStmt(self, ctx:MiniGOParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniGOParser#loopStmt.
    def enterLoopStmt(self, ctx:MiniGOParser.LoopStmtContext):
        pass

    # Exit a parse tree produced by MiniGOParser#loopStmt.
    def exitLoopStmt(self, ctx:MiniGOParser.LoopStmtContext):
        pass


    # Enter a parse tree produced by MiniGOParser#typeDeclStatement.
    def enterTypeDeclStatement(self, ctx:MiniGOParser.TypeDeclStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#typeDeclStatement.
    def exitTypeDeclStatement(self, ctx:MiniGOParser.TypeDeclStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#varDeclStatement.
    def enterVarDeclStatement(self, ctx:MiniGOParser.VarDeclStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#varDeclStatement.
    def exitVarDeclStatement(self, ctx:MiniGOParser.VarDeclStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#incDecStatement.
    def enterIncDecStatement(self, ctx:MiniGOParser.IncDecStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#incDecStatement.
    def exitIncDecStatement(self, ctx:MiniGOParser.IncDecStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MiniGOParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MiniGOParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#assignStmt.
    def enterAssignStmt(self, ctx:MiniGOParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MiniGOParser#assignStmt.
    def exitAssignStmt(self, ctx:MiniGOParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MiniGOParser#shortVarDecl.
    def enterShortVarDecl(self, ctx:MiniGOParser.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by MiniGOParser#shortVarDecl.
    def exitShortVarDecl(self, ctx:MiniGOParser.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by MiniGOParser#emptyStatement.
    def enterEmptyStatement(self, ctx:MiniGOParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by MiniGOParser#emptyStatement.
    def exitEmptyStatement(self, ctx:MiniGOParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by MiniGOParser#simpleAssign.
    def enterSimpleAssign(self, ctx:MiniGOParser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#simpleAssign.
    def exitSimpleAssign(self, ctx:MiniGOParser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#plusAssign.
    def enterPlusAssign(self, ctx:MiniGOParser.PlusAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#plusAssign.
    def exitPlusAssign(self, ctx:MiniGOParser.PlusAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#minusAssign.
    def enterMinusAssign(self, ctx:MiniGOParser.MinusAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#minusAssign.
    def exitMinusAssign(self, ctx:MiniGOParser.MinusAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#multAssign.
    def enterMultAssign(self, ctx:MiniGOParser.MultAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#multAssign.
    def exitMultAssign(self, ctx:MiniGOParser.MultAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#divAssign.
    def enterDivAssign(self, ctx:MiniGOParser.DivAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#divAssign.
    def exitDivAssign(self, ctx:MiniGOParser.DivAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#modAssign.
    def enterModAssign(self, ctx:MiniGOParser.ModAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#modAssign.
    def exitModAssign(self, ctx:MiniGOParser.ModAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ampAssign.
    def enterAmpAssign(self, ctx:MiniGOParser.AmpAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ampAssign.
    def exitAmpAssign(self, ctx:MiniGOParser.AmpAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#pipeAssign.
    def enterPipeAssign(self, ctx:MiniGOParser.PipeAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#pipeAssign.
    def exitPipeAssign(self, ctx:MiniGOParser.PipeAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#xorAssign.
    def enterXorAssign(self, ctx:MiniGOParser.XorAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#xorAssign.
    def exitXorAssign(self, ctx:MiniGOParser.XorAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#lshiftAssign.
    def enterLshiftAssign(self, ctx:MiniGOParser.LshiftAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#lshiftAssign.
    def exitLshiftAssign(self, ctx:MiniGOParser.LshiftAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#rshiftAssign.
    def enterRshiftAssign(self, ctx:MiniGOParser.RshiftAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#rshiftAssign.
    def exitRshiftAssign(self, ctx:MiniGOParser.RshiftAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ampxorAssign.
    def enterAmpxorAssign(self, ctx:MiniGOParser.AmpxorAssignContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ampxorAssign.
    def exitAmpxorAssign(self, ctx:MiniGOParser.AmpxorAssignContext):
        pass


    # Enter a parse tree produced by MiniGOParser#simpleIf.
    def enterSimpleIf(self, ctx:MiniGOParser.SimpleIfContext):
        pass

    # Exit a parse tree produced by MiniGOParser#simpleIf.
    def exitSimpleIf(self, ctx:MiniGOParser.SimpleIfContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ifElseIf.
    def enterIfElseIf(self, ctx:MiniGOParser.IfElseIfContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ifElseIf.
    def exitIfElseIf(self, ctx:MiniGOParser.IfElseIfContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ifElse.
    def enterIfElse(self, ctx:MiniGOParser.IfElseContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ifElse.
    def exitIfElse(self, ctx:MiniGOParser.IfElseContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ifWithInit.
    def enterIfWithInit(self, ctx:MiniGOParser.IfWithInitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ifWithInit.
    def exitIfWithInit(self, ctx:MiniGOParser.IfWithInitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ifWithInitElseIf.
    def enterIfWithInitElseIf(self, ctx:MiniGOParser.IfWithInitElseIfContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ifWithInitElseIf.
    def exitIfWithInitElseIf(self, ctx:MiniGOParser.IfWithInitElseIfContext):
        pass


    # Enter a parse tree produced by MiniGOParser#ifWithInitElse.
    def enterIfWithInitElse(self, ctx:MiniGOParser.IfWithInitElseContext):
        pass

    # Exit a parse tree produced by MiniGOParser#ifWithInitElse.
    def exitIfWithInitElse(self, ctx:MiniGOParser.IfWithInitElseContext):
        pass


    # Enter a parse tree produced by MiniGOParser#infiniteLoop.
    def enterInfiniteLoop(self, ctx:MiniGOParser.InfiniteLoopContext):
        pass

    # Exit a parse tree produced by MiniGOParser#infiniteLoop.
    def exitInfiniteLoop(self, ctx:MiniGOParser.InfiniteLoopContext):
        pass


    # Enter a parse tree produced by MiniGOParser#whileLoop.
    def enterWhileLoop(self, ctx:MiniGOParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MiniGOParser#whileLoop.
    def exitWhileLoop(self, ctx:MiniGOParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MiniGOParser#forLoop.
    def enterForLoop(self, ctx:MiniGOParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MiniGOParser#forLoop.
    def exitForLoop(self, ctx:MiniGOParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MiniGOParser#forLoopNoCondition.
    def enterForLoopNoCondition(self, ctx:MiniGOParser.ForLoopNoConditionContext):
        pass

    # Exit a parse tree produced by MiniGOParser#forLoopNoCondition.
    def exitForLoopNoCondition(self, ctx:MiniGOParser.ForLoopNoConditionContext):
        pass


    # Enter a parse tree produced by MiniGOParser#switchWithInitAndExpr.
    def enterSwitchWithInitAndExpr(self, ctx:MiniGOParser.SwitchWithInitAndExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#switchWithInitAndExpr.
    def exitSwitchWithInitAndExpr(self, ctx:MiniGOParser.SwitchWithInitAndExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#switchWithExpr.
    def enterSwitchWithExpr(self, ctx:MiniGOParser.SwitchWithExprContext):
        pass

    # Exit a parse tree produced by MiniGOParser#switchWithExpr.
    def exitSwitchWithExpr(self, ctx:MiniGOParser.SwitchWithExprContext):
        pass


    # Enter a parse tree produced by MiniGOParser#switchWithInit.
    def enterSwitchWithInit(self, ctx:MiniGOParser.SwitchWithInitContext):
        pass

    # Exit a parse tree produced by MiniGOParser#switchWithInit.
    def exitSwitchWithInit(self, ctx:MiniGOParser.SwitchWithInitContext):
        pass


    # Enter a parse tree produced by MiniGOParser#switchEmpty.
    def enterSwitchEmpty(self, ctx:MiniGOParser.SwitchEmptyContext):
        pass

    # Exit a parse tree produced by MiniGOParser#switchEmpty.
    def exitSwitchEmpty(self, ctx:MiniGOParser.SwitchEmptyContext):
        pass


    # Enter a parse tree produced by MiniGOParser#expressionCaseClauseList.
    def enterExpressionCaseClauseList(self, ctx:MiniGOParser.ExpressionCaseClauseListContext):
        pass

    # Exit a parse tree produced by MiniGOParser#expressionCaseClauseList.
    def exitExpressionCaseClauseList(self, ctx:MiniGOParser.ExpressionCaseClauseListContext):
        pass


    # Enter a parse tree produced by MiniGOParser#expressionCaseClause.
    def enterExpressionCaseClause(self, ctx:MiniGOParser.ExpressionCaseClauseContext):
        pass

    # Exit a parse tree produced by MiniGOParser#expressionCaseClause.
    def exitExpressionCaseClause(self, ctx:MiniGOParser.ExpressionCaseClauseContext):
        pass


    # Enter a parse tree produced by MiniGOParser#caseClause.
    def enterCaseClause(self, ctx:MiniGOParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by MiniGOParser#caseClause.
    def exitCaseClause(self, ctx:MiniGOParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by MiniGOParser#defaultClause.
    def enterDefaultClause(self, ctx:MiniGOParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by MiniGOParser#defaultClause.
    def exitDefaultClause(self, ctx:MiniGOParser.DefaultClauseContext):
        pass



del MiniGOParser