"""
Processes a CSV file on how many flights during 1958, 1959 & 1960 were being
taken accordint to each month. Calculates min, max, mean, and stdev for each month.
"""

#####################################
# Import Modules
#####################################

import pathlib
import csv
import statistics
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

def analyze_monthly_data(file_path: pathlib.Path) -> dict:
    """Analyze each month column to calculate min, max, mean, and stdev."""
    try:
        with file_path.open('r') as file:
            dict_reader = csv.DictReader(file)
            months = [col for col in dict_reader.fieldnames if col != "Year"]
            stats = {}
            for month in months:
                values = []
                for row in dict_reader:
                    try:
                        value = int(row[month])
                        values.append(value)
                    except (ValueError, KeyError):
                        continue
                # Reset reader for next month
                file.seek(0)
                next(dict_reader)
                if values:
                    stats[month] = {
                        "min": min(values),
                        "max": max(values),
                        "mean": statistics.mean(values),
                        "stdev": statistics.stdev(values) if len(values) > 1 else 0,
                    }
            return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read the flight data CSV, analyze monthly columns, and save the results."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "flight_data.csv")
    output_file = pathlib.Path(PROCESSED_DIR, "flight_stats.txt")
    stats = analyze_monthly_data(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write("Flight Data Statistics (Monthly Passenger Counts):\n")
        if stats:
            for month, s in stats.items():
                file.write(f"\n{month} Statistics:\n")
                file.write(f"  Minimum: {s['min']:,}\n")
                file.write(f"  Maximum: {s['max']:,}\n")
                file.write(f"  Mean: {s['mean']:.2f}\n")
                file.write(f"  Standard Deviation: {s['stdev']:.2f}\n")
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