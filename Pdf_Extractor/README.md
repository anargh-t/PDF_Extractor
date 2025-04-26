# PDF Extractor Web Application

A Flask-based web application for extracting text, tables, and performing OCR on PDF documents. The application can handle both digital PDFs and scanned documents.

## Features

- Extract text from digital PDFs
- Extract tables from PDFs and convert them to LaTeX format
- Perform OCR on scanned PDFs
- Modern web interface with drag-and-drop file upload
- Download extracted data in JSON format

## Prerequisites

- Python 3.7 or higher
- Tesseract OCR engine
- Poppler (for PDF to image conversion)

### Installing Tesseract OCR

#### Windows
1. Download the installer from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install and add the installation directory to your system PATH

#### Linux
```bash
sudo apt-get install tesseract-ocr
```

#### macOS
```bash
brew install tesseract
```

### Installing Poppler

#### Windows
1. Download from [http://blog.alivate.com.au/poppler-windows/](http://blog.alivate.com.au/poppler-windows/)
2. Extract and add the bin directory to your system PATH

#### Linux
```bash
sudo apt-get install poppler-utils
```

#### macOS
```bash
brew install poppler
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pdf-extractor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload a PDF file using the web interface:
   - Drag and drop a PDF file onto the upload area
   - Or click "Choose File" to select a file

4. The application will process the PDF and download a JSON file containing:
   - Extracted text
   - Tables in LaTeX format
   - OCR text from scanned pages

## Project Structure

- `app.py`: Flask application and routes
- `main.py`: Main processing logic
- `pdf_processing.py`: PDF processing utilities
- `text_extraction.py`: Text extraction functions
- `table_extraction.py`: Table extraction and LaTeX conversion
- `templates/`: HTML templates
- `uploads/`: Temporary storage for uploaded files
- `images/`: Temporary storage for extracted images

## License

This project is licensed under the MIT License - see the LICENSE file for details.
