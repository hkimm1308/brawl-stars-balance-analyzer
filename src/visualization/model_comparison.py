"""
Create a bar chart comparing model performance across the project.

Lower mean absolute error is better.
"""

from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_PATH = "charts/model_comparison.png"


def main():
    models = [
        "Linear Regression",
        "Random Forest",
        "Tuned Random Forest",
        "RFECV Random Forest",
    ]

    cv_mae = [
        3.8780,
        1.6180,
        1.5072,
        1.4975,
    ]

    Path("charts").mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))

    bars = plt.bar(models, cv_mae)

    plt.title("Model Performance Comparison")
    plt.xlabel("Model")
    plt.ylabel("Cross-Validated Mean Absolute Error")
    plt.xticks(rotation=15, ha="right")

    for bar, value in zip(bars, cv_mae):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.04,
            f"{value:.3f}",
            ha="center",
            va="bottom",
        )

    plt.ylim(0, max(cv_mae) * 1.15)
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved model comparison chart to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()