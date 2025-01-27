DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD IMAGE "../image.png" INTO img_input;
LOAD PDF "../document.pdf" INTO pdf_input;
LOAD TEXT "What is the significance of the event?" INTO query_text;

ANALYZE img_input USING multimodal_model INTO img_analysis;
EXPAND pdf_input WITH img_analysis USING text_model INTO expanded_info;
REFINE query_text WITH expanded_info USING text_model INTO final_result;
SUMMARIZE final_result WITH text_model INTO summary;

OUTPUT final_result TO "result1.txt";