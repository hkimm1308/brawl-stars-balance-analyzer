# python src/analysis/rank_progression_analysis.py

import pandas as pd

# Read the expanded performance dataset
df = pd.read_csv("data/performance_by_rank.csv")

# Make sure ranks are ordered correctly
rank_order = [
    "Silver",
    "Gold",
    "Diamond",
    "Mythic",
    "Legendary",
    "Masters"
]

# Convert RankTier into an ordered category
# This keeps plots/tables in the correct rank order
df["RankTier"] = pd.Categorical(
    df["RankTier"],
    categories=rank_order,
    ordered=True
)

# Create a wide table where each brawler has one row
# and each rank tier has its own MetaScore column
meta_by_rank = df.pivot(
    index="Name",
    columns="RankTier",
    values="MetaScore"
)

# Calculate how much each brawler's MetaScore changes
# from Silver to Masters
meta_by_rank["SilverToMastersChange"] = (
    meta_by_rank["Masters"] - meta_by_rank["Silver"]
)

# Biggest climbers
biggest_climbers = meta_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=False
).head(10)

# Biggest fallers
biggest_fallers = meta_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=True
).head(10)

print("\nBiggest MetaScore Climbers: Silver to Masters")
print(biggest_climbers[["Silver", "Masters", "SilverToMastersChange"]])

print("\nBiggest MetaScore Fallers: Silver to Masters")
print(biggest_fallers[["Silver", "Masters", "SilverToMastersChange"]])

# Repeat the same process for WinRate
winrate_by_rank = df.pivot(
    index="Name",
    columns="RankTier",
    values="WinRate"
)

winrate_by_rank["SilverToMastersChange"] = (
    winrate_by_rank["Masters"] - winrate_by_rank["Silver"]
)

biggest_winrate_climbers = winrate_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=False
).head(10)

biggest_winrate_fallers = winrate_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=True
).head(10)

print("\nBiggest WinRate Climbers: Silver to Masters")
print(biggest_winrate_climbers[["Silver", "Masters", "SilverToMastersChange"]])

print("\nBiggest WinRate Fallers: Silver to Masters")
print(biggest_winrate_fallers[["Silver", "Masters", "SilverToMastersChange"]])


# Repeat the same process for UseRate
userate_by_rank = df.pivot(
    index="Name",
    columns="RankTier",
    values="UseRate"
)

userate_by_rank["SilverToMastersChange"] = (
    userate_by_rank["Masters"] - userate_by_rank["Silver"]
)

biggest_userate_climbers = userate_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=False
).head(10)

biggest_userate_fallers = userate_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=True
).head(10)

print("\nBiggest UseRate Climbers: Silver to Masters")
print(biggest_userate_climbers[["Silver", "Masters", "SilverToMastersChange"]])

print("\nBiggest UseRate Fallers: Silver to Masters")

# Combine the most important rank progression metrics into one table
summary = meta_by_rank[["Silver", "Masters", "SilverToMastersChange"]].copy()

summary = summary.rename(columns={
    "Silver": "SilverMetaScore",
    "Masters": "MastersMetaScore",
    "SilverToMastersChange": "MetaScoreChange"
})

summary["SilverWinRate"] = winrate_by_rank["Silver"]
summary["MastersWinRate"] = winrate_by_rank["Masters"]
summary["WinRateChange"] = winrate_by_rank["SilverToMastersChange"]

summary["SilverUseRate"] = userate_by_rank["Silver"]
summary["MastersUseRate"] = userate_by_rank["Masters"]
summary["UseRateChange"] = userate_by_rank["SilverToMastersChange"]

summary = summary.sort_values(
    by="MetaScoreChange",
    ascending=False
)

summary.to_csv("data/rank_progression_summary.csv")

print("\nSaved rank progression summary to data/rank_progression_summary.csv")