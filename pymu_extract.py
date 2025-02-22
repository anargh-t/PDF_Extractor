import fitz  # PyMuPDF

pdf_path = r"C:\Users\anarg\Downloads\sample.pdf"

def extract_text_with_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

pdf_text = extract_text_with_pymupdf(pdf_path)
print(pdf_text)
