import pandas as pd

df = pd.read_csv("data/brawler_final_dataset.csv")

corr_cols = [
    "WinRate",
    "UseRate",
    "MetaScore",
    "Health",
    "ProjectileCount",
    "DamagePerProjectile",
    "TotalDamage",
    "SkillCeiling"
]

corr = df[corr_cols].corr()

print("Correlations with MetaScore:\n")

print(
    corr["MetaScore"].sort_values(ascending=False)
)

print("\nCorrelations with WinRate:\n")

print(corr["WinRate"].sort_values(ascending=False))
