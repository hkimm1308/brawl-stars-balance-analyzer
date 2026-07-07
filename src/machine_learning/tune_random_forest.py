import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import KFold, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from feature_groups import GAMEPLAY


DATA_PATH = "data/master_dataset.csv"
TARGET = "MetaScoreScaling"

df = pd.read_csv(DATA_PATH)

# Start with the best feature group from ablation
feature_columns = GAMEPLAY

X = df[feature_columns]
y = df[TARGET]

numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object", "string"]).columns.tolist()

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
        ("regressor", RandomForestRegressor(random_state=42)),
    ]
)

param_grid = {
    "regressor__n_estimators": [100, 300, 500, 800],
    "regressor__max_depth": [2, 3, 4, 5, None],
    "regressor__min_samples_split": [2, 5, 10],
    "regressor__min_samples_leaf": [1, 2, 3, 5, 8],
    "regressor__max_features": ["sqrt", "log2", 0.5, 0.75, 1.0],
}

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42,
)

search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_grid,
    n_iter=40,
    cv=cv,
    scoring="neg_mean_absolute_error",
    random_state=42,
    n_jobs=-1,
    verbose=1,
)

search.fit(X, y)

print("Random Forest Hyperparameter Tuning")
print("=" * 50)
print(f"Target: {TARGET}")
print(f"Features used: {len(feature_columns)}")
print()
print("Best parameters:")
print(search.best_params_)
print()
print(f"Best CV MAE: {-search.best_score_:.3f}")