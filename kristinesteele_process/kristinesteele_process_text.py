"""
Process a text file to count words and save the result.
"""

#####################################
# Import Modules
#####################################

import pathlib
import sys
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

def process_text_file():
    """Read the Book of Revelation, count words, and save the result."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "revelation.txt")
    output_file = pathlib.Path(PROCESSED_DIR, "bible_revelation.txt")
    try:
        with input_file.open('r', encoding='utf-8') as file:
            text = file.read()
        word_count = len(text.split())
        # Count specific words (case-insensitive)
        words_to_count = ['jesus', 'death', 'life', 'love', 'hope', 'freedom', 'joy', 'satan', 'victory', 'crown']
        counts = {word: text.lower().count(word) for word in words_to_count}
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w', encoding='utf-8') as file:
            file.write(f"Book of Revelation - Total word count: {word_count}\n")
            for word in words_to_count:
                file.write(f"Count of '{word}': {counts[word]}\n")
        logger.info(f"Processed text file: {input_file}, word counts saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing text file: {e}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")