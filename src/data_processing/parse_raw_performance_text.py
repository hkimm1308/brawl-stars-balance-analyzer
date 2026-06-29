# python src/data_processing/parse_raw_performance_text.py

import os              # Lets Python check whether files exist
import pandas as pd    # Used for creating and saving data tables (DataFrames)

# Dictionary that stores every raw performance file we want to parse.
# The key is the ranked tier, and the value is the file location.
rank_files = {
    "Silver": "data/raw_performance_silver.txt",
    "Gold": "data/raw_performance_gold.txt",
    "Diamond": "data/raw_performance_diamond.txt",
    "Mythic": "data/raw_performance_mythic.txt",
    "Legendary": "data/raw_performance_legendary.txt",
    "Masters": "data/raw_performance_masters.txt",
}

# Final combined dataset containing every ranked tier
output_file = "data/performance_by_rank.csv"

# This list will eventually contain every parsed row
all_rows = []


def parse_rank_file(input_file, rank_tier):
    """
    Reads one raw copied Brawlytix table and converts it
    into a list of dictionaries.
    """

    # Skip this rank if the raw text file doesn't exist yet.
    # This lets us build the project one rank at a time.
    if not os.path.exists(input_file):
        print(f"Skipping {rank_tier}: file not found")
        return []

    # Read every non-empty line from the text file
    with open(input_file, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    rows = []

    # Keeps track of which line we're currently reading
    i = 0

    while i < len(lines):

        # Every brawler entry begins with its numeric rank
        if lines[i].isdigit():

            rank = int(lines[i])

            try:

                # Example layout:
                #
                # 1
                # Bo Icon
                # Bo
                # 57.1   2.32   7.3
                #
                # So the useful information is located
                # a few lines after the rank number.

                name = lines[i + 2]

                # Split the statistics into three numbers
                stats = lines[i + 3].split()

                # Make sure we actually found three values
                if len(stats) != 3:
                    print(f"Skipped {rank_tier} rank {rank}: stats not found")
                    i += 1
                    continue

                # Convert text into decimal numbers
                win_rate = float(stats[0])
                use_rate = float(stats[1])
                meta_score = float(stats[2])

                # Store this brawler as one row
                rows.append({
                    "MetaRank": rank,
                    "Name": name,
                    "RankTier": rank_tier,
                    "WinRate": win_rate,
                    "UseRate": use_rate,
                    "MetaScore": meta_score
                })

                # Move to the next brawler
                i += 4

            except Exception as e:

                # If something unexpected happens,
                # print the error but keep parsing.
                print(f"Skipped {rank_tier} rank {rank}: {e}")
                i += 1

        else:
            # Skip lines that aren't the start of a new brawler
            i += 1


    return rows


# Loop through every ranked tier
for rank_tier, input_file in rank_files.items():

    print(f"\nParsing {rank_tier}...")

    # Parse one file
    rank_rows = parse_rank_file(input_file, rank_tier)

    # Add the parsed rows onto our master dataset
    all_rows.extend(rank_rows)

    print(f"Rows parsed: {len(rank_rows)}")


# Convert everything into one DataFrame
df = pd.DataFrame(all_rows)

# Save the finished dataset
df.to_csv(output_file, index=False)

print("\nCombined dataset:")
print(df.head())
print(df.shape)

print(f"\nSaved to {output_file}")