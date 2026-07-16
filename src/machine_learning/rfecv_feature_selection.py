"""
Use recursive feature elimination with cross-validation to identify
the strongest subset of engineered gameplay features.
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold

from feature_groups import GAMEPLAY


DATA_PATH = "data/master_dataset.csv"
TARGET = "MetaScoreScaling"

RANKING_OUTPUT_PATH = "results/rfecv_feature_rankings.csv"
CURVE_OUTPUT_PATH = "results/rfecv_performance_curve.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[GAMEPLAY]
    y = df[TARGET]

    model = RandomForestRegressor(
        n_estimators=500,
        max_depth=2,
        min_samples_split=10,
        min_samples_leaf=1,
        max_features="log2",
        random_state=42,
    )

    cv = KFold(
        n_splits=5,
        shuffle=False,
    )

    selector = RFECV(
        estimator=model,
        step=1,
        min_features_to_select=1,
        cv=cv,
        scoring="neg_mean_absolute_error",
        n_jobs=-1,
    )

    print("Running RFECV feature selection...")
    selector.fit(X, y)

    selected_features = [
        feature
        for feature, selected in zip(GAMEPLAY, selector.support_)
        if selected
    ]

    rankings_df = pd.DataFrame(
        {
            "Feature": GAMEPLAY,
            "Selected": selector.support_,
            "Ranking": selector.ranking_,
        }
    ).sort_values(
        by=["Selected", "Ranking"],
        ascending=[False, True],
    )

    # RFECV reports negative MAE because sklearn maximizes scores.
    performance_df = pd.DataFrame(
        {
            "NumFeatures": selector.cv_results_["n_features"],
            "MeanCV_MAE": -selector.cv_results_["mean_test_score"],
            "StdCV_MAE": selector.cv_results_["std_test_score"],
        }
    ).sort_values("NumFeatures")

    Path("results").mkdir(exist_ok=True)

    rankings_df.to_csv(RANKING_OUTPUT_PATH, index=False)
    performance_df.to_csv(CURVE_OUTPUT_PATH, index=False)

    best_row = performance_df.loc[
        performance_df["NumFeatures"] == selector.n_features_
    ].iloc[0]

    print()
    print("RFECV analysis complete.")
    print(f"Optimal number of features: {selector.n_features_}")
    print(f"Optimal CV MAE: {best_row['MeanCV_MAE']:.4f}")
    print()
    print("Selected features:")

    for feature in selected_features:
        print(f"- {feature}")

    print()
    print("Complete feature rankings:")
    print(rankings_df.to_string(index=False))

    print()
    print(f"Saved rankings to {RANKING_OUTPUT_PATH}")
    print(f"Saved performance curve to {CURVE_OUTPUT_PATH}")


if __name__ == "__main__":
    main()