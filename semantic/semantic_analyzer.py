from gen.LLMChainVisitor import LLMChainVisitor

class SemanticAnalyzer(LLMChainVisitor):
    def __init__(self):
        self.symbol_table = {}
    
    def visitDefineStatement(self, ctx):
        name = ctx.ID().getText()  
        model_type = ctx.STRING().getText()
        if name in self.symbol_table:
            raise Exception(f"Model '{name}' is already defined.")
        self.symbol_table[name] = {"type": "MODEL", "model_type": model_type}
    
    def visitLoadStatement(self, ctx):
        input_type = ctx.getChild(1).getText()
        input_name = ctx.ID().getText()  
        if input_name in self.symbol_table:
            raise Exception(f"Input '{input_name}' is already loaded.")
        self.symbol_table[input_name] = {"type": input_type}
    
    def visitActionStatement(self, ctx):
        action = ctx.getChild(0).getText()  
        input_name = ctx.ID(0).getText()  
        model_name = ctx.ID(1).getText()
        output_name = ctx.ID(2).getText()  
        
        # Validate input
        if input_name not in self.symbol_table:
            raise Exception(f"Input '{input_name}' is not defined.")
        
        # Validate model
        if model_name not in self.symbol_table or self.symbol_table[model_name]["type"] != "MODEL":
            raise Exception(f"Model '{model_name}' is not defined.")
        
        # Type compatibility check
        input_type = self.symbol_table[input_name]["type"]
        if action == "ANALYZE" and input_type != "IMAGE":
            raise Exception(f"ANALYZE requires an IMAGE, but got {input_type}.")
        if action in ["EXPAND", "REFINE"] and input_type not in ["TEXT", "PDF"]:
            raise Exception(f"{action} requires TEXT or PDF, but got {input_type}.")
        
        # Store output in symbol table
        self.symbol_table[output_name] = {"type": "TEXT"}  # Assume output is always TEXT for simplicity
    
    def visitOutputStatement(self, ctx):
        output_name = ctx.ID().getText()
        if output_name not in self.symbol_table:
            raise Exception(f"Output '{output_name}' is not defined.")

