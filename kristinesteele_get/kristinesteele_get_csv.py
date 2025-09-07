"""
This example file fetches a CSV file from the web 
and saves it to a local file named usda_foundation_foods.csv in a folder named kristinesteele_data.

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

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """Write string data to a CSV file in the specified folder."""
    folder = pathlib.Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / filename
    with file_path.open('w', encoding='utf-8') as file:
        file.write(string_data)
    logger.info(f"Wrote CSV data to {file_path}")

def fetch_and_extract_usda_csv(folder_name: str, zip_filename: str, csv_filename: str, url: str) -> None:
    """Fetch the USDA Foundation Foods CSV zip file, extract the CSV, and save it locally."""
    import zipfile
    response = requests.get(url)
    response.raise_for_status()
    output_dir = pathlib.Path(folder_name)
    output_dir.mkdir(exist_ok=True)
    zip_path = output_dir / zip_filename
    with open(zip_path, "wb") as f:
        f.write(response.content)
    logger.info(f"Downloaded USDA Foundation Foods CSV zip to {zip_path}")
    # Extract CSV from zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.csv'):
                zip_ref.extract(file, output_dir)
                extracted_csv = output_dir / file
                extracted_csv.rename(output_dir / csv_filename)
                logger.info(f"Extracted CSV file to {output_dir / csv_filename}")
                break
        else:
            logger.error("No CSV file found in the zip archive.")

#####################################
# Define main() function
#####################################

def main():
    """Main function to fetch and extract USDA Foundation Foods CSV file."""
    # URL for USDA Foundation Foods CSV zip
    url = "https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_csv_2023-10-04.zip"
    folder_name = FETCHED_DATA_DIR
    zip_filename = "usda_foundation_foods.zip"
    csv_filename = "usda_foundation_foods.csv"
    fetch_and_extract_usda_csv(folder_name, zip_filename, csv_filename, url)
    logger.info(f"Fetched and extracted CSV file from {url} to {folder_name}/{csv_filename}")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()