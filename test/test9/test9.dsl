DEFINE multimodal_model AS "llava";
DEFINE text_model AS "llama3.1";

LOAD PDF "project_report.pdf" INTO reportText;
SUMMARIZE reportText WITH text_model INTO reportSummary;
DEFINE additionalInsights AS "additional insights";
EXPAND reportSummary WITH additionalInsights USING text_model INTO expandedReport;
OUTPUT expandedReport TO "expanded_report.txt";