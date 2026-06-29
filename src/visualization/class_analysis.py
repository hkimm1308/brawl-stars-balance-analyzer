import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the final cleaned dataset
df = pd.read_csv("data/brawler_final_dataset.csv")

# Check how many brawlers are in each class
# This helps us understand the sample size for each group
print("Brawler count by class:")
print(df["Class"].value_counts())

# Group brawlers by Class, then calculate the average MetaScore for each class
class_scores = (
    df.groupby("Class")["MetaScore"]
      .mean()
      .sort_values(ascending=False)
)

# Print results in the terminal so we can interpret the numbers
print("\nAverage MetaScore by class:")
print(class_scores)

# Make sure the charts folder exists before saving the image
Path("charts").mkdir(exist_ok=True)

# Create the chart
plt.figure(figsize=(10, 6))

# Bar chart of average MetaScore by class
ax = class_scores.plot(
    kind="bar",
    edgecolor="black"
)

# Chart title and axis labels
plt.title(
    "Average MetaScore by Brawler Class",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Brawler Class", fontsize=12)
plt.ylabel("Average MetaScore", fontsize=12)

# Add exact values above each bar
for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f",
        padding=3
    )

# Add light horizontal grid lines to make values easier to compare
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Rotate x labels so class names do not overlap
plt.xticks(rotation=30, ha="right")

# Prevent labels from being cut off
plt.tight_layout()

# Save the chart to the charts folder
plt.savefig("charts/class_meta_scores.png", dpi=400)

# Display the chart
plt.show()