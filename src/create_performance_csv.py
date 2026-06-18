import re
import pandas as pd
from pathlib import Path

# This script reads raw brawler performance data from a text file, extracts relevant information using 
# regular expressions, and saves the cleaned data into a CSV file for further analysis.

# This saves the paths for the raw data and the output CSV file. The raw data is read from a text file, and 
# the output will be saved as a CSV file in the specified location.
raw_path = Path("data/raw_brawler_data.txt")
output_path = Path("data/brawler_performance.csv")

raw_text = raw_path.read_text(encoding="utf-8")

# Using Regex to recognize patterns in raw text and extract relevent data for each brawler, such as rank, name, 
# win rate, use rate, and meta score.
pattern = re.compile(
    r"(\d+)\s+(.+?) Icon\s+(.+?)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)"
)

rows = []

# The regex pattern looks for lines that match the format of the raw data, capturing the rank, name, 
# win rate, use rate, and meta score. 

# Each match is processed to extract these values, which are then stored in a list of dictionaries. 

# Finally, this list is converted into a DataFrame and saved as a CSV file.
for match in pattern.finditer(raw_text):
    rank = int(match.group(1))
    name = match.group(3).strip()
    win_rate = float(match.group(4))
    use_rate = float(match.group(5))
    meta_score = float(match.group(6))

    rows.append({
        "Rank": rank,
        "Name": name,
        "WinRate": win_rate,
        "UseRate": use_rate,
        "MetaScore": meta_score
    })

df = pd.DataFrame(rows)

df.to_csv(output_path, index=False)

# After creating the CSV file, the script prints a confirmation message along with the number of rows 
# in the DataFrame and a preview of the first few rows to verify that the data has been processed correctly.
print(f"Created {output_path} with {len(df)} rows.")
print(df.head())