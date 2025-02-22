# PDF Extractor

## Overview
This project extracts text and tables from PDFs, supporting both digital and scanned documents. Extracted tables are converted to LaTeX format.

## Features
- Extracts text from digital PDFs
- Identifies and extracts tables, converting them into LaTeX format
- Supports OCR for scanned PDFs

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/anargh-t/PDF_Extractor.git
   cd pdf_extractor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Place your PDF file in the project folder and run:
```sh
python main.py
```
Modify `main.py` to specify the input PDF file.

## Dependencies
- PyMuPDF
- pytesseract
- pdf2image
- pdfplumber
- pandas

## License
MIT License
