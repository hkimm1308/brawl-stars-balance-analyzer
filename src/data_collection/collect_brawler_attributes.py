import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Base website URLs
BASE_URL = "https://brawlytix.com"
META_URL = "https://brawlytix.com/meta-tracker"

# Download the meta tracker page
response = requests.get(META_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Find all rows in the brawler rankings table
rows = soup.find_all("tr", attrs={"data-brawler-id": True})

brawler_links = []

# Extract every brawler name and profile URL
for row in rows:
    link = row.find("a", class_="brawler-link")

    name = link.get_text(strip=True)
    href = link["href"]
    full_url = BASE_URL + href

    brawler_links.append({
        "Name": name,
        "URL": full_url
    })

print("Brawlers found:", len(brawler_links))
print(brawler_links[:5])

attribute_data = []

# Visit each brawler page and collect attributes
for brawler in brawler_links:

    name = brawler["Name"]
    url = brawler["URL"]

    print("Scraping:", name)

    try:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Core stats
        hp = soup.find(id="brawler-hp-value")
        damage = soup.find(id="brawler-damage-value")

        # Range and movement speed sections
        speed_section = soup.find(id="brawler-speed")
        range_section = soup.find(id="brawler-range")

        # Rarity and class are stored as pills
        meta_line = soup.find("div", class_="brawler-meta-line")
        meta_pills = meta_line.find_all(
            "span",
            class_="brawler-meta-pill"
        )

        rarity = meta_pills[0].get_text(strip=True)
        brawler_class = meta_pills[1].get_text(strip=True)

        # Extract displayed values
        speed = speed_section.find("strong").get_text(strip=True)
        range_category = range_section.find("strong").get_text(strip=True)

        # Store all collected attributes
        attribute_data.append({
            "Name": name,
            "Health": int(hp["data-power11-value"]),
            "Damage": damage.get_text(strip=True),
            "MovementSpeed": speed,
            "RangeCategory": range_category,
            "Rarity": rarity,
            "Class": brawler_class
        })

    except Exception as e:
        print(f"Failed on {name}: {e}")

    # Small delay so we don't spam the website
    time.sleep(0.5)

# Convert to DataFrame
df = pd.DataFrame(attribute_data)

print(df.head())
print(df.shape)

# Save scraped data
df.to_csv(
    "data/brawler_attributes_scraped.csv",
    index=False
)