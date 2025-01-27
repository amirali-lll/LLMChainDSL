DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD TEXT "Initial draft for analysis." INTO draftText;
ANALYZE draftText USING text_model INTO draftAnalysis;
DEFINE feedback AS "peer feedback";
REFINE draftAnalysis WITH feedback USING text_model INTO refinedDraft;
OUTPUT refinedDraft TO "refined_draft.txt";