import requests
from pathlib import Path
import logging
# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)
file_handler = logging.FileHandler(log_folder / "project_log.log")
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Directory to save fetched data
FETCHED_DATA_DIR = "fetched_data"

def fetch_csv(output_dir, csv_filename, url):
    """Download CSV file from url and save to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / csv_filename
    response = requests.get(url)
    response.raise_for_status()
    with open(csv_path, "wb") as f:
        f.write(response.content)
    logger.info(f"Saved CSV file to {csv_path}")

def main():
    """Main function to fetch TSA daily travel numbers CSV file."""
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    folder_name = "kristinesteele_data"
    csv_filename = "flight_data.csv"
    fetch_csv(folder_name, csv_filename, url)
    logger.info(f"Fetched CSV file from {url} to {folder_name}/{csv_filename}")

if __name__ == "__main__":
    main()