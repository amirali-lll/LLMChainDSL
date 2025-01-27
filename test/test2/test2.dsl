DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD IMAGE "../image.png" INTO imageInput;
ANALYZE imageInput USING multimodal_model INTO imageAnalysis;
SUMMARIZE imageAnalysis WITH text_model INTO imageSummary;
OUTPUT imageSummary TO "result2.txt";