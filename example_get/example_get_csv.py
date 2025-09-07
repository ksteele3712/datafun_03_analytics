"""
This example file fetches a CSV file from the web 
and saves it to a local file named 2020_happiness.csv in a folder named example_data.

For best results, add the provided utils_logger.py file 
to the same folder as this file.
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

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """Fetch a CSV file from the web and save it locally."""
    response = requests.get(url)
    response.raise_for_status()
    write_csv_file(folder_name, filename, response.text)
    logger.info(f"Fetched CSV file from {url} and saved to {folder_name}/{filename}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """Write string data to a CSV file in the specified folder."""
    folder = pathlib.Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / filename
    with file_path.open('w', encoding='utf-8') as file:
        file.write(string_data)
    logger.info(f"Wrote CSV data to {file_path}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching CSV data.
    """
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    logger.info("Starting CSV fetch demonstration...")
    fetch_csv_file(FETCHED_DATA_DIR, "2020_happiness.csv", csv_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
