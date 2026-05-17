# Generated from TextToBin.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TextToBinParser import TextToBinParser
else:
    from TextToBinParser import TextToBinParser

# This class defines a complete listener for a parse tree produced by TextToBinParser.
class TextToBinListener(ParseTreeListener):

    # Enter a parse tree produced by TextToBinParser#program.
    def enterProgram(self, ctx:TextToBinParser.ProgramContext):
        pass

    # Exit a parse tree produced by TextToBinParser#program.
    def exitProgram(self, ctx:TextToBinParser.ProgramContext):
        pass


    # Enter a parse tree produced by TextToBinParser#statement.
    def enterStatement(self, ctx:TextToBinParser.StatementContext):
        pass

    # Exit a parse tree produced by TextToBinParser#statement.
    def exitStatement(self, ctx:TextToBinParser.StatementContext):
        pass


    # Enter a parse tree produced by TextToBinParser#expr.
    def enterExpr(self, ctx:TextToBinParser.ExprContext):
        pass

    # Exit a parse tree produced by TextToBinParser#expr.
    def exitExpr(self, ctx:TextToBinParser.ExprContext):
        pass


    # Enter a parse tree produced by TextToBinParser#relationalExpr.
    def enterRelationalExpr(self, ctx:TextToBinParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by TextToBinParser#relationalExpr.
    def exitRelationalExpr(self, ctx:TextToBinParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by TextToBinParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:TextToBinParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by TextToBinParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:TextToBinParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by TextToBinParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:TextToBinParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by TextToBinParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:TextToBinParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by TextToBinParser#unaryExpr.
    def enterUnaryExpr(self, ctx:TextToBinParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by TextToBinParser#unaryExpr.
    def exitUnaryExpr(self, ctx:TextToBinParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by TextToBinParser#primary.
    def enterPrimary(self, ctx:TextToBinParser.PrimaryContext):
        pass

    # Exit a parse tree produced by TextToBinParser#primary.
    def exitPrimary(self, ctx:TextToBinParser.PrimaryContext):
        pass



del TextToBinParser