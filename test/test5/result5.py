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
manualText = extract_text_from_pdf("manual.pdf")
manualAnalysis = query_ollama(multimodal_model, 'Analyze the content of the image', manualText)
manualSummary = query_ollama(text_model, f'Summarize this text:{manualAnalysis}')
technicalReview = "technical review"
finalManual = query_ollama(text_model, f'Refine this text:{manualSummary} with context: {technicalReview}')
with open("final_manual.txt", 'w') as f:
	f.write(finalManual)
