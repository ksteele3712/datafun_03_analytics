import requests
import pathlib

# URL for USDA Foundation Foods CSV (large file)
url = "https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_csv_2023-10-04.zip"
output_dir = pathlib.Path("example_data")
output_dir.mkdir(exist_ok=True)
output_file = output_dir / "usda_foundation_foods.zip"

print(f"Downloading USDA Foundation Foods CSV from {url}...")
response = requests.get(url)
with open(output_file, "wb") as f:
    f.write(response.content)
print(f"Saved to {output_file}")

# You can unzip and process the CSV file after download.
