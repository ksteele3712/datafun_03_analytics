"""
This example file fetches an Excel file from the web 
and saves it to a local file named feedback.xlsx in a folder named example_data.

Please save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import requests

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR = "example_data"

#####################################
# Define Functions
#####################################

def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """Fetch an Excel file from the web and save it locally."""
    response = requests.get(url)
    response.raise_for_status()
    write_excel_file(folder_name, filename, response.content)
    logger.info(f"Fetched Excel file from {url} and saved to {folder_name}/{filename}")

def write_excel_file(folder_name: str, filename: str, binary_data: bytes) -> None:
    """Write binary data to an Excel file in the specified folder."""
    folder = pathlib.Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / filename
    with file_path.open('wb') as file:
        file.write(binary_data)
    logger.info(f"Wrote Excel data to {file_path}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching Excel data.
    """
    excel_url = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/Feedback.xlsx'
    logger.info("Starting Excel fetch demonstration...")
    fetch_excel_file(FETCHED_DATA_DIR, "Feedback.xlsx", excel_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
