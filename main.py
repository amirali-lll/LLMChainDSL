from antlr4 import *
import argparse
from gen.LLMChainLexer import LLMChainLexer
from gen.LLMChainParser import LLMChainParser
from semantic.semantic_analyzer import SemanticAnalyzer


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')

    lexer = LLMChainLexer(stream)
    token_stream = CommonTokenStream(lexer)
    
    parser = LLMChainParser(token_stream)
    tree = parser.start() 

    # Semantic Analysis
    analyzer = SemanticAnalyzer()
    try:
        analyzer.visit(tree)
        print("Semantic analysis completed successfully!")
    except Exception as e:
        print(f"Semantic analysis failed: {e}")
        return

    # AST Generation
    
    # Code Generation
    print("Code generation would start here.")

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'dist/test.dsl')
	argparser.add_argument('-o', '--output', help='Output path', default=r'dist/test_output.py')
	args = argparser.parse_args()
	main(args)