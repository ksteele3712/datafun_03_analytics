"""
Process an Excel file to count occurrences of 'GitHub' in a specific column and save the result.
"""

#####################################
# Import Modules
#####################################

import pathlib
import sys
import openpyxl

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR = "kristinesteele_data"
PROCESSED_DIR = "kristinesteele_processed"

#####################################
# Define Functions
#####################################

def count_goals_in_column(file_path: pathlib.Path, column: str, min_goals: int) -> int:
    """Count how many players scored at least min_goals in a specific column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column][1:]:  # Skip header
            try:
                if cell.value is not None and int(cell.value) >= min_goals:
                    count += 1
            except (ValueError, TypeError):
                continue
        return count
    except Exception as e:
        logger.error(f"Error processing Excel file: {e}")
        return 0

def process_excel_file():
    """Read womans_pro_stats.xlsx, count players with 3+ goals in column H, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "womans_pro_stats.xlsx")
    output_file = pathlib.Path(PROCESSED_DIR, "womans_pro_goals.txt")
    column_to_check = "H"
    min_goals = 3
    player_count = count_goals_in_column(input_file, column_to_check, min_goals)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Number of players with {min_goals} or more goals in column {column_to_check}: {player_count}\n")
    logger.info(f"Processed Excel file: {input_file}, Result saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")