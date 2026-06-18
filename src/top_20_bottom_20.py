import pandas as pd

df = pd.read_csv("data/brawler_performance.csv")

print("\nTop 20 MetaScore")
print(
    df.sort_values("MetaScore", ascending=False)
    [["Name", "MetaScore"]]
    .head(20)
)

print("\nBottom 20 MetaScore")
print(
    df.sort_values("MetaScore")
    [["Name", "MetaScore"]]
    .head(20)
)