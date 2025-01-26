grammar LLMChain;

// PARSER RULES

start: statement+ EOF;

statement: defineStatement | loadStatement | actionStatement | outputStatement;

// STATEMENTS

defineStatement: 'DEFINE' ID 'AS' STRING ';';

loadStatement: 'LOAD' ( 'IMAGE' | 'PDF' | 'TEXT') STRING 'INTO' ID ';';

outputStatement: 'OUTPUT' ID 'TO' STRING ';';

actionStatement:
	'ANALYZE' ID 'USING' ID 'INTO' ID ';' |
	'EXPAND' ID 'WITH' ID 'USING' ID 'INTO' ID ';' |
	'REFINE' ID 'WITH' ID 'USING' ID 'INTO' ID ';' |
	'SUMMARIZE' ID 'WITH' ID 'INTO' ID ';';


// LEXER RULES

ID: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;