


# DataFun-03-Analytics

## Project Summary

Welcome to Kristine Steele's DataFun-03-Analytics project! This project is the heart of my learning journey in the Data Analytics Fundamentals course at Northwest Missouri State University. Here, I demonstrate how to fetch, process, and analyze real-world data using Python, focusing on practical skills and clear understanding.

### What is this project about?

The goal is to work with multiple types of data—CSV, Excel, JSON, and plain text—using Python scripts I wrote myself. I fetch data from public sources, process it to extract meaningful insights, and save the results for review. Each script is designed to teach and reinforce core data analytics concepts:

- **Fetching Data:** Downloading files from the web (airline flight data, soccer stats, weather forecasts, and the Book of Revelation).
- **Processing Data:** Using pandas and other libraries to clean, summarize, and analyze the data. For example, I count players with 3+ goals in soccer, calculate weather statistics, and analyze word counts in literature.
- **Saving Results:** All processed outputs are saved in a dedicated folder for easy access and review.

### Why is this important?

This project shows my ability to:
- Work independently with real datasets
- Apply Python for data wrangling and analysis
- Document my workflow for clarity and reproducibility
- Use version control (Git) to manage and submit my work

## How the Project Works

**Key Scripts:**
- `kristinesteele_get_csv.py` — Fetches airline flight data (CSV)
- `kristinesteele_get_excel.py` — Fetches soccer stats (CSV), converts to Excel
- `kristinesteele_get_json.py` — Fetches weather forecast (JSON)
- `kristinesteele_get_text.py` — Fetches Book of Revelation (TXT)
- `kristinesteele_process_excel.py` — Counts soccer players with 3+ goals
- `kristinesteele_process_json.py` — Summarizes weather statistics
- `kristinesteele_process_text.py` — Counts words and keywords in Revelation
- `utils_logger.py` — Shared logging utility

**Folders:**
- `kristinesteele_data/` — Raw data files
- `kristinesteele_processed/` — Processed results
- `logs/` — Execution logs

## How to Run

1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the fetch scripts to download data:
   ```powershell
   python kristinesteele_get\kristinesteele_get_csv.py
   python kristinesteele_get\kristinesteele_get_excel.py
   python kristinesteele_get\kristinesteele_get_json.py
   python kristinesteele_get\kristinesteele_get_text.py
   ```
3. Run the process scripts to analyze data:
   ```powershell
   python kristinesteele_process\kristinesteele_process_excel.py
   python kristinesteele_process\kristinesteele_process_json.py
   python kristinesteele_process\kristinesteele_process_text.py
   ```

## Data Sources

- **CSV:** [Airline Flight Data](https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv)
- **Excel:** [NWSL Soccer Stats](https://www.kaggle.com/datasets/)
- **JSON:** [Open-Meteo Weather Data](https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m)
- **Text:** [Book of Revelation (Bible)](https://www.gutenberg.org/cache/epub/10/pg10.txt)

## Output

- All processed results are saved in `kristinesteele_processed/`
- Logs are written to `logs/project_log.log`

## Learning Outcomes

Through this project, I learned how to:
- Use Python for data fetching and processing
- Work with multiple file formats
- Summarize and analyze real-world data
- Organize code and outputs for clarity
- Document my work for others to follow

---
**Author:** Kristine Steele
**Course:** Data Analytics Fundamentals
**Date:** September 9, 2025






