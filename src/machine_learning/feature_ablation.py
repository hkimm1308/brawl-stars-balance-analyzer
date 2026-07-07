import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from feature_groups import (
    CORE_STATS,
    COMBAT,
    GAMEPLAY,
    MECHANICS,
    CATEGORIES,
    ALL_FEATURES,
)

# -----------------------------
# Configuration
# -----------------------------

DATA_PATH = "data/master_dataset.csv"
TARGET = "MetaScoreScaling"

# Load master dataset
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Feature Group Combinations
# -----------------------------
# Each experiment trains the same model using a different
# subset of gameplay features.

FEATURE_GROUPS = {
    "Core Stats": CORE_STATS,
    "Combat": COMBAT,
    "Gameplay": GAMEPLAY,
    "Mechanics": MECHANICS,
    "Categories": CATEGORIES,

    "Core + Combat": CORE_STATS + COMBAT,
    "Core + Gameplay": CORE_STATS + GAMEPLAY,
    "Core + Mechanics": CORE_STATS + MECHANICS,
    "Core + Categories": CORE_STATS + CATEGORIES,

    "Everything": ALL_FEATURES,
}

# -----------------------------
# Feature Ablation Experiment
# -----------------------------

results = []

y = df[TARGET]

for group_name, feature_columns in FEATURE_GROUPS.items():

    print(f"\nRunning: {group_name}")

    X = df[feature_columns]

    # Separate numeric and categorical columns
    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = X.select_dtypes(include=["object", "string"]).columns.tolist()

    # Preprocessing pipelines
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, numeric_cols),
            ("categorical", categorical_transformer, categorical_cols),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "regressor",
                RandomForestRegressor(
                    n_estimators=500,
                    random_state=42,
                    min_samples_leaf=3,
                ),
            ),
        ]
    )

    cv = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42,
    )

    r2_scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="r2",
    )

    mae_scores = -cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="neg_mean_absolute_error",
    )

    results.append({
        "Feature Group": group_name,
        "Mean R²": r2_scores.mean(),
        "Std R²": r2_scores.std(),
        "Mean MAE": mae_scores.mean(),
        "Features": len(feature_columns),
    })

# -----------------------------
# Display Results
# -----------------------------

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    "Mean R²",
    ascending=False,
)

print("\n")
print("=" * 85)
print("FEATURE ABLATION RESULTS")
print("=" * 85)

print(results_df.to_string(index=False))