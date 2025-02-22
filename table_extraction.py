# table_extraction.py
import pdfplumber
import pandas as pd

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
