# PDF Table Extractor
This Python script extracts tables from PDF documents and converts them to CSV format. It uses the Camelot library for accurate table extraction.

## Prerequisites
- Homebrew
- Python 3.x
- Pip (Python package installer)

## Setup
1. Clone the repository or download the script and associated files to your local machine.
2. Run the setup.sh script to install the necessary dependencies and set up your environment.
   
    ```./setup.sh```
       setup.sh will use brew to install system-level dependencies and pip to install Python packages from ```requirements.txt```
   
    

## Usage
Run the script from the terminal using the following command format:

```python extract.py <input_file_name.pdf> <output_file_name.csv> <start_page> <end_page> <header_0_1>```

### Arguments:

<input_file_name.pdf>: The path to the PDF from which you want to extract tables.

<output_file_name.csv>: The desired path for the output CSV file.

<start_page>: The first page number from the PDF to include in table extraction.

<end_page>: The last page number for table extraction (inclusive).
Make sure the provided start page is a positive number and the end page is greater than or equal to the start page.

<header_0_1>: Whether or not each page has a header. 1 if so, 0 if not.

## Example
To extract tables from pages 2 to 5 of example.pdf, without headers, and save them as output.csv, run:

```python extract.py example.pdf output.csv 2 5 0```
Upon successful extraction, the script will save the tables to output.csv and print a confirmation message.
