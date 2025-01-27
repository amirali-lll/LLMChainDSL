from repository.ast import AST
from repository.make_ast_subtree import make_ast_subtree
from gen.LLMChainListener import LLMChainListener



class LLMChainCustomListener(LLMChainListener):
    def __init__(self, rule_names):
        self.overridden_rules = [ 
            'defineStatement' ,
            'loadStatement',
            'analyzeStatement',
            'expandStatement',
            'summarizeStatement',
            'refineStatement',
            'outputStatement' ]
        self.rule_names = rule_names
        self.ast = AST()
    
    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)
    
        
    def exitDefineStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "define", keep_node=True)
        
    def exitLoadStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "load", keep_node=True)
        
    def exitOutputStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "output", keep_node=True)
        
    def exitAnalyzeStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "analyze", keep_node=True)
    
    def exitExpandStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "expand", keep_node=True)
    
    def exitSummarizeStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "summarize", keep_node=True)
    
    def exitRefineStatement(self, ctx):
        make_ast_subtree(self.ast, ctx, "refine", keep_node=True)
    
    