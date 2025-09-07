"""
This example file fetches a text file from the web 
and saves it to a local file named romeo.txt in a folder named example_data.

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
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR = "example_data"

#####################################
# Define Functions
#####################################

def fetch_txt_file(folder_name: str, filename: str, url: str) -> None:
    """Fetch a text file from the web and save it locally."""
    response = requests.get(url)
    response.raise_for_status()
    write_txt_file(folder_name, filename, response.text)
    logger.info(f"Fetched text file from {url} and saved to {folder_name}/{filename}")

def write_txt_file(folder_name: str, filename: str, string_data: str) -> None:
    """Write string data to a text file in the specified folder."""
    folder = pathlib.Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / filename
    with file_path.open('w', encoding='utf-8') as file:
        file.write(string_data)
    logger.info(f"Wrote text data to {file_path}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching text data.
    """
    txt_url = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/romeo.txt'
    logger.info("Starting text fetch demonstration...")
    fetch_txt_file(FETCHED_DATA_DIR, "romeo.txt", txt_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
