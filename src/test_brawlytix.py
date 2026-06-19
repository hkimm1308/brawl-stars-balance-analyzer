import requests

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://brawlytix.com/meta-tracker"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

rows = soup.find_all("tr", attrs={"data-brawler-id": True})

brawler_data = []

for row in rows:
    cells = row.find_all("td")

    rank = int(cells[0].get_text(strip=True))

    name = cells[1].get_text(strip=True)

    win_rate = float(cells[2].get_text(strip=True))
    use_rate = float(cells[3].get_text(strip=True))
    meta_score = float(cells[4].get_text(strip=True))

    brawler_data.append({
        "Rank": rank,
        "Name": name,
        "WinRate": win_rate,
        "UseRate": use_rate,
        "MetaScore": meta_score
    })

df = pd.DataFrame(brawler_data)

print(df.head())
print(df.shape)

df.to_csv("data/brawler_performance_scraped.csv", index=False)