import pandas as pd

PERFORMANCE_PATH = "data/performance_by_rank.csv"
FEATURES_PATH = "data/brawler_features_v3_ml_ready.csv"
OUTPUT_PATH = "data/master_dataset.csv"

performance = pd.read_csv(PERFORMANCE_PATH)
features = pd.read_csv(FEATURES_PATH)

# Clean name spacing
performance["Name"] = performance["Name"].str.strip()
features["Name"] = features["Name"].str.strip()

# Pivot rank data from long format to wide format
wide_performance = performance.pivot(
    index="Name",
    columns="RankTier",
    values=["WinRate", "UseRate", "MetaScore"]
)

# Flatten column names
wide_performance.columns = [
    f"{rank}{metric}"
    for metric, rank in wide_performance.columns
]

wide_performance = wide_performance.reset_index()

# Merge features with rank performance
master = features.merge(
    wide_performance,
    on="Name",
    how="inner"
)

# Optional: sort by name
master = master.sort_values("Name")

# -----------------------------
# Average Metrics Across Ranks
# -----------------------------

meta_cols = [
    "SilverMetaScore",
    "GoldMetaScore",
    "DiamondMetaScore",
    "MythicMetaScore",
    "LegendaryMetaScore",
    "MastersMetaScore",
]

win_cols = [
    "SilverWinRate",
    "GoldWinRate",
    "DiamondWinRate",
    "MythicWinRate",
    "LegendaryWinRate",
    "MastersWinRate",
]

use_cols = [
    "SilverUseRate",
    "GoldUseRate",
    "DiamondUseRate",
    "MythicUseRate",
    "LegendaryUseRate",
    "MastersUseRate",
]

master["AverageMetaScore"] = master[meta_cols].mean(axis=1)
master["AverageWinRate"] = master[win_cols].mean(axis=1)
master["AverageUseRate"] = master[use_cols].mean(axis=1)

# -----------------------------
# Standard Deviations
# -----------------------------

master["MetaScoreStdDev"] = master[meta_cols].std(axis=1)
master["WinRateStdDev"] = master[win_cols].std(axis=1)
master["UseRateStdDev"] = master[use_cols].std(axis=1)

# -----------------------------
# Ranges
# -----------------------------

master["MetaScoreRange"] = (
    master[meta_cols].max(axis=1)
    - master[meta_cols].min(axis=1)
)

master["WinRateRange"] = (
    master[win_cols].max(axis=1)
    - master[win_cols].min(axis=1)
)

master["UseRateRange"] = (
    master[use_cols].max(axis=1)
    - master[use_cols].min(axis=1)
)

# -----------------------------
# Skill Scaling Metrics
# -----------------------------

master["MetaScoreScaling"] = (
    master["MastersMetaScore"]
    - master["SilverMetaScore"]
)

master["WinRateScaling"] = (
    master["MastersWinRate"]
    - master["SilverWinRate"]
)

master["UseRateScaling"] = (
    master["MastersUseRate"]
    - master["SilverUseRate"]
)

# Save final master dataset
master.to_csv(OUTPUT_PATH, index=False)

print("Master dataset created successfully!")
print(f"Rows: {len(master)}")
print(f"Columns: {len(master.columns)}")
print(f"Saved to: {OUTPUT_PATH}")

