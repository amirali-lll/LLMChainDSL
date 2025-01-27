DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD TEXT "Draft content for review." INTO draftContent;
DEFINE editorialSuggestions AS "editorial suggestions";
REFINE draftContent WITH editorialSuggestions USING text_model INTO refinedDraft;
OUTPUT refinedDraft TO "result4.txt";