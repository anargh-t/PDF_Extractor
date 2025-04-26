# pdf_processing.py
import fitz  # PyMuPDF
import pytesseract
import pdfplumber
import pandas as pd
from pdf2image import convert_from_path
from PIL import Image
import os

#load pdf
def load_pdf(pdf_path):
    return fitz.open(pdf_path)

#extract text from pdf  
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    structured_text = {}
    for page_num, page in enumerate(doc, start=1):
        structured_text[f"Page {page_num}"] = page.get_text("text")
    return structured_text

#extract images from pdf
def extract_images(pdf_path, output_folder="images"):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, img in enumerate(images):
        img_path = os.path.join(output_folder, f"page_{i+1}.png")
        img.save(img_path, "PNG")
        image_paths.append(img_path)
    return image_paths

#extract text from images
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)


#extract tables from pdf
def extract_tables(pdf_path):
    tables_dict = {}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            if tables:
                tables_dict[f"Page {i+1}"] = [pd.DataFrame(table) for table in tables]
    return tables_dict

def convert_table_to_latex(dataframe):
    return dataframe.to_latex(index=False)