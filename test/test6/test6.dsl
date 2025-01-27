DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD IMAGE "chart.png" INTO chartData;
ANALYZE chartData USING multimodal_model INTO chartAnalysis;
DEFINE clarificationNotes AS "clarification notes";
REFINE chartAnalysis WITH clarificationNotes USING text_model INTO clarifiedChart;
OUTPUT clarifiedChart TO "clarified_chart.txt";