import pandas as pd

df = pd.read_csv("data/brawler_performance.csv")

# After loading the CSV file into a DataFrame, the script prints the first few rows, the DataFrame's info, and descriptive 
# statistics to provide an overview of the data and ensure it has been loaded correctly.
print(df.head())
print(df.info())
print(df.describe())

# What is the average win rate?
# Should be around 50%. Result was 50.24, which is reasonable given the nature of win rates in Brawl Stars.
print(df["WinRate"].mean())

# What is the average Meta Score?
# I am not familar with this scale, so the mean should give a good understanding of interpreting Meta Scores. Result was 4.80.
print(df["MetaScore"].mean())

# What brawlers have the highest win rates?
# The top 3 are all brand new brawlers, which is expected with the trend of new brawlers being very strong at launch.
print(df.sort_values("WinRate", ascending=False).head())

# Who has the lowest win rates?
# Off the bat it seems lik ethe bottom 5 seem to all be older brawlers, though the pattern of bottom tier brawlers seems more random.
print(df.sort_values("WinRate").head())

# Which brawlers are Meta? Ie. which brawlers have a Meta Score above 7?
# There were 15 brawlers, and almost all of them were either new or had recently recieved buffies.
print(df[df["MetaScore"] > 7])

# What brawlers are the most popular? Ie. which brawlers have the highest use rates?
# Mostly all low rarity meta brawlers. Accessible and strong brawlers tend to be the most popular.
print(df.sort_values("UseRate", ascending=False).head(10))

# Is the Meta Score correlated with Win Rate?
# It seems like they might, but I am not sure how strong the correlation is. 
# A scatter plot would be a good way to visualize this relationship.
print(df[["Name","WinRate","MetaScore"]]
      .sort_values("MetaScore", ascending=False)
      .head(20))

