import sys
import pandas as pd
import camelot
import os


# USAGE:
# python extract.py input_filename output_filename start_page_num end_page_num header

# Set the environment variable for the dynamic linker
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/lib'

# Check for the correct number of arguments.
if len(sys.argv) != 6:
    print("Usage: python extract.py <input_file_name.pdf> <output_file_name.csv> start_page_num end_page_num header")
    sys.exit(1)

# The first argument passed to the script is the file name of the PDF.
pdf_file_name = sys.argv[1]
output_file_name = sys.argv[2]
start_page_num = int(sys.argv[3])
end_page_num = int(sys.argv[4])
header = bool(sys.argv[5])

if start_page_num > end_page_num:
    print("End page must be greater than or equal to start page")
    sys.exit(1)

if start_page_num < 0:
    print("Start page must be greater than zero")
    sys.exit(1)

# Use Camelot to read the PDF file.
waste_report = camelot.read_pdf(pdf_file_name, flavor='lattice', pages=(str(start_page_num) + '-' + str(end_page_num)))

# Convert the pages to DataFrames.
if header:
        
    table = waste_report[1].df

    if start_page_num != end_page_num:
        
        # skip header tables
        for i in range(3, (end_page_num - start_page_num + 1) * 2, 2):
            new_page = waste_report[i].df
            table = pd.concat([table, new_page])

else:
    table = waste_report[0].df

    if start_page_num != end_page_num:

        # iterate through each table
        for i in range(1, (end_page_num - start_page_num + 1)):
            new_page = waste_report[i].df
            table = pd.concat([table, new_page])


# Save the complete DataFrame to a CSV file.
print(table)

table.to_csv(output_file_name, index=False)
print(f"Table saved to '{output_file_name}'")