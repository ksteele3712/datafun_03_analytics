from pathlib import Path
from utils_logger import logger

from kristinesteele_process.kristinesteele_process_csv import process_csv_file
from kristinesteele_process.kristinesteele_process_excel import process_excel_file
from kristinesteele_process.kristinesteele_process_json import process_json_file
from kristinesteele_process.kristinesteele_process_text import process_text_file


def main():
    logger.info("Starting Kristine Steele's DataFun-03-Analytics Project")

    data_dir = Path("kristinesteele_data")
    processed_dir = Path("kristinesteele_processed")
    processed_dir.mkdir(exist_ok=True)

    # Process CSV
    process_csv_file()

    # Process Excel
    process_excel_file()

    # Process JSON
    process_json_file()

    # Process Text
    process_text_file()

    logger.info("All data processed and saved.")

if __name__ == "__main__":
    main()
