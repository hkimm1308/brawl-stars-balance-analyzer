"""
Visualize benchmark results across machine learning models.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


RESULTS_PATH = "results/model_benchmark.csv"
OUTPUT_PATH = "charts/model_benchmark.png"


def main():
    results = pd.read_csv(RESULTS_PATH)
    results = results.sort_values("MeanCV_MAE")

    Path("charts").mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        results["Model"],
        results["MeanCV_MAE"],
    )

    winner = bars[0]
    winner.set_hatch("//")

    for bar, value in zip(bars, results["MeanCV_MAE"]):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            value + 0.015,
            f"{value:.3f}",
            ha="center",
            fontsize=10,
        )

    plt.title("Machine Learning Model Benchmark")
    plt.ylabel("Cross-Validated Mean Absolute Error")
    plt.xticks(rotation=12, ha="right")

    margin = 0.05
    plt.ylim(
        results["MeanCV_MAE"].min() - margin,
        results["MeanCV_MAE"].max() + margin,
    )

    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=300)
    plt.close()

    print(f"Saved benchmark chart to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()