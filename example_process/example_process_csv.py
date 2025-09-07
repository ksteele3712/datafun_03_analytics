"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

import pathlib
import csv
import statistics
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

def analyze_ladder_score(file_path: pathlib.Path) -> dict:
    """Analyze the Ladder score column to calculate min, max, mean, and stdev."""
    try:
        score_list = []
        with file_path.open('r') as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                try:
                    score = float(row["Ladder score"])
                    score_list.append(score)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        stats = {
            "min": min(score_list),
            "max": max(score_list),
            "mean": statistics.mean(score_list),
            "stdev": statistics.stdev(score_list) if len(score_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "2020_happiness.csv")
    output_file = pathlib.Path(PROCESSED_DIR, "happiness_ladder_score_stats.txt")
    stats = analyze_ladder_score(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write("Ladder Score Statistics:\n")
        if stats:
            file.write(f"Minimum: {stats['min']:.2f}\n")
            file.write(f"Maximum: {stats['max']:.2f}\n")
            file.write(f"Mean: {stats['mean']:.2f}\n")
            file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
        else:
            file.write("No statistics available. Please check your input file.\n")
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
