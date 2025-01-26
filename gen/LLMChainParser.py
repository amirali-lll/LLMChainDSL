# Generated from /Users/amirali/Programming/University/Compiler/LLMChainDSL/grammar/LLMChain.g4 by ANTLR 4.13.1
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
        4,1,20,82,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,4,1,19,8,1,11,1,12,1,20,1,2,1,2,1,2,1,2,3,2,27,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,80,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,5,7,
        81,0,14,1,0,0,0,2,18,1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,34,1,0,
        0,0,10,41,1,0,0,0,12,79,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,
        1,0,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,
        20,21,1,0,0,0,21,3,1,0,0,0,22,27,3,6,3,0,23,27,3,8,4,0,24,27,3,12,
        6,0,25,27,3,10,5,0,26,22,1,0,0,0,26,23,1,0,0,0,26,24,1,0,0,0,26,
        25,1,0,0,0,27,5,1,0,0,0,28,29,5,1,0,0,29,30,5,17,0,0,30,31,5,2,0,
        0,31,32,5,18,0,0,32,33,5,3,0,0,33,7,1,0,0,0,34,35,5,4,0,0,35,36,
        7,0,0,0,36,37,5,18,0,0,37,38,5,8,0,0,38,39,5,17,0,0,39,40,5,3,0,
        0,40,9,1,0,0,0,41,42,5,9,0,0,42,43,5,17,0,0,43,44,5,10,0,0,44,45,
        5,18,0,0,45,46,5,3,0,0,46,11,1,0,0,0,47,48,5,11,0,0,48,49,5,17,0,
        0,49,50,5,12,0,0,50,51,5,17,0,0,51,52,5,8,0,0,52,53,5,17,0,0,53,
        80,5,3,0,0,54,55,5,13,0,0,55,56,5,17,0,0,56,57,5,14,0,0,57,58,5,
        17,0,0,58,59,5,12,0,0,59,60,5,17,0,0,60,61,5,8,0,0,61,62,5,17,0,
        0,62,80,5,3,0,0,63,64,5,15,0,0,64,65,5,17,0,0,65,66,5,14,0,0,66,
        67,5,17,0,0,67,68,5,12,0,0,68,69,5,17,0,0,69,70,5,8,0,0,70,71,5,
        17,0,0,71,80,5,3,0,0,72,73,5,16,0,0,73,74,5,17,0,0,74,75,5,14,0,
        0,75,76,5,17,0,0,76,77,5,8,0,0,77,78,5,17,0,0,78,80,5,3,0,0,79,47,
        1,0,0,0,79,54,1,0,0,0,79,63,1,0,0,0,79,72,1,0,0,0,80,13,1,0,0,0,
        3,20,26,79
    ]

class LLMChainParser ( Parser ):

    grammarFileName = "LLMChain.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DEFINE'", "'AS'", "';'", "'LOAD'", "'IMAGE'", 
                     "'PDF'", "'TEXT'", "'INTO'", "'OUTPUT'", "'TO'", "'ANALYZE'", 
                     "'USING'", "'EXPAND'", "'WITH'", "'REFINE'", "'SUMMARIZE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "WS", "COMMENT" ]

    RULE_start = 0
    RULE_program = 1
    RULE_statement = 2
    RULE_defineStatement = 3
    RULE_loadStatement = 4
    RULE_outputStatement = 5
    RULE_actionStatement = 6

    ruleNames =  [ "start", "program", "statement", "defineStatement", "loadStatement", 
                   "outputStatement", "actionStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    ID=17
    STRING=18
    WS=19
    COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(LLMChainParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(LLMChainParser.EOF, 0)

        def getRuleIndex(self):
            return LLMChainParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = LLMChainParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.program()
            self.state = 15
            self.match(LLMChainParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LLMChainParser.StatementContext)
            else:
                return self.getTypedRuleContext(LLMChainParser.StatementContext,i)


        def getRuleIndex(self):
            return LLMChainParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LLMChainParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.statement()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 109074) != 0)):
                    break

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

        def defineStatement(self):
            return self.getTypedRuleContext(LLMChainParser.DefineStatementContext,0)


        def loadStatement(self):
            return self.getTypedRuleContext(LLMChainParser.LoadStatementContext,0)


        def actionStatement(self):
            return self.getTypedRuleContext(LLMChainParser.ActionStatementContext,0)


        def outputStatement(self):
            return self.getTypedRuleContext(LLMChainParser.OutputStatementContext,0)


        def getRuleIndex(self):
            return LLMChainParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LLMChainParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.defineStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.loadStatement()
                pass
            elif token in [11, 13, 15, 16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.actionStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.outputStatement()
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


    class DefineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LLMChainParser.ID, 0)

        def STRING(self):
            return self.getToken(LLMChainParser.STRING, 0)

        def getRuleIndex(self):
            return LLMChainParser.RULE_defineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineStatement" ):
                listener.enterDefineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineStatement" ):
                listener.exitDefineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineStatement" ):
                return visitor.visitDefineStatement(self)
            else:
                return visitor.visitChildren(self)




    def defineStatement(self):

        localctx = LLMChainParser.DefineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_defineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(LLMChainParser.T__0)
            self.state = 29
            self.match(LLMChainParser.ID)
            self.state = 30
            self.match(LLMChainParser.T__1)
            self.state = 31
            self.match(LLMChainParser.STRING)
            self.state = 32
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(LLMChainParser.STRING, 0)

        def ID(self):
            return self.getToken(LLMChainParser.ID, 0)

        def getRuleIndex(self):
            return LLMChainParser.RULE_loadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStatement" ):
                listener.enterLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStatement" ):
                listener.exitLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStatement" ):
                return visitor.visitLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def loadStatement(self):

        localctx = LLMChainParser.LoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loadStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(LLMChainParser.T__3)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 36
            self.match(LLMChainParser.STRING)
            self.state = 37
            self.match(LLMChainParser.T__7)
            self.state = 38
            self.match(LLMChainParser.ID)
            self.state = 39
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LLMChainParser.ID, 0)

        def STRING(self):
            return self.getToken(LLMChainParser.STRING, 0)

        def getRuleIndex(self):
            return LLMChainParser.RULE_outputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStatement" ):
                listener.enterOutputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStatement" ):
                listener.exitOutputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStatement" ):
                return visitor.visitOutputStatement(self)
            else:
                return visitor.visitChildren(self)




    def outputStatement(self):

        localctx = LLMChainParser.OutputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_outputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(LLMChainParser.T__8)
            self.state = 42
            self.match(LLMChainParser.ID)
            self.state = 43
            self.match(LLMChainParser.T__9)
            self.state = 44
            self.match(LLMChainParser.STRING)
            self.state = 45
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LLMChainParser.ID)
            else:
                return self.getToken(LLMChainParser.ID, i)

        def getRuleIndex(self):
            return LLMChainParser.RULE_actionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionStatement" ):
                listener.enterActionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionStatement" ):
                listener.exitActionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionStatement" ):
                return visitor.visitActionStatement(self)
            else:
                return visitor.visitChildren(self)




    def actionStatement(self):

        localctx = LLMChainParser.ActionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_actionStatement)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(LLMChainParser.T__10)
                self.state = 48
                self.match(LLMChainParser.ID)
                self.state = 49
                self.match(LLMChainParser.T__11)
                self.state = 50
                self.match(LLMChainParser.ID)
                self.state = 51
                self.match(LLMChainParser.T__7)
                self.state = 52
                self.match(LLMChainParser.ID)
                self.state = 53
                self.match(LLMChainParser.T__2)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(LLMChainParser.T__12)
                self.state = 55
                self.match(LLMChainParser.ID)
                self.state = 56
                self.match(LLMChainParser.T__13)
                self.state = 57
                self.match(LLMChainParser.ID)
                self.state = 58
                self.match(LLMChainParser.T__11)
                self.state = 59
                self.match(LLMChainParser.ID)
                self.state = 60
                self.match(LLMChainParser.T__7)
                self.state = 61
                self.match(LLMChainParser.ID)
                self.state = 62
                self.match(LLMChainParser.T__2)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(LLMChainParser.T__14)
                self.state = 64
                self.match(LLMChainParser.ID)
                self.state = 65
                self.match(LLMChainParser.T__13)
                self.state = 66
                self.match(LLMChainParser.ID)
                self.state = 67
                self.match(LLMChainParser.T__11)
                self.state = 68
                self.match(LLMChainParser.ID)
                self.state = 69
                self.match(LLMChainParser.T__7)
                self.state = 70
                self.match(LLMChainParser.ID)
                self.state = 71
                self.match(LLMChainParser.T__2)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(LLMChainParser.T__15)
                self.state = 73
                self.match(LLMChainParser.ID)
                self.state = 74
                self.match(LLMChainParser.T__13)
                self.state = 75
                self.match(LLMChainParser.ID)
                self.state = 76
                self.match(LLMChainParser.T__7)
                self.state = 77
                self.match(LLMChainParser.ID)
                self.state = 78
                self.match(LLMChainParser.T__2)
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





