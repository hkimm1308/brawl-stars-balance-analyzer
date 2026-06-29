# python src/visualization/userate_v_metascore.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/brawler_final_dataset.csv")

plt.scatter(df["UseRate"], df["MetaScore"])
plt.xlabel("Use Rate")
plt.ylabel("Meta Score")
plt.title("Use Rate vs Meta Score")
plt.savefig("charts/use_rate_vs_meta_score.png", dpi=300)
plt.show()