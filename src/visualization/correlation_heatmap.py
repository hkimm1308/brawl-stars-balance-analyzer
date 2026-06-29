import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

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

labels = [
    "Win Rate",
    "Use Rate",
    "Meta Score",
    "Health",
    "Projectiles",
    "Damage/Proj",
    "Total Damage",
    "Skill Ceiling"
]

corr = df[corr_cols].corr()

Path("charts").mkdir(exist_ok=True)

plt.figure(figsize=(12, 10))

plt.imshow(
    corr,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

cbar = plt.colorbar()
cbar.set_label("Pearson Correlation", fontsize=11)

plt.xticks(
    range(len(labels)),
    labels,
    rotation=40,
    ha="right",
    fontsize=11
)

plt.yticks(
    range(len(labels)),
    labels,
    fontsize=11
)

plt.gca().set_xticks([x - 0.5 for x in range(1, len(labels))], minor=True)
plt.gca().set_yticks([y - 0.5 for y in range(1, len(labels))], minor=True)

plt.grid(which="minor", color="white", linewidth=1.5)
plt.tick_params(which="minor", bottom=False, left=False)

plt.title(
    "Correlation Matrix of Brawler Performance Features",
    fontsize=18,
    fontweight="bold",
    pad=15
)

for i in range(len(corr_cols)):
    for j in range(len(corr_cols)):
        value = corr.iloc[i, j]

        if i == j:
            display_text = ""
        else:
            display_text = f"{value:.2f}"

        text_color = "white" if abs(value) > 0.5 else "black"
        text_weight = "bold" if abs(value) >= 0.5 else "normal"

        plt.text(
            j,
            i,
            display_text,
            ha="center",
            va="center",
            color=text_color,
            fontsize=11,
            fontweight=text_weight
        )

plt.tight_layout()
plt.subplots_adjust(
    top=0.92,
    bottom=0.22,
    left=0.18,
    right=0.95
)

plt.savefig("charts/correlation_heatmap.png", dpi=400)
plt.show()