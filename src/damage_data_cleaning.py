import pandas as pd
import re

df = pd.read_csv("data/brawler_final_dataset.csv")

projectile_counts = []
damage_per_projectile = []
total_damage = []

for value in df["Damage"]:

    if pd.isna(value):
        projectile_counts.append(None)
        damage_per_projectile.append(None)
        total_damage.append(None)
        continue

    value = str(value).strip()

    match = re.match(r"(\d+)\s*x\s*(\d+)", value)

    if match:
        count = int(match.group(1))
        damage = int(match.group(2))

        projectile_counts.append(count)
        damage_per_projectile.append(damage)
        total_damage.append(count * damage)

    else:
        damage = int(float(value))

        projectile_counts.append(1)
        damage_per_projectile.append(damage)
        total_damage.append(damage)

df["ProjectileCount"] = projectile_counts
df["DamagePerProjectile"] = damage_per_projectile
df["TotalDamage"] = total_damage

int_cols = [
    "ProjectileCount",
    "DamagePerProjectile",
    "TotalDamage"
]

for col in int_cols:
    df[col] = df[col].astype("Int64")

df.to_csv(
    "data/brawler_final_dataset.csv",
    index=False
)

print("Updated final dataset saved.")