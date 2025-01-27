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
        4,1,20,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,1,4,1,33,8,1,11,1,12,1,34,1,2,1,2,1,2,1,2,3,2,41,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,66,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,0,1,1,0,14,16,102,0,28,1,0,0,0,2,32,1,0,0,0,4,40,
        1,0,0,0,6,42,1,0,0,0,8,48,1,0,0,0,10,55,1,0,0,0,12,65,1,0,0,0,14,
        67,1,0,0,0,16,75,1,0,0,0,18,83,1,0,0,0,20,93,1,0,0,0,22,103,1,0,
        0,0,24,105,1,0,0,0,26,107,1,0,0,0,28,29,3,2,1,0,29,30,5,0,0,1,30,
        1,1,0,0,0,31,33,3,4,2,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,
        0,34,35,1,0,0,0,35,3,1,0,0,0,36,41,3,6,3,0,37,41,3,8,4,0,38,41,3,
        12,6,0,39,41,3,10,5,0,40,36,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,0,
        40,39,1,0,0,0,41,5,1,0,0,0,42,43,5,1,0,0,43,44,3,24,12,0,44,45,5,
        2,0,0,45,46,3,26,13,0,46,47,5,3,0,0,47,7,1,0,0,0,48,49,5,4,0,0,49,
        50,3,22,11,0,50,51,3,26,13,0,51,52,5,5,0,0,52,53,3,24,12,0,53,54,
        5,3,0,0,54,9,1,0,0,0,55,56,5,6,0,0,56,57,3,24,12,0,57,58,5,7,0,0,
        58,59,3,26,13,0,59,60,5,3,0,0,60,11,1,0,0,0,61,66,3,14,7,0,62,66,
        3,18,9,0,63,66,3,16,8,0,64,66,3,20,10,0,65,61,1,0,0,0,65,62,1,0,
        0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,13,1,0,0,0,67,68,5,8,0,0,68,69,
        3,24,12,0,69,70,5,9,0,0,70,71,3,24,12,0,71,72,5,5,0,0,72,73,3,24,
        12,0,73,74,5,3,0,0,74,15,1,0,0,0,75,76,5,10,0,0,76,77,3,24,12,0,
        77,78,5,11,0,0,78,79,3,24,12,0,79,80,5,5,0,0,80,81,3,24,12,0,81,
        82,5,3,0,0,82,17,1,0,0,0,83,84,5,12,0,0,84,85,3,24,12,0,85,86,5,
        11,0,0,86,87,3,24,12,0,87,88,5,9,0,0,88,89,3,24,12,0,89,90,5,5,0,
        0,90,91,3,24,12,0,91,92,5,3,0,0,92,19,1,0,0,0,93,94,5,13,0,0,94,
        95,3,24,12,0,95,96,5,11,0,0,96,97,3,24,12,0,97,98,5,9,0,0,98,99,
        3,24,12,0,99,100,5,5,0,0,100,101,3,24,12,0,101,102,5,3,0,0,102,21,
        1,0,0,0,103,104,7,0,0,0,104,23,1,0,0,0,105,106,5,17,0,0,106,25,1,
        0,0,0,107,108,5,18,0,0,108,27,1,0,0,0,3,34,40,65
    ]

class LLMChainParser ( Parser ):

    grammarFileName = "LLMChain.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DEFINE'", "'AS'", "';'", "'LOAD'", "'INTO'", 
                     "'OUTPUT'", "'TO'", "'ANALYZE'", "'USING'", "'SUMMARIZE'", 
                     "'WITH'", "'EXPAND'", "'REFINE'", "'IMAGE'", "'PDF'", 
                     "'TEXT'" ]

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
    RULE_analyzeStatement = 7
    RULE_summarizeStatement = 8
    RULE_expandStatement = 9
    RULE_refineStatement = 10
    RULE_type = 11
    RULE_name = 12
    RULE_string = 13

    ruleNames =  [ "start", "program", "statement", "defineStatement", "loadStatement", 
                   "outputStatement", "actionStatement", "analyzeStatement", 
                   "summarizeStatement", "expandStatement", "refineStatement", 
                   "type", "name", "string" ]

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
            self.state = 28
            self.program()
            self.state = 29
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
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.statement()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 13650) != 0)):
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.defineStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.loadStatement()
                pass
            elif token in [8, 10, 12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.actionStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
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

        def name(self):
            return self.getTypedRuleContext(LLMChainParser.NameContext,0)


        def string(self):
            return self.getTypedRuleContext(LLMChainParser.StringContext,0)


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
            self.state = 42
            self.match(LLMChainParser.T__0)
            self.state = 43
            self.name()
            self.state = 44
            self.match(LLMChainParser.T__1)
            self.state = 45
            self.string()
            self.state = 46
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

        def type_(self):
            return self.getTypedRuleContext(LLMChainParser.TypeContext,0)


        def string(self):
            return self.getTypedRuleContext(LLMChainParser.StringContext,0)


        def name(self):
            return self.getTypedRuleContext(LLMChainParser.NameContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(LLMChainParser.T__3)
            self.state = 49
            self.type_()
            self.state = 50
            self.string()
            self.state = 51
            self.match(LLMChainParser.T__4)
            self.state = 52
            self.name()
            self.state = 53
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

        def name(self):
            return self.getTypedRuleContext(LLMChainParser.NameContext,0)


        def string(self):
            return self.getTypedRuleContext(LLMChainParser.StringContext,0)


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
            self.state = 55
            self.match(LLMChainParser.T__5)
            self.state = 56
            self.name()
            self.state = 57
            self.match(LLMChainParser.T__6)
            self.state = 58
            self.string()
            self.state = 59
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

        def analyzeStatement(self):
            return self.getTypedRuleContext(LLMChainParser.AnalyzeStatementContext,0)


        def expandStatement(self):
            return self.getTypedRuleContext(LLMChainParser.ExpandStatementContext,0)


        def summarizeStatement(self):
            return self.getTypedRuleContext(LLMChainParser.SummarizeStatementContext,0)


        def refineStatement(self):
            return self.getTypedRuleContext(LLMChainParser.RefineStatementContext,0)


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
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.analyzeStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.expandStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.summarizeStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.refineStatement()
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


    class AnalyzeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LLMChainParser.NameContext)
            else:
                return self.getTypedRuleContext(LLMChainParser.NameContext,i)


        def getRuleIndex(self):
            return LLMChainParser.RULE_analyzeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnalyzeStatement" ):
                listener.enterAnalyzeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnalyzeStatement" ):
                listener.exitAnalyzeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnalyzeStatement" ):
                return visitor.visitAnalyzeStatement(self)
            else:
                return visitor.visitChildren(self)




    def analyzeStatement(self):

        localctx = LLMChainParser.AnalyzeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_analyzeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(LLMChainParser.T__7)
            self.state = 68
            self.name()
            self.state = 69
            self.match(LLMChainParser.T__8)
            self.state = 70
            self.name()
            self.state = 71
            self.match(LLMChainParser.T__4)
            self.state = 72
            self.name()
            self.state = 73
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummarizeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LLMChainParser.NameContext)
            else:
                return self.getTypedRuleContext(LLMChainParser.NameContext,i)


        def getRuleIndex(self):
            return LLMChainParser.RULE_summarizeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummarizeStatement" ):
                listener.enterSummarizeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummarizeStatement" ):
                listener.exitSummarizeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummarizeStatement" ):
                return visitor.visitSummarizeStatement(self)
            else:
                return visitor.visitChildren(self)




    def summarizeStatement(self):

        localctx = LLMChainParser.SummarizeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_summarizeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LLMChainParser.T__9)
            self.state = 76
            self.name()
            self.state = 77
            self.match(LLMChainParser.T__10)
            self.state = 78
            self.name()
            self.state = 79
            self.match(LLMChainParser.T__4)
            self.state = 80
            self.name()
            self.state = 81
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpandStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LLMChainParser.NameContext)
            else:
                return self.getTypedRuleContext(LLMChainParser.NameContext,i)


        def getRuleIndex(self):
            return LLMChainParser.RULE_expandStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpandStatement" ):
                listener.enterExpandStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpandStatement" ):
                listener.exitExpandStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpandStatement" ):
                return visitor.visitExpandStatement(self)
            else:
                return visitor.visitChildren(self)




    def expandStatement(self):

        localctx = LLMChainParser.ExpandStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expandStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LLMChainParser.T__11)
            self.state = 84
            self.name()
            self.state = 85
            self.match(LLMChainParser.T__10)
            self.state = 86
            self.name()
            self.state = 87
            self.match(LLMChainParser.T__8)
            self.state = 88
            self.name()
            self.state = 89
            self.match(LLMChainParser.T__4)
            self.state = 90
            self.name()
            self.state = 91
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RefineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LLMChainParser.NameContext)
            else:
                return self.getTypedRuleContext(LLMChainParser.NameContext,i)


        def getRuleIndex(self):
            return LLMChainParser.RULE_refineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefineStatement" ):
                listener.enterRefineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefineStatement" ):
                listener.exitRefineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefineStatement" ):
                return visitor.visitRefineStatement(self)
            else:
                return visitor.visitChildren(self)




    def refineStatement(self):

        localctx = LLMChainParser.RefineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_refineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(LLMChainParser.T__12)
            self.state = 94
            self.name()
            self.state = 95
            self.match(LLMChainParser.T__10)
            self.state = 96
            self.name()
            self.state = 97
            self.match(LLMChainParser.T__8)
            self.state = 98
            self.name()
            self.state = 99
            self.match(LLMChainParser.T__4)
            self.state = 100
            self.name()
            self.state = 101
            self.match(LLMChainParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LLMChainParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = LLMChainParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LLMChainParser.ID, 0)

        def getRuleIndex(self):
            return LLMChainParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = LLMChainParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(LLMChainParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(LLMChainParser.STRING, 0)

        def getRuleIndex(self):
            return LLMChainParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = LLMChainParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(LLMChainParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





