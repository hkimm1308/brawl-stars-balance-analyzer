# python src/data_collection/test_rank_scrape.py

import requests
from bs4 import BeautifulSoup

# First rank page to test
urls = [
    "https://brawlytix.com/meta-tracker",
    "https://brawlytix.com/meta-tracker/ranked/gold/overall",
    "https://brawlytix.com/meta-tracker/ranked/legendary/overall"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr", attrs={"data-brawler-id": True})

    print("\nURL:", url)
    print("Status:", response.status_code)
    print("Title:", soup.title.text if soup.title else "No title")
    print("Brawler rows found:", len(rows))