from gen.LLMChainVisitor import LLMChainVisitor
from .actions import checkAnalyzeOrSummarize, checkExpandOrRefine

class SemanticAnalyzer(LLMChainVisitor):
    def __init__(self):
        self.symbol_table = {}
    
    def visitDefineStatement(self, ctx):
        name = ctx.name().getText()  
        model_type = ctx.string().getText()
        if name in self.symbol_table:
            raise Exception(f"Model '{name}' is already defined.")
        self.symbol_table[name] = {"type": "MODEL", "model_type": model_type}
    
    def visitLoadStatement(self, ctx):
        input_type = ctx.getChild(1).getText()
        input_name = ctx.name().getText()  
        if input_name in self.symbol_table:
            raise Exception(f"Input '{input_name}' is already loaded.")
        self.symbol_table[input_name] = {"type": input_type}
    
# TODO: implement SemanticAnalyzer for 4 types of actions

    
    def visitOutputStatement(self, ctx):
        output_name = ctx.name().getText()
        if output_name not in self.symbol_table:
            raise Exception(f"Output '{output_name}' is not defined.")
