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
        4,1,20,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,4,1,25,8,1,11,1,12,1,26,
        1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,90,8,6,
        1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,
        1,0,14,16,94,0,20,1,0,0,0,2,24,1,0,0,0,4,32,1,0,0,0,6,34,1,0,0,0,
        8,40,1,0,0,0,10,47,1,0,0,0,12,89,1,0,0,0,14,91,1,0,0,0,16,93,1,0,
        0,0,18,95,1,0,0,0,20,21,3,2,1,0,21,22,5,0,0,1,22,1,1,0,0,0,23,25,
        3,4,2,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,
        27,3,1,0,0,0,28,33,3,6,3,0,29,33,3,8,4,0,30,33,3,12,6,0,31,33,3,
        10,5,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        5,1,0,0,0,34,35,5,1,0,0,35,36,3,16,8,0,36,37,5,2,0,0,37,38,3,18,
        9,0,38,39,5,3,0,0,39,7,1,0,0,0,40,41,5,4,0,0,41,42,3,14,7,0,42,43,
        3,18,9,0,43,44,5,5,0,0,44,45,3,16,8,0,45,46,5,3,0,0,46,9,1,0,0,0,
        47,48,5,6,0,0,48,49,3,16,8,0,49,50,5,7,0,0,50,51,3,18,9,0,51,52,
        5,3,0,0,52,11,1,0,0,0,53,54,5,8,0,0,54,55,3,16,8,0,55,56,5,9,0,0,
        56,57,3,16,8,0,57,58,5,5,0,0,58,59,3,16,8,0,59,60,5,3,0,0,60,90,
        1,0,0,0,61,62,5,10,0,0,62,63,3,16,8,0,63,64,5,11,0,0,64,65,3,16,
        8,0,65,66,5,9,0,0,66,67,3,16,8,0,67,68,5,5,0,0,68,69,3,16,8,0,69,
        70,5,3,0,0,70,90,1,0,0,0,71,72,5,12,0,0,72,73,3,16,8,0,73,74,5,11,
        0,0,74,75,3,16,8,0,75,76,5,9,0,0,76,77,3,16,8,0,77,78,5,5,0,0,78,
        79,3,16,8,0,79,80,5,3,0,0,80,90,1,0,0,0,81,82,5,13,0,0,82,83,3,16,
        8,0,83,84,5,11,0,0,84,85,3,16,8,0,85,86,5,5,0,0,86,87,3,16,8,0,87,
        88,5,3,0,0,88,90,1,0,0,0,89,53,1,0,0,0,89,61,1,0,0,0,89,71,1,0,0,
        0,89,81,1,0,0,0,90,13,1,0,0,0,91,92,7,0,0,0,92,15,1,0,0,0,93,94,
        5,17,0,0,94,17,1,0,0,0,95,96,5,18,0,0,96,19,1,0,0,0,3,26,32,89
    ]

class LLMChainParser ( Parser ):

    grammarFileName = "LLMChain.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DEFINE'", "'AS'", "';'", "'LOAD'", "'INTO'", 
                     "'OUTPUT'", "'TO'", "'ANALYZE'", "'USING'", "'EXPAND'", 
                     "'WITH'", "'REFINE'", "'SUMMARIZE'", "'IMAGE'", "'PDF'", 
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
    RULE_type = 7
    RULE_name = 8
    RULE_string = 9

    ruleNames =  [ "start", "program", "statement", "defineStatement", "loadStatement", 
                   "outputStatement", "actionStatement", "type", "name", 
                   "string" ]

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
            self.state = 20
            self.program()
            self.state = 21
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
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.statement()
                self.state = 26 
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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.defineStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.loadStatement()
                pass
            elif token in [8, 10, 12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.actionStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
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
            self.state = 34
            self.match(LLMChainParser.T__0)
            self.state = 35
            self.name()
            self.state = 36
            self.match(LLMChainParser.T__1)
            self.state = 37
            self.string()
            self.state = 38
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
            self.state = 40
            self.match(LLMChainParser.T__3)
            self.state = 41
            self.type_()
            self.state = 42
            self.string()
            self.state = 43
            self.match(LLMChainParser.T__4)
            self.state = 44
            self.name()
            self.state = 45
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
            self.state = 47
            self.match(LLMChainParser.T__5)
            self.state = 48
            self.name()
            self.state = 49
            self.match(LLMChainParser.T__6)
            self.state = 50
            self.string()
            self.state = 51
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

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LLMChainParser.NameContext)
            else:
                return self.getTypedRuleContext(LLMChainParser.NameContext,i)


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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(LLMChainParser.T__7)
                self.state = 54
                self.name()
                self.state = 55
                self.match(LLMChainParser.T__8)
                self.state = 56
                self.name()
                self.state = 57
                self.match(LLMChainParser.T__4)
                self.state = 58
                self.name()
                self.state = 59
                self.match(LLMChainParser.T__2)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(LLMChainParser.T__9)
                self.state = 62
                self.name()
                self.state = 63
                self.match(LLMChainParser.T__10)
                self.state = 64
                self.name()
                self.state = 65
                self.match(LLMChainParser.T__8)
                self.state = 66
                self.name()
                self.state = 67
                self.match(LLMChainParser.T__4)
                self.state = 68
                self.name()
                self.state = 69
                self.match(LLMChainParser.T__2)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.match(LLMChainParser.T__11)
                self.state = 72
                self.name()
                self.state = 73
                self.match(LLMChainParser.T__10)
                self.state = 74
                self.name()
                self.state = 75
                self.match(LLMChainParser.T__8)
                self.state = 76
                self.name()
                self.state = 77
                self.match(LLMChainParser.T__4)
                self.state = 78
                self.name()
                self.state = 79
                self.match(LLMChainParser.T__2)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.match(LLMChainParser.T__12)
                self.state = 82
                self.name()
                self.state = 83
                self.match(LLMChainParser.T__10)
                self.state = 84
                self.name()
                self.state = 85
                self.match(LLMChainParser.T__4)
                self.state = 86
                self.name()
                self.state = 87
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
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
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
        self.enterRule(localctx, 16, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
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
        self.enterRule(localctx, 18, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LLMChainParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





