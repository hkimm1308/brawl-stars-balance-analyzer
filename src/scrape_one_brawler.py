import requests
from bs4 import BeautifulSoup

url = "https://brawlytix.com/brawlers/bolt"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(response.text, "html.parser")

hp = soup.find(id="brawler-hp-value")
damage = soup.find(id="brawler-damage-value")

speed_section = soup.find(id="brawler-speed")
range_section = soup.find(id="brawler-range")

speed = speed_section.find("strong").get_text(strip=True)
range_category = range_section.find("strong").get_text(strip=True)

print("HP:", hp["data-power11-value"])
print("Damage:", damage["data-power11-value"])
print("Movement Speed:", speed)
print("Range:", range_category)

meta_line = soup.find("div", class_="brawler-meta-line")
meta_pills = meta_line.find_all("span", class_="brawler-meta-pill")

rarity = meta_pills[0].get_text(strip=True)
brawler_class = meta_pills[1].get_text(strip=True)

print("Rarity:", rarity)
print("Class:", brawler_class)