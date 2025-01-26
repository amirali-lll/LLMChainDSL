# Generated from /Users/amirali/Programming/University/Compiler/LLMChainDSL/grammar/LLMChain.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LLMChainParser import LLMChainParser
else:
    from LLMChainParser import LLMChainParser

# This class defines a complete generic visitor for a parse tree produced by LLMChainParser.

class LLMChainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LLMChainParser#start.
    def visitStart(self, ctx:LLMChainParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#program.
    def visitProgram(self, ctx:LLMChainParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#statement.
    def visitStatement(self, ctx:LLMChainParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#defineStatement.
    def visitDefineStatement(self, ctx:LLMChainParser.DefineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#loadStatement.
    def visitLoadStatement(self, ctx:LLMChainParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#outputStatement.
    def visitOutputStatement(self, ctx:LLMChainParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#actionStatement.
    def visitActionStatement(self, ctx:LLMChainParser.ActionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#type.
    def visitType(self, ctx:LLMChainParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#name.
    def visitName(self, ctx:LLMChainParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLMChainParser#string.
    def visitString(self, ctx:LLMChainParser.StringContext):
        return self.visitChildren(ctx)



del LLMChainParser