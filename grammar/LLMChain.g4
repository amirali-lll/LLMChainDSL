grammar LLMChain;

// PARSER RULES

start: program EOF;

program: statement+;

statement: defineStatement | loadStatement | actionStatement | outputStatement;

// STATEMENTS

defineStatement: 'DEFINE' name 'AS' string ';';

loadStatement: 'LOAD' type string 'INTO' name ';';

outputStatement: 'OUTPUT' name 'TO' string ';';

actionStatement:
	analyzeStatement |
	expandStatement |
	summarizeStatement |
	refineStatement;

analyzeStatement: 'ANALYZE' name 'USING' name 'INTO' name ';';
summarizeStatement: 'SUMMARIZE' name 'WITH' name 'INTO' name ';';
expandStatement: 'EXPAND' name 'WITH' name 'USING' name 'INTO' name ';';
refineStatement: 'REFINE' name 'WITH' name 'USING' name 'INTO' name ';';


type: 'IMAGE' | 'PDF' | 'TEXT';
name: ID;
string: STRING;

// LEXER RULES

ID: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;