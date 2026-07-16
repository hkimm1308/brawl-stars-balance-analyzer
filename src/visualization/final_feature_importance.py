"""
Train the final Random Forest model and visualize the importance
of the six RFECV-selected gameplay features.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


DATA_PATH = "data/master_dataset.csv"
OUTPUT_PATH = "charts/final_feature_importance.png"
TARGET = "MetaScoreScaling"

SELECTED_FEATURES = [
    "MobilityScore",
    "EscapeScore",
    "PositioningImportance",
    "DecisionComplexity",
    "SkillCeiling",
    "SurvivabilityScore",
]

DISPLAY_NAMES = {
    "MobilityScore": "Mobility",
    "EscapeScore": "Escape",
    "PositioningImportance": "Positioning",
    "DecisionComplexity": "Decision Complexity",
    "SkillCeiling": "Skill Ceiling",
    "SurvivabilityScore": "Survivability",
}


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[SELECTED_FEATURES]
    y = df[TARGET]

    model = RandomForestRegressor(
        n_estimators=500,
        max_depth=2,
        min_samples_split=10,
        min_samples_leaf=1,
        max_features="log2",
        random_state=42,
    )

    model.fit(X, y)

    importance_df = pd.DataFrame(
        {
            "Feature": SELECTED_FEATURES,
            "Importance": model.feature_importances_,
        }
    )

    importance_df["DisplayName"] = importance_df["Feature"].map(DISPLAY_NAMES)
    importance_df = importance_df.sort_values("Importance")

    Path("charts").mkdir(exist_ok=True)

    plt.figure(figsize=(9, 6))

    bars = plt.barh(
        importance_df["DisplayName"],
        importance_df["Importance"],
    )

    for bar, value in zip(bars, importance_df["Importance"]):
        plt.text(
            value + 0.005,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.3f}",
            va="center",
        )

    plt.title("Importance of Selected Gameplay Features")
    plt.xlabel("Feature Importance")
    plt.ylabel("Gameplay Feature")
    plt.grid(axis="x", alpha=0.3)

    plt.xlim(
        0,
        importance_df["Importance"].max() + 0.06,
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    print("Final feature importances:")
    print(
        importance_df[
            ["DisplayName", "Importance"]
        ]
        .sort_values("Importance", ascending=False)
        .to_string(index=False)
    )

    print()
    print(f"Saved feature importance chart to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()