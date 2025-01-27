DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD IMAGE "presentation_slide.png" INTO slideData;
ANALYZE slideData USING multimodal_model INTO slideAnalysis;
SUMMARIZE slideAnalysis WITH text_model INTO slideSummary;
OUTPUT slideSummary TO "slide_summary.txt";