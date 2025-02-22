import pdfplumber
import pandas as pd

# Path to the PDF file
pdf_path = r"C:\Users\anarg\Downloads\S3 Time Table Dec 2024.pdf"


# Function to extract tables from the PDF
def extract_tables_from_pdf(pdf_path):
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_table()
            if tables:
                df = pd.DataFrame(tables[1:], columns=tables[0])  # Convert to DataFrame
                all_tables.append(df)

    return all_tables


# Extract tables
tables = extract_tables_from_pdf(pdf_path)

# Display extracted tables
for i, table in enumerate(tables):
    print(f"🔹 Table {i + 1}:\n", table, "\n")

# Store the first table in a structured variable for analysis
if tables:
    df_main = tables[0]  # Taking the first table as an example
    print("✅ Table stored for analysis!")

# Save table to an Excel file (optional)
df_main.to_excel("extracted_table.xlsx", index=False)
