#pip install transformers fitz


import fitz  # PyMuPDF
from transformers import pipeline

# Open the PDF file
pdf_document = "your_pdf_file.pdf"
pdf = fitz.open(pdf_document)

# Extract text from each page
text = ""
for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)
    text += page.get_text()

print("Extracted Text:\n", text[:1000])  # Print first 1000 characters of the extracted text

# You can use a Hugging Face model to analyze the text, e.g., summarization
summarizer = pipeline("summarization")

# Summarize the extracted text
summary = summarizer(text, max_length=200, min_length=30, do_sample=False)
print("Summary:\n", summary)
