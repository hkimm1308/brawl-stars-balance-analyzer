import requests

url = "https://brawlytix.com/brawlers/bolt"

response = requests.get(url)
html = response.text

print("Status code:", response.status_code)
print("HTML length:", len(html))

terms = ["Damage", "Range", "Movement", "Hitpoints", "Reload Speed"]

for term in terms:
    print("\n" + "=" * 80)
    print("TERM:", term)

    index = html.find(term)

    print("Index:", index)

    if index != -1:
        print(html[index - 1000:index + 2000])