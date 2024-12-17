# PDF to Excel Data Extraction Tool

This Python project automates the extraction, cleaning, and organization of tabular data from PDF files, converting them into Excel (.xlsx) format for easy analysis. It is ideal for scenarios where tables from PDF reports need to be quickly and efficiently processed.

## Features

- **Table Extraction:**
  Utilizes the `tabula` library to extract tables from specified PDF files, reading all pages and converting them into `pandas` DataFrame objects.

- **Data Consolidation and Cleaning:**
  - Combines extracted tables into a single DataFrame using `pd.concat()`.
  - Renames columns manually to reflect the expected fields, such as "Number of Users," "Revenue," "Total Expense," etc.

- **Output Directory Handling:**
  Ensures the specified output directory exists. If it doesn’t, it is created automatically using `os.makedirs()`.

- **Excel Export:**
  The consolidated DataFrame is exported to an Excel file (.xlsx) using `pandas`' `to_excel()` method, organizing the data for further analysis.

- **Status Messages:**
  Displays messages in the console to confirm successful creation and location of the Excel file.

## Requirements

- Python 3.7 or higher
- Required libraries:
  - `pandas`
  - `tabula`
  - `openpyxl`

Install the dependencies using pip:
```bash
pip install pandas tabula-py openpyxl
```

## How to Run the Project

1. **Set up the Environment:**
   Ensure Python and the required libraries are installed.

2. **Specify the Input PDF File:**
   Update the `pdf_file` variable in the code with the path to your PDF file:
   ```python
   pdf_file = r"C:/path/to/your/pdf_file.pdf"
   ```

3. **Run the Script:**
   Execute the Python script to extract, clean, and export the data:
   ```bash
   python script_name.py
   ```

4. **View the Output:**
   The processed data will be saved as an Excel file in the specified output directory:
   ```python
   output_dir = r"C:/path/to/output/directory"
   ```

5. **Customize Column Names:**
   Adjust the column names in the `colunas` list to match the structure of your PDF tables.


## Future Improvements

- Add automated column name detection to reduce manual adjustments.
- Enhance error handling for unsupported PDF structures.
- Introduce support for multiple output formats (e.g., CSV, JSON).
- Optimize performance for large PDF files.


