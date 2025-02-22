# text_extraction.py
import fitz

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    structured_text = {}
    for page_num, page in enumerate(doc, start=1):
        structured_text[f"Page {page_num}"] = page.get_text("text")
    return structured_text