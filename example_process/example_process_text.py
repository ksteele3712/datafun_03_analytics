"""
Process a text file to count words and save the result.
"""

#####################################
# Import Modules
#####################################

import pathlib
import sys

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

def process_text_file():
    """Read a text file, count words, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "romeo.txt")
    output_file = pathlib.Path(PROCESSED_DIR, "text_romeo_word_count.txt")
    try:
        with input_file.open('r', encoding='utf-8') as file:
            text = file.read()
        word_count = len(text.split())
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w', encoding='utf-8') as file:
            file.write(f"Word count: {word_count}\n")
        logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing text file: {e}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")
