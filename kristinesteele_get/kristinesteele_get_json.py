"""
This example file fetches a JSON file from the web 
and saves it to a local file named forecast.json in a folder named kristinesteele_data.

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

FETCHED_DATA_DIR = "kristinesteele_data"

#####################################
# Define Functions
#####################################

def fetch_json_file(folder_name: str, filename: str, url: str) -> None:
    """Fetch a JSON file from the web and save it locally."""
    response = requests.get(url)
    response.raise_for_status()
    write_json_file(folder_name, filename, response.text)
    logger.info(f"Fetched JSON file from {url} and saved to {folder_name}/{filename}")

def write_json_file(folder_name: str, filename: str, string_data: str) -> None:
    """Write string data to a JSON file in the specified folder."""
    folder = pathlib.Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / filename
    with file_path.open('w', encoding='utf-8') as file:
        file.write(string_data)
    logger.info(f"Wrote JSON data to {file_path}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to fetch weather JSON data and save it locally.
    """
    json_url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
    logger.info("Fetching weather JSON data...")
    fetch_json_file(FETCHED_DATA_DIR, "forecast.json", json_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()