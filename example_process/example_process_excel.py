"""
Process an Excel file to count occurrences of 'GitHub' in a specific column and save the result.
"""

#####################################
# Import Modules
#####################################

import pathlib
import sys
import openpyxl

sys.path.append(str(pathlib.Path(__file__).resolve().parent))
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR = "example_data"
PROCESSED_DIR = "example_processed"

#####################################
# Define Functions
#####################################

def count_word_in_column(file_path: pathlib.Path, column: str, word: str) -> int:
    """Count occurrences of a word in a specific column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column]:
            if cell.value and word in str(cell.value):
                count += 1
        return count
    except Exception as e:
        logger.error(f"Error processing Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of 'GitHub' in a specific column, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "Feedback.xlsx")
    output_file = pathlib.Path(PROCESSED_DIR, "excel_feedback_github_count.txt")
    column_to_check = "A"
    word_to_count = "GitHub"
    word_count = count_word_in_column(input_file, column_to_check, word_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}' in column {column_to_check}: {word_count}\n")
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")
