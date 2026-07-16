"""
Compare multiple ensemble regression models using the same selected features,
cross-validation folds, and evaluation metrics.
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import (
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.metrics import make_scorer, mean_absolute_error, r2_score
from sklearn.model_selection import KFold, cross_validate


DATA_PATH = "data/master_dataset.csv"
OUTPUT_PATH = "results/model_benchmark.csv"
TARGET = "MetaScoreScaling"

SELECTED_FEATURES = [
    "MobilityScore",
    "EscapeScore",
    "PositioningImportance",
    "DecisionComplexity",
    "SkillCeiling",
    "SurvivabilityScore",
]


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[SELECTED_FEATURES]
    y = df[TARGET]

    cv = KFold(
        n_splits=5,
        shuffle=False,
    )

    scoring = {
        "mae": make_scorer(
            mean_absolute_error,
            greater_is_better=False,
        ),
        "r2": make_scorer(r2_score),
    }

    models = {
        "Tuned Random Forest": RandomForestRegressor(
            n_estimators=500,
            max_depth=2,
            min_samples_split=10,
            min_samples_leaf=1,
            max_features="log2",
            random_state=42,
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            random_state=42,
        ),
        "Histogram Gradient Boosting": HistGradientBoostingRegressor(
            random_state=42,
        ),
        "Extra Trees": ExtraTreesRegressor(
            n_estimators=500,
            random_state=42,
        ),
    }

    results = []

    for model_name, model in models.items():
        print(f"Evaluating {model_name}...")

        scores = cross_validate(
            model,
            X,
            y,
            cv=cv,
            scoring=scoring,
            return_train_score=False,
        )

        results.append(
            {
                "Model": model_name,
                "MeanCV_MAE": -scores["test_mae"].mean(),
                "StdCV_MAE": scores["test_mae"].std(),
                "MeanCV_R2": scores["test_r2"].mean(),
                "StdCV_R2": scores["test_r2"].std(),
            }
        )

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values("MeanCV_MAE")

    Path("results").mkdir(exist_ok=True)
    results_df.to_csv(OUTPUT_PATH, index=False)

    print()
    print("Model benchmark complete.")
    print(results_df.to_string(index=False))
    print()
    print(f"Saved results to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()