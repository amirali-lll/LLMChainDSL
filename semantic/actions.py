def checkAnalyzeOrSummarize(ctx, action, symbol_table):
    input_data = ctx.name(0).getText() 
    model = ctx.name(1).getText()
    output_data = ctx.name(2).getText()

    # Check input_data validity
    if input_data not in symbol_table:
        raise Exception(f"Input variable '{input_data}' is not defined.")

    # Check model validity
    if model not in symbol_table:
        raise Exception(f"Model '{model}' is not defined.")
    if symbol_table[model]["type"] != "MODEL":
        raise Exception(f"'{model}' is not a valid model type for '{action}'.")

    # Register output_data
    if output_data in symbol_table:
        raise Exception(f"Output variable '{output_data}' is already defined.")
    symbol_table[output_data] = {"type": "TEXT"}


def checkExpandOrRefine(ctx, action, symbol_table):
    input_data = ctx.name(0).getText()  
    context_data = ctx.name(1).getText() 
    model = ctx.name(2).getText()       
    output_data = ctx.name(3).getText() 

    # Check input_data validity
    if input_data not in symbol_table:
        raise Exception(f"Input variable '{input_data}' is not defined.")

    # Check context_data validity
    if context_data not in symbol_table:
        raise Exception(f"Context variable '{context_data}' is not defined.")
    if symbol_table[context_data]["type"] != "TEXT":
        raise Exception(f"'{context_data}' is not a valid data type for '{action}'.")

    # Check model validity
    if model not in symbol_table:
        raise Exception(f"Model '{model}' is not defined.")
    if symbol_table[model]["type"] != "MODEL":
        raise Exception(f"'{model}' is not a valid model type for '{action}'.")

    # Register output_data
    if output_data in symbol_table:
        raise Exception(f"Output variable '{output_data}' is already defined.")
    symbol_table[output_data] = { "type": "TEXT" }
