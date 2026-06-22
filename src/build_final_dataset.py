import pandas as pd

performance = pd.read_csv("data/brawler_performance_scraped.csv")
attributes = pd.read_csv("data/brawler_attributes_scraped.csv")
ai = pd.read_csv("data/brawler_ai.csv")

performance = performance.drop_duplicates(subset="Name")
attributes = attributes.drop_duplicates(subset="Name")
ai = ai.drop_duplicates(subset="Name")

print("Performance rows:", len(performance))
print("Attribute rows:", len(attributes))
print("AI rows:", len(ai))

merged = performance.merge(attributes, on="Name", how="left")
merged = merged.merge(ai, on="Name", how="left")

print("\nFinal shape:", merged.shape)

print("\nMissing scraped attributes:")
print(merged[merged["Health"].isna()]["Name"].tolist())

print("\nMissing AI features:")
print(merged[merged["HasDash"].isna()]["Name"].tolist())

merged.to_csv("data/brawler_final_dataset.csv", index=False)

print("\nSaved final dataset to data/brawler_final_dataset.csv")