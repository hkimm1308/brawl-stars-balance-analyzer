# src/analysis.py

import pandas as pd

# Load the final cleaned dataset.
# This file now includes performance data, scraped attributes,
# AI-labeled gameplay mechanics, and engineered damage features.
df = pd.read_csv("data/brawler_final_dataset.csv")

# These are the binary gameplay mechanics we added with AI labels.
# Each column answers a True/False question, like:
# "Does this brawler have healing?" or "Does this brawler have stun?"
mechanics = [
    "HasDash",
    "HasHealing",
    "HasStun",
    "HasSlow",
    "HasPet",
    "HasPiercing",
    "HasSplashDamage",
    "HasWallBreak",
    "HasShield",
    "HasInvisibility",
    "HasKnockback",
    "HasAreaControl",
]

# For each gameplay mechanic, compare the average MetaScore
# of brawlers that HAVE the mechanic vs brawlers that DO NOT.
#
# Example:
# If HasStun=True brawlers have a much higher average MetaScore
# than HasStun=False brawlers, stun may be associated with stronger brawlers.
results = []

for mechanic in mechanics:

    means = df.groupby(mechanic)["MetaScore"].mean()

    if True in means.index and False in means.index:

        results.append({
            "Mechanic": mechanic,
            "MetaScoreBoost":
                means[True] - means[False]
        })

results_df = pd.DataFrame(results)

results_df = (
    results_df
    .sort_values(
        "MetaScoreBoost",
        ascending=False
    )
)

print(results_df)