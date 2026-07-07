import pandas as pd

PERFORMANCE_PATH = "data/performance_by_rank.csv"
FEATURES_PATH = "data/brawler_features_v3_ml_ready.csv"

performance = pd.read_csv(PERFORMANCE_PATH)
features = pd.read_csv(FEATURES_PATH)

# Clean name spacing just in case
performance["Name"] = performance["Name"].str.strip()
features["Name"] = features["Name"].str.strip()

performance_names = set(performance["Name"].unique())
feature_names = set(features["Name"].unique())

only_in_performance = sorted(performance_names - feature_names)
only_in_features = sorted(feature_names - performance_names)

print("\n=== Dataset Row Counts ===")
print(f"Performance rows: {len(performance)}")
print(f"Feature rows: {len(features)}")

print("\n=== Unique Brawler Counts ===")
print(f"Performance brawlers: {len(performance_names)}")
print(f"Feature brawlers: {len(feature_names)}")

print("\n=== Names only in performance_by_rank.csv ===")
if only_in_performance:
    for name in only_in_performance:
        print(f"- {name}")
else:
    print("None")

print("\n=== Names only in brawler_features_v3_ml_ready.csv ===")
if only_in_features:
    for name in only_in_features:
        print(f"- {name}")
else:
    print("None")

print("\n=== Duplicate Names in Features Dataset ===")
feature_duplicates = features[features["Name"].duplicated()]["Name"].tolist()
if feature_duplicates:
    for name in feature_duplicates:
        print(f"- {name}")
else:
    print("None")

print("\n=== Rank Counts per Brawler ===")
rank_counts = performance.groupby("Name")["RankTier"].nunique()
bad_rank_counts = rank_counts[rank_counts != 6]

if len(bad_rank_counts) > 0:
    print("Some brawlers do not have all 6 ranks:")
    print(bad_rank_counts)
else:
    print("Every performance brawler has all 6 ranks.")

print("\nValidation complete.")