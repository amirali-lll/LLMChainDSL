# Generated from /Users/amirali/Programming/University/Compiler/LLMChainDSL/grammar/LLMChain.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,20,165,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,5,16,134,8,16,10,16,12,16,137,9,16,1,
        17,1,17,5,17,141,8,17,10,17,12,17,144,9,17,1,17,1,17,1,18,4,18,149,
        8,18,11,18,12,18,150,1,18,1,18,1,19,1,19,1,19,1,19,5,19,159,8,19,
        10,19,12,19,162,9,19,1,19,1,19,1,142,0,20,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,1,0,4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,
        95,97,122,3,0,9,10,13,13,32,32,2,0,10,10,13,13,168,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,
        1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,1,41,1,0,0,0,3,48,
        1,0,0,0,5,51,1,0,0,0,7,53,1,0,0,0,9,58,1,0,0,0,11,64,1,0,0,0,13,
        68,1,0,0,0,15,73,1,0,0,0,17,78,1,0,0,0,19,85,1,0,0,0,21,88,1,0,0,
        0,23,96,1,0,0,0,25,102,1,0,0,0,27,109,1,0,0,0,29,114,1,0,0,0,31,
        121,1,0,0,0,33,131,1,0,0,0,35,138,1,0,0,0,37,148,1,0,0,0,39,154,
        1,0,0,0,41,42,5,68,0,0,42,43,5,69,0,0,43,44,5,70,0,0,44,45,5,73,
        0,0,45,46,5,78,0,0,46,47,5,69,0,0,47,2,1,0,0,0,48,49,5,65,0,0,49,
        50,5,83,0,0,50,4,1,0,0,0,51,52,5,59,0,0,52,6,1,0,0,0,53,54,5,76,
        0,0,54,55,5,79,0,0,55,56,5,65,0,0,56,57,5,68,0,0,57,8,1,0,0,0,58,
        59,5,73,0,0,59,60,5,77,0,0,60,61,5,65,0,0,61,62,5,71,0,0,62,63,5,
        69,0,0,63,10,1,0,0,0,64,65,5,80,0,0,65,66,5,68,0,0,66,67,5,70,0,
        0,67,12,1,0,0,0,68,69,5,84,0,0,69,70,5,69,0,0,70,71,5,88,0,0,71,
        72,5,84,0,0,72,14,1,0,0,0,73,74,5,73,0,0,74,75,5,78,0,0,75,76,5,
        84,0,0,76,77,5,79,0,0,77,16,1,0,0,0,78,79,5,79,0,0,79,80,5,85,0,
        0,80,81,5,84,0,0,81,82,5,80,0,0,82,83,5,85,0,0,83,84,5,84,0,0,84,
        18,1,0,0,0,85,86,5,84,0,0,86,87,5,79,0,0,87,20,1,0,0,0,88,89,5,65,
        0,0,89,90,5,78,0,0,90,91,5,65,0,0,91,92,5,76,0,0,92,93,5,89,0,0,
        93,94,5,90,0,0,94,95,5,69,0,0,95,22,1,0,0,0,96,97,5,85,0,0,97,98,
        5,83,0,0,98,99,5,73,0,0,99,100,5,78,0,0,100,101,5,71,0,0,101,24,
        1,0,0,0,102,103,5,69,0,0,103,104,5,88,0,0,104,105,5,80,0,0,105,106,
        5,65,0,0,106,107,5,78,0,0,107,108,5,68,0,0,108,26,1,0,0,0,109,110,
        5,87,0,0,110,111,5,73,0,0,111,112,5,84,0,0,112,113,5,72,0,0,113,
        28,1,0,0,0,114,115,5,82,0,0,115,116,5,69,0,0,116,117,5,70,0,0,117,
        118,5,73,0,0,118,119,5,78,0,0,119,120,5,69,0,0,120,30,1,0,0,0,121,
        122,5,83,0,0,122,123,5,85,0,0,123,124,5,77,0,0,124,125,5,77,0,0,
        125,126,5,65,0,0,126,127,5,82,0,0,127,128,5,73,0,0,128,129,5,90,
        0,0,129,130,5,69,0,0,130,32,1,0,0,0,131,135,7,0,0,0,132,134,7,1,
        0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,
        0,0,136,34,1,0,0,0,137,135,1,0,0,0,138,142,5,34,0,0,139,141,9,0,
        0,0,140,139,1,0,0,0,141,144,1,0,0,0,142,143,1,0,0,0,142,140,1,0,
        0,0,143,145,1,0,0,0,144,142,1,0,0,0,145,146,5,34,0,0,146,36,1,0,
        0,0,147,149,7,2,0,0,148,147,1,0,0,0,149,150,1,0,0,0,150,148,1,0,
        0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,6,18,0,0,153,38,1,0,
        0,0,154,155,5,47,0,0,155,156,5,47,0,0,156,160,1,0,0,0,157,159,8,
        3,0,0,158,157,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,
        0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,164,6,19,0,0,164,40,1,
        0,0,0,5,0,135,142,150,160,1,6,0,0
    ]

class LLMChainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    ID = 17
    STRING = 18
    WS = 19
    COMMENT = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'DEFINE'", "'AS'", "';'", "'LOAD'", "'IMAGE'", "'PDF'", "'TEXT'", 
            "'INTO'", "'OUTPUT'", "'TO'", "'ANALYZE'", "'USING'", "'EXPAND'", 
            "'WITH'", "'REFINE'", "'SUMMARIZE'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "ID", "STRING", "WS", "COMMENT" ]

    grammarFileName = "LLMChain.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


