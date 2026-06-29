import pandas as pd
import matplotlib.pyplot as plt

performance_df = pd.read_csv("data/brawler_performance.csv")
attributes_df = pd.read_csv("data/brawler_attributes_scraped.csv")

print("Performance Shape:")
print(performance_df.shape)

print("\nAttributes Shape:")
print(attributes_df.shape)

# The merged DataFrame contains all the performance metrics along with the attributes for each brawler in the attributes csv.
merged_df = performance_df.merge(
    attributes_df,
    on="Name",
    how="inner"
)

# Check that the merge worked correctly and that we have the expected number of rows and columns in the merged DataFrame.
print("\nMerged Shape:")
print(merged_df.shape)

# Lets look at the average win rate by class to see if there are any trends in the data. 
# We group the merged DataFrame by the "Class" column and calculate the mean win rate for each class, 
# then sort the results in descending order to see which classes have the highest average win rates.
print("\nAverage Win Rate by Class")
print(
    merged_df.groupby("Class")["WinRate"]
    .mean()
    .sort_values(ascending=False)
)


# Now lets look at average meta score by class.
print("\nAverage Meta Score by Class")
print(
    merged_df.groupby("Class")["MetaScore"]
    .mean()
    .sort_values(ascending=False)
)

# Lets now look at average win rate by range.
# We group the merged DataFrame by the "RangeCategory" column and calculate the mean win rate for each range category, 
# then sort the results in descending order to see which range categories have the highest average win rates.
print(
    merged_df.groupby("RangeCategory")["WinRate"]
    .mean()
    .sort_values(ascending=False)
)

# Finally, we look at the average meta score by range category to see if there are any trends in the data.
print("\nAverage Meta Score by Range")
print(
    merged_df.groupby("RangeCategory")["MetaScore"]
    .mean()
    .sort_values(ascending=False)
)

print("\nHealth vs Win Rate Correlation")
print(
    merged_df["Health"].corr(
        merged_df["WinRate"]
    )
)

print("\nHealth vs Meta Score Correlation")
print(
    merged_df["Health"].corr(
        merged_df["MetaScore"]
    )
)



# Chart 1: Health vs Win Rate
plt.figure()

plt.scatter(
    merged_df["Health"],
    merged_df["WinRate"]
)

plt.xlabel("Health")
plt.ylabel("Win Rate")
plt.title("Health vs Win Rate")

plt.tight_layout()
plt.savefig("charts/health_vs_win_rate.png")
plt.close()


# Chart 2: Health vs Meta Score
plt.figure()

plt.scatter(
    merged_df["Health"],
    merged_df["MetaScore"]
)

plt.xlabel("Health")
plt.ylabel("Meta Score")
plt.title("Health vs Meta Score")

plt.tight_layout()
plt.savefig("charts/health_vs_meta_score.png")
plt.close()

# Start Day 6

# Chart 3: Average Meta Score by Class
avg_meta_by_class = (
    merged_df.groupby("Class")["MetaScore"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure()

avg_meta_by_class.plot(kind="bar")

plt.xlabel("Class")
plt.ylabel("Average Meta Score")
plt.title("Average Meta Score by Class")

plt.tight_layout()
plt.savefig("charts/average_meta_score_by_class.png")
plt.close()

# Chart 4: Average Win Rate by class
avg_wr_by_class = (
    merged_df.groupby("Class")["WinRate"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure()

avg_wr_by_class.plot(kind="bar")

plt.xlabel("Class")
plt.ylabel("Average Win Rate")
plt.title("Average Win Rate by Class")

plt.tight_layout()
plt.savefig("charts/average_win_rate_by_class.png")
plt.close()


class_summary = merged_df.groupby("Class").agg({
    "WinRate": "mean",
    "MetaScore": "mean"
})

class_summary["MetaMinusWin"] = (
    class_summary["MetaScore"]
    - class_summary["WinRate"] / 10
)

print(class_summary)

# Chart 5: Meta Score by Rarity
print("\nAverage Meta Score by Rarity")
print(
    merged_df.groupby("Rarity")["MetaScore"]
    .mean()
    .sort_values(ascending=False)
)

# Chart 6: Average Win Rate by Rarity
print("\nAverage Win Rate by Rarity")
print(
    merged_df.groupby("Rarity")["WinRate"]
    .mean()
    .sort_values(ascending=False)
)