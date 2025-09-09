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

import pandas as pd
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


def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """Fetch an Excel file from the web and save it locally."""
    response = requests.get(url)
    response.raise_for_status()
    folder = pathlib.Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / filename
    with open(file_path, 'wb') as f:
        f.write(response.content)
    logger.info(f"Fetched Excel file from {url} and saved to {file_path}")


# No longer needed: write_excel_file

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to convert NWSL Women's Soccer League CSV to Excel in kristinesteele_data.
    """
    input_csv = 'kristinesteele_data/2024_nwsl_0525.csv'
    output_excel = 'kristinesteele_data/womans_pro_stats.xlsx'
    df = pd.read_csv(input_csv)
    df.to_excel(output_excel, index=False)
    logger.info(f"Converted {input_csv} to {output_excel}")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()