import pandas as pd

performance_df = pd.read_csv("data/brawler_performance.csv")
attributes_df = pd.read_csv("data/brawler_attributes.csv")

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

import matplotlib.pyplot as plt

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