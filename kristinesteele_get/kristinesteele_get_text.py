"""
This example file fetches a text file from the web 
and saves it to a local file named bible_revelation.txt in a folder named kristinesteele_data.

It also counts specific words in the text and logs the results.
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
    Main function to fetch the Book of Revelation and save it locally.
    """
    # Project Gutenberg Bible (KJV) full text
    txt_url = 'https://www.gutenberg.org/cache/epub/10/pg10.txt'
    logger.info("Fetching Book of Revelation from Project Gutenberg...")
    response = requests.get(txt_url)
    response.raise_for_status()
    # Extract only the Book of Revelation
    start_marker = "The Revelation of Saint John the Divine"
    end_marker = "End of the Project Gutenberg EBook of The King James Version of the Bible"
    text = response.text
    start_idx = text.find(start_marker)
    end_idx = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
    revelation_text = text[start_idx:end_idx].strip() if start_idx != -1 and end_idx != -1 else text[start_idx:].strip()
    write_txt_file(FETCHED_DATA_DIR, "revelation.txt", revelation_text)
    logger.info(f"Fetched Book of Revelation and saved to {FETCHED_DATA_DIR}/revelation.txt")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()