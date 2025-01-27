DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD PDF "manual.pdf" INTO manualText;
ANALYZE manualText USING multimodal_model INTO manualAnalysis;
SUMMARIZE manualAnalysis WITH text_model INTO manualSummary;
DEFINE technicalReview AS "technical review";
REFINE manualSummary WITH technicalReview USING text_model INTO finalManual;
OUTPUT finalManual TO "final_manual.txt";