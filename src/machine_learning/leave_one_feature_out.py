# src/machine_learning/leave_one_feature_out.py

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import make_scorer, mean_absolute_error, r2_score
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from pathlib import Path

from feature_groups import GAMEPLAY


DATA_PATH = "data/master_dataset.csv"
TARGET = "MetaScoreScaling"
OUTPUT_PATH = "results/leave_one_feature_out.csv"


def evaluate_features(df, features):
    X = df[features]
    y = df[TARGET]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), features),
        ]
    )

    model = RandomForestRegressor(
        n_estimators=500,
        max_depth=2,
        min_samples_split=10,
        min_samples_leaf=1,
        max_features="log2",
        random_state=42,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    scoring = {
        "mae": make_scorer(mean_absolute_error, greater_is_better=False),
        "r2": make_scorer(r2_score),
    }

    scores = cross_validate(
        pipeline,
        X,
        y,
        cv=5,
        scoring=scoring,
        return_train_score=False,
    )

    return -scores["test_mae"].mean(), scores["test_r2"].mean()


def main():
    df = pd.read_csv(DATA_PATH)

    baseline_mae, baseline_r2 = evaluate_features(df, GAMEPLAY)

    results = []

    for removed_feature in GAMEPLAY:
        remaining_features = [
            feature for feature in GAMEPLAY if feature != removed_feature
        ]

        mae, r2 = evaluate_features(df, remaining_features)

        results.append(
            {
                "RemovedFeature": removed_feature,
                "CV_MAE": mae,
                "CV_R2": r2,
                "Delta_MAE": mae - baseline_mae,
                "Delta_R2": r2 - baseline_r2,
            }
        )

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values("Delta_MAE", ascending=False)

    Path("results").mkdir(exist_ok=True)
    results_df.to_csv(OUTPUT_PATH, index=False)

    print("Leave-one-feature-out analysis complete.")
    print(f"Baseline MAE: {baseline_mae:.4f}")
    print(f"Baseline R2: {baseline_r2:.4f}")
    print(f"Saved results to {OUTPUT_PATH}")
    print()
    print(results_df)


if __name__ == "__main__":
    main()