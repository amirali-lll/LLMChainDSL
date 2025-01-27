DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD TEXT "Complex sentence needing expansion." INTO complexSentence;
DEFINE contextualDetails AS "contextual details";
EXPAND complexSentence WITH contextualDetails USING text_model INTO expandedSentence;
ANALYZE expandedSentence USING multimodal_model INTO sentenceAnalysis;
OUTPUT sentenceAnalysis TO "sentence_analysis.txt";