import pandas as pd

MASTER_PATH = "data/master_dataset.csv"

df = pd.read_csv(MASTER_PATH)

required_columns = [
    "Name",
    "Rarity",
    "PrimaryRoleGroup",
    "PrimaryAttackCategory",
    "RangeClass",
    "EffectiveRangeTiles",
    "Health",
    "Damage",
    "AmmoCount",
    "ReloadSpeedClass",
    "ReloadSpeedScore",
    "AttackCooldownClass",
    "AttackCooldownScore",
    "ProjectileSpeedClass",
    "ProjectileSpeedScore",
    "ProjectileWidthClass",
    "ProjectileWidthScore",
    "BurstDamageClass",
    "BurstDamageScore",
    "SustainedDPSClass",
    "SustainedDPSScore",
    "SuperChargeRateClass",
    "SuperChargeRateScore",
    "SkillFloor",
    "SkillCeiling",
    "MechanicalDifficulty",
    "PositioningImportance",
    "DecisionComplexity",
    "SilverMetaScore",
    "GoldMetaScore",
    "DiamondMetaScore",
    "MythicMetaScore",
    "LegendaryMetaScore",
    "MastersMetaScore",
]

missing = [col for col in required_columns if col not in df.columns]

print("\n=== Master Dataset Column Check ===")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nMissing required columns:")
if missing:
    for col in missing:
        print(f"- {col}")
else:
    print("None")

print("\nAll columns:")
for col in df.columns:
    print(col)