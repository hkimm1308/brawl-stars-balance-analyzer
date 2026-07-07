import pandas as pd
import re

FEATURES_PATH = "data/brawler_features_v3_ml_ready.csv"
OLD_STATS_PATH = "data/brawler_final_dataset.csv"

features = pd.read_csv(FEATURES_PATH)
old_stats = pd.read_csv(OLD_STATS_PATH)

features["Name"] = features["Name"].str.strip()
old_stats["Name"] = old_stats["Name"].str.strip()

def parse_total_damage(value):
    value = str(value).strip()

    # Handles values like "3 x 1280"
    match = re.match(r"(\d+)\s*x\s*(\d+)", value)
    if match:
        count = int(match.group(1))
        damage = int(match.group(2))
        return count * damage

    # Handles simple values like "2200"
    try:
        return int(value)
    except ValueError:
        return None

core_stats = old_stats[[
    "Name",
    "Health",
    "Damage",
    "MovementSpeed",
    "RangeCategory",
    "Class"
]].copy()

core_stats = core_stats.drop_duplicates("Name")

core_stats["TotalDamage"] = core_stats["Damage"].apply(parse_total_damage)

fallback_rows = pd.DataFrame([
    {
        "Name": "Glowy",
        "Health": 6400,
        "Damage": "1900",
        "MovementSpeed": "Fast",
        "RangeCategory": "Long",
        "Class": "Controller",
        "TotalDamage": 1900,
    },
    {
        "Name": "Larry & Lawrie",
        "Health": 7600,
        "Damage": "1400",
        "MovementSpeed": "Normal",
        "RangeCategory": "Long",
        "Class": "Artillery",
        "TotalDamage": 1400,
    },
])

core_stats = pd.concat([core_stats, fallback_rows], ignore_index=True)

updated = features.merge(
    core_stats,
    on="Name",
    how="left"
)

front_cols = [
    "Name",
    "Rarity",
    "PrimaryRoleGroup",
    "PrimaryAttackCategory",
    "RangeClass",
    "Health",
    "Damage",
    "TotalDamage",
    "MovementSpeed",
    "RangeCategory",
    "Class",
]

remaining_cols = [col for col in updated.columns if col not in front_cols]
updated = updated[front_cols + remaining_cols]

updated.to_csv(FEATURES_PATH, index=False)

print("Core stats added to feature dataset.")
print(f"Rows: {len(updated)}")

for col in ["Health", "Damage", "TotalDamage", "MovementSpeed"]:
    missing = updated[updated[col].isna()]["Name"].tolist()
    print(f"\nMissing {col}:")
    print(missing if missing else "None")