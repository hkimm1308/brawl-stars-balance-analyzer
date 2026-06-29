# python src/visualization/rank_progression_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/performance_by_rank.csv")

rank_order = ["Silver", "Gold", "Diamond", "Mythic", "Legendary", "Masters"]
x_values = list(range(len(rank_order)))

df["RankTier"] = pd.Categorical(df["RankTier"], categories=rank_order, ordered=True)

meta_by_rank = df.pivot(index="Name", columns="RankTier", values="MetaScore")

meta_by_rank["SilverToMastersChange"] = meta_by_rank["Masters"] - meta_by_rank["Silver"]

top_climbers = meta_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=False
).head(5).index

top_fallers = meta_by_rank.sort_values(
    by="SilverToMastersChange",
    ascending=True
).head(5).index

plt.figure(figsize=(12, 7))

# Background brawlers
for brawler in meta_by_rank.index:
    plt.plot(
        x_values,
        meta_by_rank.loc[brawler, rank_order],
        linewidth=1,
        alpha=0.08
    )

# Highlight climbers
for brawler in top_climbers:
    y_values = meta_by_rank.loc[brawler, rank_order]

    plt.plot(
        x_values,
        y_values,
        linewidth=3,
        marker="o"
    )

    plt.text(
        x_values[-1] + 0.05,
        y_values["Masters"],
        brawler,
        fontsize=9,
        va="center"
    )

# Highlight fallers
for brawler in top_fallers:
    y_values = meta_by_rank.loc[brawler, rank_order]

    plt.plot(
        x_values,
        y_values,
        linewidth=3,
        marker="o",
        linestyle="--"
    )

    plt.text(
        x_values[-1] + 0.05,
        y_values["Masters"],
        brawler,
        fontsize=9,
        va="center"
    )

plt.title("Brawler MetaScore Progression Across Ranked Tiers")
plt.xlabel("Rank Tier")
plt.ylabel("MetaScore")

plt.xticks(x_values, rank_order)
plt.ylim(0, 10)
plt.xlim(-0.2, len(rank_order) - 0.3)

plt.tight_layout()

plt.savefig("charts/rank_progression_metascore.png", dpi=300)
plt.show()