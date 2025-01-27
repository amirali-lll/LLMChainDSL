from gen.LLMChainVisitor import LLMChainVisitor

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
        
    
    def visitOutputStatement(self, ctx):
        output_name = ctx.name().getText()
        if output_name not in self.symbol_table:
            raise Exception(f"Output '{output_name}' is not defined.")

    def visitAnalyzeStatement(self, ctx):
        input_name = ctx.getChild(1).getText()
        model_name = ctx.getChild(3).getText()
        output_name = ctx.getChild(5).getText()
        
        if input_name not in self.symbol_table:
            raise Exception(f"Input '{input_name}' is not defined.")
        if model_name not in self.symbol_table:
            raise Exception(f"Model '{model_name}' is not defined.")
        if output_name in self.symbol_table:
            raise Exception(f"Output '{output_name}' is already defined.")
        
        self.symbol_table[output_name] = {"type": "TEXT"}

    def visitSummarizeStatement(self, ctx):
        input_name = ctx.getChild(1).getText()
        model_name = ctx.getChild(3).getText()
        output_name = ctx.getChild(5).getText()
        
        if input_name not in self.symbol_table:
            raise Exception(f"Input '{input_name}' is not defined.")
        if model_name not in self.symbol_table:
            raise Exception(f"Model '{model_name}' is not defined.")
        if output_name in self.symbol_table:
            raise Exception(f"Output '{output_name}' is already defined.")
        
        self.symbol_table[output_name] = {"type": "TEXT"}

    def visitExpandStatement(self, ctx):
        input_name = ctx.getChild(1).getText()
        context_name = ctx.getChild(3).getText()
        model_name = ctx.getChild(5).getText()
        output_name = ctx.getChild(7).getText()
        
        if input_name not in self.symbol_table:
            raise Exception(f"Input '{input_name}' is not defined.")
        if context_name not in self.symbol_table:
            raise Exception(f"Context '{context_name}' is not defined.")
        if model_name not in self.symbol_table:
            raise Exception(f"Model '{model_name}' is not defined.")
        if output_name in self.symbol_table:
            raise Exception(f"Output '{output_name}' is already defined.")
        
        self.symbol_table[output_name] = {"type": "TEXT"}
        
    def visitRefineStatement(self, ctx):
        input_name = ctx.getChild(1).getText()
        context_name = ctx.getChild(3).getText()
        model_name = ctx.getChild(5).getText()
        output_name = ctx.getChild(7).getText()
        
        if input_name not in self.symbol_table:
            raise Exception(f"Input '{input_name}' is not defined.")
        if context_name not in self.symbol_table:
            raise Exception(f"Context '{context_name}' is not defined.")
        if model_name not in self.symbol_table:
            raise Exception(f"Model '{model_name}' is not defined.")
        if output_name in self.symbol_table:
            raise Exception(f"Output '{output_name}' is already defined.")
        
        self.symbol_table[output_name] = {"type": "TEXT"}
        