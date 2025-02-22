import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from pdf2image import convert_from_path
import os

# Set Tesseract OCR path (Only needed for Windows)
# Change this path if Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# PDF file path
pdf_path = r"C:\Users\anarg\Downloads\Anurag.pdf"


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a scanned PDF using Tesseract OCR and stores it in a structured dictionary.
    """
    structured_data = {}

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    for page_num, img in enumerate(images):
        # Extract text from image using Tesseract
        text = pytesseract.image_to_string(img)

        # Store text in dictionary
        structured_data[f"Page_{page_num + 1}"] = text.strip()

    return structured_data


# Store extracted text in a variable
pdf_text_data = extract_text_from_pdf(pdf_path)


# Function to retrieve text from a specific page
def get_page_text(page_number):
    """
    Retrieves text from a specific page number.
    """
    return pdf_text_data.get(f"Page_{page_number}", "Page not found")


# Example Usage
print("Extracted Text Data (Structured Dictionary):")
print(pdf_text_data)  # Print all extracted text

# Retrieve text from Page 1
page_1_text = get_page_text(1)
print("\nText from Page 1:")
print(page_1_text)
