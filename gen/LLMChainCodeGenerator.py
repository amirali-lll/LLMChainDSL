from gen.FunctionsBody import functions


class LLMChainCodeGenerator:
    
    def __init__(self):
        self.non_operands  = ['define', 'load', 'output',
                              'analyze', 'expand', 'summarize', 'refine']
        self.operand_stack = []
        self.code = []

    
    def is_operand(self, item):
        return item not in self.non_operands
    
    def generate_code(self, traversal):
        # Imports
        self.code.append("import os")
        self.code.append("import pdfplumber")
        self.code.append("from ollama import chat")
        self.code.append("import base64")
        
        # Add BASE_DIR
        self.code.append("BASE_DIR = os.path.dirname(os.path.abspath(__file__))")
        
        # Functions
        self.code.extend(functions)
        
        for item in traversal:
            if self.is_operand(item['label']):
                self.operand_stack.append(item['label'])
            else:
                self.code.append(self.generate_code_for_non_operand(item['label']))
        
        
        result = ''
        for line in self.code:
            result += line + '\n'
        
        return result
    
    
    def generate_code_for_non_operand(self, item):
        if item == 'define':
            return self.generate_code_for_define()
        elif item == 'load':
            return self.generate_code_for_load()
        elif item == 'output':
            return self.generate_code_for_output()
        elif item == 'analyze':
            return self.generate_code_for_analyze()
        elif item == 'summarize':
            return self.generate_code_for_summarize()
        elif item == 'expand':
            return self.generate_code_for_expand()
        elif item == 'refine':
            return self.generate_code_for_refine()
        
    def generate_code_for_output(self):
        path = self.operand_stack.pop()
        variable = self.operand_stack.pop()
        
        return f"with open('{path}', 'w') as f:\n\tf.write({variable})"
    
    def generate_code_for_load(self):
        variable = self.operand_stack.pop()
        path_or_text = self.operand_stack.pop()
        type = self.operand_stack.pop()
        
        if type == 'TEXT':
            return f"{variable} = '{path_or_text}'"
        elif type == 'PDF':
            return f"{variable} = extract_text_from_pdf({path_or_text})"
        elif type == 'IMAGE':
            # we keep the image full path in the variable
            
            return f"""
with open({path_or_text}, 'rb') as image_file:
    {variable} = base64.b64encode(image_file.read()).decode('utf-8')
        """
        else:
            raise Exception(f"Unsupported data type '{type}'")
        
    def generate_code_for_define(self):
        model_id = self.operand_stack.pop()
        variable = self.operand_stack.pop()
        
        # simply just assign the model_id to the variable
        return f"{variable} = {model_id}"
    
    def generate_code_for_analyze(self):
        output = self.operand_stack.pop()
        model = self.operand_stack.pop()
        input = self.operand_stack.pop()
        
        return f"{output} = query_ollama({model}, 'Analyze the content of the image', {input})"
    
    def generate_code_for_summarize(self):
        output = self.operand_stack.pop()
        model = self.operand_stack.pop()
        input = self.operand_stack.pop()
        
        return f"{output} = query_ollama({model}, f'Summarize this text:" + '{' + input + "}')"
    
    def generate_code_for_expand(self):
        output = self.operand_stack.pop()
        model = self.operand_stack.pop()
        context = self.operand_stack.pop()
        input = self.operand_stack.pop()
        
        return f"{output} = query_ollama({model}, f'Expand this text:"+ '{' + input + '} with context: {'+ context + "}')"
        

    
    def generate_code_for_refine(self):
        output = self.operand_stack.pop()
        model = self.operand_stack.pop()
        context = self.operand_stack.pop()
        input = self.operand_stack.pop()
        
        return f"{output} = query_ollama({model}, f'Refine this text:" + '{' + input + '} with context: {'+ context + "}')"
        



        
        
        


            
    
        