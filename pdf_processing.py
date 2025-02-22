# pdf_processing.py
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_images(pdf_path, output_folder="images"):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, img in enumerate(images):
        img_path = os.path.join(output_folder, f"page_{i+1}.png")
        img.save(img_path, "PNG")
        image_paths.append(img_path)
    return image_paths

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

def load_pdf(pdf_path):
    return fitz.open(pdf_path)