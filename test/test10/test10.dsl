DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD TEXT "Brief overview of the topic." INTO overviewText;
DEFINE detailedContext AS "detailed context";
EXPAND overviewText WITH detailedContext USING text_model INTO detailedOverview;
OUTPUT detailedOverview TO "detailed_overview.txt";