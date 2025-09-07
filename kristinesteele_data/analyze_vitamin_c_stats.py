
import zipfile
import csv
import pathlib
import statistics

# Unzip the USDA file to kristinesteele_data
zip_path = pathlib.Path("kristinesteele_data/usda_foundation_foods.zip")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("kristinesteele_data")

# Find the CSV file in kristinesteele_data
csv_files = list(pathlib.Path("kristinesteele_data").glob("*.csv"))
if not csv_files:
    print("No CSV file found after unzip.")
    exit(1)
csv_path = csv_files[0]

# Analyze Vitamin C (mg) column
vitamin_c_values = []
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        value = row.get('Vitamin C, total ascorbic acid (mg)')
        if value:
            try:
                vitamin_c_values.append(float(value))
            except ValueError:
                continue

stats_file = pathlib.Path("kristinesteele_data/vitaminc_stats.txt")
with open(stats_file, "w", encoding="utf-8") as f:
    if vitamin_c_values:
        f.write(f"Vitamin C stats for {csv_path.name}:\n")
        f.write(f"Min: {min(vitamin_c_values):.2f} mg\n")
        f.write(f"Max: {max(vitamin_c_values):.2f} mg\n")
        f.write(f"Mean: {statistics.mean(vitamin_c_values):.2f} mg\n")
        f.write(f"Std Dev: {statistics.stdev(vitamin_c_values):.2f} mg\n")
    else:
        f.write("No Vitamin C data found.\n")
