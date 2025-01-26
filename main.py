from antlr4 import *
import argparse
from repository.post_order_ast_traverser import PostOrderASTTraverser
from repository.ast_to_networkx_graph import show_ast
from gen.LLMChainLexer import LLMChainLexer
from gen.LLMChainParser import LLMChainParser
from gen.LLMChainCodeGenerator import LLMChainCodeGenerator
from gen.LLMChainCustomListener import LLMChainCustomListener
from semantic.semantic_analyzer import SemanticAnalyzer


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')

    lexer = LLMChainLexer(stream)
    token_stream = CommonTokenStream(lexer)
    
    parser = LLMChainParser(token_stream)
    parse_tree = parser.program() 

    # Semantic Analysis
    analyzer = SemanticAnalyzer()
    try:
        analyzer.visit(parse_tree)
        print("Semantic analysis completed successfully!")
    except Exception as e:
        print(f"Semantic analysis failed: {e}")
        return

    # AST Generation
    ast_builder_listener = LLMChainCustomListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)
    ast = ast_builder_listener.ast
    # show_ast(ast.root)
    
    # Post Order AST Traversal
    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label','text','number']
    traversal = post_order_ast_traverser.traverse_ast(ast.root)
    traversal_labels = [item['label'] for item in traversal]
    print(traversal_labels)
    print(traversal[0])
    print(type(traversal_labels[0]))
    
    # Code Generation
    code_generator = LLMChainCodeGenerator()
    generated_code = code_generator.generate_code(traversal)
    
    with open(arguments.output, 'w') as f:
        f.write(generated_code)
    
    print(f"Code generation completed successfully! Output written to {arguments.output}")

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'dist/test.dsl')
	argparser.add_argument('-o', '--output', help='Output path', default=r'dist/test_output.py')
	args = argparser.parse_args()
	main(args)