# Generated from /Users/amirali/Programming/University/Compiler/LLMChainDSL/grammar/LLMChain.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LLMChainParser import LLMChainParser
else:
    from LLMChainParser import LLMChainParser

# This class defines a complete listener for a parse tree produced by LLMChainParser.
class LLMChainListener(ParseTreeListener):

    # Enter a parse tree produced by LLMChainParser#start.
    def enterStart(self, ctx:LLMChainParser.StartContext):
        pass

    # Exit a parse tree produced by LLMChainParser#start.
    def exitStart(self, ctx:LLMChainParser.StartContext):
        pass


    # Enter a parse tree produced by LLMChainParser#statement.
    def enterStatement(self, ctx:LLMChainParser.StatementContext):
        pass

    # Exit a parse tree produced by LLMChainParser#statement.
    def exitStatement(self, ctx:LLMChainParser.StatementContext):
        pass


    # Enter a parse tree produced by LLMChainParser#defineStatement.
    def enterDefineStatement(self, ctx:LLMChainParser.DefineStatementContext):
        pass

    # Exit a parse tree produced by LLMChainParser#defineStatement.
    def exitDefineStatement(self, ctx:LLMChainParser.DefineStatementContext):
        pass


    # Enter a parse tree produced by LLMChainParser#loadStatement.
    def enterLoadStatement(self, ctx:LLMChainParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by LLMChainParser#loadStatement.
    def exitLoadStatement(self, ctx:LLMChainParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by LLMChainParser#outputStatement.
    def enterOutputStatement(self, ctx:LLMChainParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by LLMChainParser#outputStatement.
    def exitOutputStatement(self, ctx:LLMChainParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by LLMChainParser#actionStatement.
    def enterActionStatement(self, ctx:LLMChainParser.ActionStatementContext):
        pass

    # Exit a parse tree produced by LLMChainParser#actionStatement.
    def exitActionStatement(self, ctx:LLMChainParser.ActionStatementContext):
        pass



del LLMChainParser