"""
Processes a JSON file to extract and save information about weather.
"""

#####################################
# Import Modules
#####################################

import pathlib
import sys
import json

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

def process_json_file():
    """Read the weather JSON file, extract hourly temperatures, and save summary statistics."""
    input_file = pathlib.Path(FETCHED_DATA_DIR, "forecast.json")
    output_file = pathlib.Path(PROCESSED_DIR, "weather_results.txt")
    try:
        with input_file.open('r', encoding='utf-8') as file:
            data = json.load(file)
        # Extract location and date range
        latitude = data.get('latitude', None)
        longitude = data.get('longitude', None)
        times = data.get('hourly', {}).get('time', [])
        temps = data.get('hourly', {}).get('temperature_2m', [])
        if temps:
            avg_temp = sum(temps) / len(temps)
            min_temp = min(temps)
            max_temp = max(temps)
        else:
            avg_temp = min_temp = max_temp = None
        # Prepare summary info
        location_str = f"Location: Latitude {latitude}, Longitude {longitude} (Tokyo, Japan)" if latitude == 35.0 and longitude == 139.0 else f"Location: Latitude {latitude}, Longitude {longitude}"
        date_range_str = f"Date Range: {times[0][:10]} to {times[-1][:10]}" if times else "Date Range: Unknown"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w', encoding='utf-8') as file:
            if temps:
                file.write(f"Weather Data Summary\n")
                file.write(location_str + "\n")
                file.write(date_range_str + "\n\n")
                file.write(f"Average Temperature: {avg_temp:.2f}°C\n")
                file.write(f"Minimum Temperature: {min_temp:.2f}°C\n")
                file.write(f"Maximum Temperature: {max_temp:.2f}°C\n")
                file.write(f"Total Hours: {len(temps)}\n")
            else:
                file.write("No temperature data found in the JSON file.\n")
        logger.info(f"Processed JSON file: {input_file}, Weather summary saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error processing JSON file: {e}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")