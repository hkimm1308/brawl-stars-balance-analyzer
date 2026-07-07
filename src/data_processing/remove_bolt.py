import pandas as pd

path = "data/brawler_features_v3_ml_ready.csv"

df = pd.read_csv(path)
df = df[df["Name"] != "Bolt"]

df.to_csv(path, index=False)

print("Bolt removed successfully.")
print(f"Feature rows now: {len(df)}")