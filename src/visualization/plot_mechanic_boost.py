import pandas as pd
import matplotlib.pyplot as plt

# Load the final cleaned dataset.
# This contains:
# - Performance data (WinRate, UseRate, MetaScore)
# - Scraped attributes (Health, Damage, Class, etc.)
# - AI-generated gameplay mechanic features
# - Engineered damage features
df = pd.read_csv("data/brawler_final_dataset.csv")

# These are the gameplay mechanics we want to analyze.
# Each column is a True/False feature describing whether
# a brawler possesses that mechanic.
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

# We'll store the results here before turning them
# into a dataframe.
results = []

# For each gameplay mechanic:
# Compare the average MetaScore of brawlers WITH the mechanic
# against the average MetaScore of brawlers WITHOUT it.
#
# Example:
# HasStun = True  -> average MetaScore = 5.85
# HasStun = False -> average MetaScore = 4.60
#
# MetaScoreBoost = 5.85 - 4.60 = +1.25
#
# Positive values suggest the mechanic is associated with
# stronger brawlers.
#
# Negative values suggest the mechanic is associated with
# weaker brawlers.
for mechanic in mechanics:

    means = df.groupby(mechanic)["MetaScore"].mean()

    # Make sure both True and False groups exist.
    # This prevents errors if a feature only contains
    # one value.
    if True in means.index and False in means.index:

        results.append({
            "Mechanic": mechanic,
            "MetaScoreBoost": means[True] - means[False]
        })

# Convert results into a dataframe.
results_df = pd.DataFrame(results)

# Sort so the mechanics with the biggest positive impact
# appear first.
results_df = results_df.sort_values(
    "MetaScoreBoost",
    ascending=False
)

# Print the ranking table so we can inspect the values.
print(results_df)

# Create the visualization.
plt.figure(figsize=(10, 6))

# Each bar represents the average MetaScore advantage
# associated with a mechanic.
plt.bar(
    results_df["Mechanic"],
    results_df["MetaScoreBoost"]
)

# Rotate labels so they don't overlap.
plt.xticks(rotation=45)

plt.ylabel("MetaScore Boost")

plt.title(
    "Average MetaScore Advantage by Gameplay Mechanic"
)

# Improve spacing.
plt.tight_layout()

# Save chart for README/GitHub usage later.
plt.savefig("charts/mechanic_boosts.png")

# Display chart.
plt.show()