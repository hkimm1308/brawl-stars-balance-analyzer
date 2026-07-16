"""
Visualize RFECV performance as the number of selected features changes.

Lower cross-validated MAE is better.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


RESULTS_PATH = "results/rfecv_performance_curve.csv"
OUTPUT_PATH = "charts/rfecv_performance_curve.png"


def main():
    results = pd.read_csv(RESULTS_PATH)
    results = results.sort_values("NumFeatures")

    best_row = results.loc[results["MeanCV_MAE"].idxmin()]
    best_num_features = int(best_row["NumFeatures"])
    best_mae = best_row["MeanCV_MAE"]

    Path("charts").mkdir(exist_ok=True)

    plt.figure(figsize=(9, 6))

    plt.plot(
        results["NumFeatures"],
        results["MeanCV_MAE"],
        marker="o",
        linewidth=2,
    )

    plt.scatter(
        best_num_features,
        best_mae,
        s=100,
        zorder=3,
    )

    plt.annotate(
        f"Best: {best_num_features} features\nMAE: {best_mae:.4f}",
        xy=(best_num_features, best_mae),
        xytext=(best_num_features + 1, best_mae + 0.015),
        arrowprops={"arrowstyle": "->"},
    )

    plt.title("RFECV Performance by Number of Gameplay Features")
    plt.xlabel("Number of Selected Features")
    plt.ylabel("Cross-Validated Mean Absolute Error")
    plt.xticks(results["NumFeatures"])
    plt.grid(axis="y", alpha=0.3)

    margin = 0.005
    plt.ylim(
        results["MeanCV_MAE"].min() - margin,
        results["MeanCV_MAE"].max() + margin,
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH,
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    print(f"Optimal number of features: {best_num_features}")
    print(f"Optimal CV MAE: {best_mae:.4f}")
    print(f"Saved RFECV performance curve to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()