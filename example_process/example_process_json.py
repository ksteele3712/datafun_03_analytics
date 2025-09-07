"""
Process a JSON file to extract and save information about astronauts.
"""

#####################################
# Import Modules
#####################################

import pathlib
import sys
import json

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

def process_json_file():
    """Read a JSON file, extract astronaut names, and save the results."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "astros.json")
    output_file = pathlib.Path(PROCESSED_DIR, "json_astronauts_by_craft.txt")
    try:
        with input_file.open('r', encoding='utf-8') as file:
            data = json.load(file)
        craft_dict = {}
        for person in data.get('people', []):
            craft = person.get('craft', 'Unknown')
            name = person.get('name', 'Unknown')
            craft_dict.setdefault(craft, []).append(name)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w', encoding='utf-8') as file:
            for craft, names in craft_dict.items():
                file.write(f"{craft}: {', '.join(names)}\n")
        logger.info(f"Processed JSON file: {input_file}, Astronauts by craft saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing JSON file: {e}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
