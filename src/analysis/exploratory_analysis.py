import pandas as pd

# Load cleaned brawler performance dataset
df = pd.read_csv("data/brawler_performance.csv")

# Metric 1: Popularity Efficiency
# Higher = strong win rate relative to how often the brawler is used
df["PopularityEfficiency"] = df["WinRate"] / df["UseRate"]

print("\nTop 10 Popularity Efficiency")
print(
    df[["Name", "WinRate", "UseRate", "PopularityEfficiency"]]
    .sort_values("PopularityEfficiency", ascending=False)
    .head(10)
)

# Always says low use brawlers are the most efficient, so it is important to properly weigh the metrics we are looking at.

# Standardize win rate and use rate using z-scores
df["WinRateZ"] = (df["WinRate"] - df["WinRate"].mean()) / df["WinRate"].std()
df["UseRateZ"] = (df["UseRate"] - df["UseRate"].mean()) / df["UseRate"].std()

# Better underused metric:
# High if win rate is above average and use rate is below average
df["UnderusedScore"] = df["WinRateZ"] - df["UseRateZ"]

print("\nTop 15 Underused Brawlers")
print(
    df[["Name", "WinRate", "UseRate", "WinRateZ", "UseRateZ", "UnderusedScore"]]
    .sort_values("UnderusedScore", ascending=False)
    .head(15)
)

# New and improved overused brawler list.
df["OverusedScore"] = df["UseRateZ"] - df["WinRateZ"]

print("\nTop 15 Overused Brawlers")
print(
    df[["Name", "WinRate", "UseRate", "WinRateZ", "UseRateZ", "OverusedScore"]]
    .sort_values("OverusedScore", ascending=False)
    .head(15)
)

print("\nMost Underused Brawlers:")
print(df.sort_values("UnderusedScore", ascending=False)[
    ["Name", "WinRate", "UseRate", "WinRateZ", "UseRateZ", "UnderusedScore"]
].head(15))

print("\nMost Overused Brawlers:")
print(df.sort_values("OverusedScore", ascending=False)[
    ["Name", "WinRate", "UseRate", "WinRateZ", "UseRateZ", "OverusedScore"]
].head(15))

# Metric 2: Meta Gap
# Higher = meta score is high compared to raw win rate
df["MetaGap"] = df["MetaScore"] - (df["WinRate"] / 10)

print("\nTop 10 Meta Gap")
print(
    df[["Name", "WinRate", "MetaScore", "MetaGap"]]
    .sort_values("MetaGap", ascending=False)
    .head(10)
)

# Metric 3: Underused Strength
# Higher = strong win rate but low use rate
df["UnderusedStrength"] = df["WinRate"] - (df["UseRate"] * 5)

print("\nTop 10 Underused Strength")
print(
    df[["Name", "WinRate", "UseRate", "UnderusedStrength"]]
    .sort_values("UnderusedStrength", ascending=False)
    .head(10)
)

# New columns:
df["PickWinProduct"] = df["WinRate"] * df["UseRate"]

df["MetaGap"] = df["MetaScore"] - df["WinRateZ"]

# Standardized strength rating accounting for standardized win rate and meta score.
df["StrengthScore"] = (
    0.6 * df["WinRateZ"] +
    0.4 * df["MetaScore"]
)


# Who are the strongest brawlers overall?
print(df.sort_values("StrengthScore", ascending=False).head)

# How correlated are win rate and meta score?
correlation = df["WinRate"].corr(df["MetaScore"])

print(correlation)


# Is it difference if we look at standardized win rate? No.
correlation_adjusted = df["WinRateZ"].corr(df["MetaScore"])

print(correlation_adjusted)

print(df[["WinRate", "MetaScore"]].describe())

print(df[["WinRate", "MetaScore"]].sort_values("WinRate", ascending=False).head(20))

