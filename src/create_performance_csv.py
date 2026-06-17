import re
import pandas as pd
from pathlib import Path

raw_path = Path("data/raw_brawler_data.txt")
output_path = Path("data/brawler_performance.csv")

raw_text = raw_path.read_text(encoding="utf-8")

pattern = re.compile(
    r"(\d+)\s+(.+?) Icon\s+(.+?)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)"
)

rows = []

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

print(f"Created {output_path} with {len(df)} rows.")
print(df.head())