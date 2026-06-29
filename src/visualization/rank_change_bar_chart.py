# python src/visualization/rank_change_bar_chart.py

import pandas as pd
import matplotlib.pyplot as plt

# Read expanded dataset with Silver through Masters performance data
df = pd.read_csv("data/performance_by_rank.csv")

# Create a wide table:
# one row per brawler, one column per rank tier
meta_by_rank = df.pivot(
    index="Name",
    columns="RankTier",
    values="MetaScore"
)

# Measure how much each brawler's MetaScore changes
# from Silver to Legendary
meta_by_rank["MetaScoreChange"] = (
    meta_by_rank["Legendary"] - meta_by_rank["Silver"]
)

# Get the 8 biggest climbers and 8 biggest fallers
top_climbers = meta_by_rank.sort_values(
    by="MetaScoreChange",
    ascending=False
).head(8)

top_fallers = meta_by_rank.sort_values(
    by="MetaScoreChange",
    ascending=True
).head(8)

# Combine both groups into one chart dataset
plot_df = pd.concat([top_fallers, top_climbers])

# Sort so the biggest positive changes appear at the top
plot_df = plot_df.sort_values("MetaScoreChange")

# Create horizontal bar chart
plt.figure(figsize=(10, 8))

plt.barh(
    plot_df.index,
    plot_df["MetaScoreChange"]
)

# Add vertical zero line to separate climbers from fallers
plt.axvline(0, linewidth=1)

plt.title("Biggest MetaScore Changes from Silver to Legendary")
plt.xlabel("MetaScore Change")
plt.ylabel("Brawler")

plt.tight_layout()

# Save chart
plt.savefig(
    "charts/metascore_change_silver_to_legendary.png",
    dpi=300
)

plt.show()
