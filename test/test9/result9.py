import os
import pdfplumber
from ollama import chat
import base64
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def query_ollama(model, query, encoded_image=None):
    messages = [{'role': 'user', 'content': query}]
    if encoded_image:
        messages.append({'role': 'user', 'content': '[IMAGE]', 'image': encoded_image})
    response = chat(model=model, messages=messages)
    return response.message.content
    

def extract_text_from_pdf(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text
    
multimodal_model = "llava"
text_model = "llama3.1"
reportText = extract_text_from_pdf("project_report.pdf")
reportSummary = query_ollama(text_model, f'Summarize this text:{reportText}')
additionalInsights = "additional insights"
expandedReport = query_ollama(text_model, f'Expand this text:{reportSummary} with context: {additionalInsights}')
with open("expanded_report.txt", 'w') as f:
	f.write(expandedReport)
