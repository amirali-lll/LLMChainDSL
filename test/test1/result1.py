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

with open("../image.png", 'rb') as image_file:
    img_input = base64.b64encode(image_file.read()).decode('utf-8')
        
pdf_input = extract_text_from_pdf("../document.pdf")
query_text = '"What is the significance of the event?"'
img_analysis = query_ollama(multimodal_model, 'Analyze the content of the image', img_input)
expanded_info = query_ollama(text_model, f'Expand this text:{pdf_input} with context: {img_analysis}')
final_result = query_ollama(text_model, f'Refine this text:{query_text} with context: {expanded_info}')
summary = query_ollama(text_model, f'Summarize this text:{final_result}')
with open("final_result.txt", 'w') as f:
	f.write(final_result)
