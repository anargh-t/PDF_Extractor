# main.py
from pdf_processing import load_pdf, extract_images, extract_text_from_image
from text_extraction import extract_text
from table_extraction import extract_tables, convert_table_to_latex


def main(pdf_path):
    print("Extracting text...")
    text_data = extract_text(pdf_path)

    print("Extracting tables...")
    tables = extract_tables(pdf_path)
    latex_tables = {page: [convert_table_to_latex(df) for df in tables[page]] for page in tables}

    print("Processing scanned PDFs...")
    image_paths = extract_images(pdf_path)
    ocr_text = {img: extract_text_from_image(img) for img in image_paths}

    return {
        "text": text_data,
        "tables": latex_tables,
        "ocr_text": ocr_text
    }


if __name__ == "__main__":
    pdf_file = r"C:\Users\anarg\Downloads\doc2.pdf"  # Replace with your PDF file
    extracted_data = main(pdf_file)
    print(extracted_data)
