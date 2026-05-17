# Generated from TextToBin.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,3,3,38,8,3,1,4,1,4,1,4,5,4,
        43,8,4,10,4,12,4,46,9,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,
        1,6,1,6,1,6,3,6,59,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,67,8,7,1,7,0,
        0,8,0,2,4,6,8,10,12,14,0,3,1,0,6,11,1,0,12,13,1,0,14,16,67,0,19,
        1,0,0,0,2,24,1,0,0,0,4,32,1,0,0,0,6,34,1,0,0,0,8,39,1,0,0,0,10,47,
        1,0,0,0,12,58,1,0,0,0,14,66,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,
        18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,
        0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,1,0,0,25,26,3,4,2,0,26,
        27,5,2,0,0,27,28,5,21,0,0,28,29,5,3,0,0,29,30,3,4,2,0,30,31,5,4,
        0,0,31,3,1,0,0,0,32,33,3,6,3,0,33,5,1,0,0,0,34,37,3,8,4,0,35,36,
        7,0,0,0,36,38,3,8,4,0,37,35,1,0,0,0,37,38,1,0,0,0,38,7,1,0,0,0,39,
        44,3,10,5,0,40,41,7,1,0,0,41,43,3,10,5,0,42,40,1,0,0,0,43,46,1,0,
        0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,9,1,0,0,0,46,44,1,0,0,0,47,52,
        3,12,6,0,48,49,7,2,0,0,49,51,3,12,6,0,50,48,1,0,0,0,51,54,1,0,0,
        0,52,50,1,0,0,0,52,53,1,0,0,0,53,11,1,0,0,0,54,52,1,0,0,0,55,56,
        5,13,0,0,56,59,3,12,6,0,57,59,3,14,7,0,58,55,1,0,0,0,58,57,1,0,0,
        0,59,13,1,0,0,0,60,67,5,20,0,0,61,67,5,21,0,0,62,63,5,17,0,0,63,
        64,3,4,2,0,64,65,5,18,0,0,65,67,1,0,0,0,66,60,1,0,0,0,66,61,1,0,
        0,0,66,62,1,0,0,0,67,15,1,0,0,0,6,19,37,44,52,58,66
    ]

class TextToBinParser ( Parser ):

    grammarFileName = "TextToBin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'='", "';'", "<INVALID>", 
                     "'=='", "<INVALID>", "'>='", "'<='", "'>'", "'<'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "THEN", "ASSIGN", "DELIMITER", 
                      "INVALID_OP", "EQ", "NEQ", "GE", "LE", "GT", "LT", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", 
                      "INVALID_ID", "NUMBER", "IDENTIFIER", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "UNKNOWN" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_relationalExpr = 3
    RULE_additiveExpr = 4
    RULE_multiplicativeExpr = 5
    RULE_unaryExpr = 6
    RULE_primary = 7

    ruleNames =  [ "program", "statement", "expr", "relationalExpr", "additiveExpr", 
                   "multiplicativeExpr", "unaryExpr", "primary" ]

    EOF = Token.EOF
    IF=1
    THEN=2
    ASSIGN=3
    DELIMITER=4
    INVALID_OP=5
    EQ=6
    NEQ=7
    GE=8
    LE=9
    GT=10
    LT=11
    PLUS=12
    MINUS=13
    MUL=14
    DIV=15
    MOD=16
    LPAREN=17
    RPAREN=18
    INVALID_ID=19
    NUMBER=20
    IDENTIFIER=21
    WS=22
    LINE_COMMENT=23
    BLOCK_COMMENT=24
    UNKNOWN=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TextToBinParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextToBinParser.StatementContext)
            else:
                return self.getTypedRuleContext(TextToBinParser.StatementContext,i)


        def getRuleIndex(self):
            return TextToBinParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = TextToBinParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(TextToBinParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TextToBinParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextToBinParser.ExprContext)
            else:
                return self.getTypedRuleContext(TextToBinParser.ExprContext,i)


        def THEN(self):
            return self.getToken(TextToBinParser.THEN, 0)

        def IDENTIFIER(self):
            return self.getToken(TextToBinParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(TextToBinParser.ASSIGN, 0)

        def DELIMITER(self):
            return self.getToken(TextToBinParser.DELIMITER, 0)

        def getRuleIndex(self):
            return TextToBinParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TextToBinParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(TextToBinParser.IF)
            self.state = 25
            self.expr()
            self.state = 26
            self.match(TextToBinParser.THEN)
            self.state = 27
            self.match(TextToBinParser.IDENTIFIER)
            self.state = 28
            self.match(TextToBinParser.ASSIGN)
            self.state = 29
            self.expr()
            self.state = 30
            self.match(TextToBinParser.DELIMITER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self):
            return self.getTypedRuleContext(TextToBinParser.RelationalExprContext,0)


        def getRuleIndex(self):
            return TextToBinParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = TextToBinParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.relationalExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextToBinParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(TextToBinParser.AdditiveExprContext,i)


        def GT(self):
            return self.getToken(TextToBinParser.GT, 0)

        def LT(self):
            return self.getToken(TextToBinParser.LT, 0)

        def GE(self):
            return self.getToken(TextToBinParser.GE, 0)

        def LE(self):
            return self.getToken(TextToBinParser.LE, 0)

        def EQ(self):
            return self.getToken(TextToBinParser.EQ, 0)

        def NEQ(self):
            return self.getToken(TextToBinParser.NEQ, 0)

        def getRuleIndex(self):
            return TextToBinParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)




    def relationalExpr(self):

        localctx = TextToBinParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.additiveExpr()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0):
                self.state = 35
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.additiveExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextToBinParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(TextToBinParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(TextToBinParser.PLUS)
            else:
                return self.getToken(TextToBinParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(TextToBinParser.MINUS)
            else:
                return self.getToken(TextToBinParser.MINUS, i)

        def getRuleIndex(self):
            return TextToBinParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)




    def additiveExpr(self):

        localctx = TextToBinParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.multiplicativeExpr()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.multiplicativeExpr()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TextToBinParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(TextToBinParser.UnaryExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(TextToBinParser.MUL)
            else:
                return self.getToken(TextToBinParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(TextToBinParser.DIV)
            else:
                return self.getToken(TextToBinParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(TextToBinParser.MOD)
            else:
                return self.getToken(TextToBinParser.MOD, i)

        def getRuleIndex(self):
            return TextToBinParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)




    def multiplicativeExpr(self):

        localctx = TextToBinParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.unaryExpr()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 48
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self.unaryExpr()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(TextToBinParser.MINUS, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(TextToBinParser.UnaryExprContext,0)


        def primary(self):
            return self.getTypedRuleContext(TextToBinParser.PrimaryContext,0)


        def getRuleIndex(self):
            return TextToBinParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)




    def unaryExpr(self):

        localctx = TextToBinParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unaryExpr)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(TextToBinParser.MINUS)
                self.state = 56
                self.unaryExpr()
                pass
            elif token in [17, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(TextToBinParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(TextToBinParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(TextToBinParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TextToBinParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TextToBinParser.RPAREN, 0)

        def getRuleIndex(self):
            return TextToBinParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = TextToBinParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primary)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(TextToBinParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(TextToBinParser.IDENTIFIER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(TextToBinParser.LPAREN)
                self.state = 63
                self.expr()
                self.state = 64
                self.match(TextToBinParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





