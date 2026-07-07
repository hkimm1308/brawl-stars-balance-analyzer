# Target: MetaScoreScaling

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from feature_groups import GAMEPLAY


DATA_PATH = "data/master_dataset.csv"
TARGET = "MetaScoreScaling"

df = pd.read_csv(DATA_PATH)

feature_columns = GAMEPLAY

X = df[feature_columns]
y = df[TARGET]

numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object", "string"]).columns.tolist()

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
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
        ("regressor", LinearRegression()),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)

print("Baseline Linear Regression Results")
print("=" * 40)
print(f"Target: {TARGET}")
print(f"Rows: {len(df)}")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print()
print(f"MAE:  {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²:   {r2:.3f}")

results = pd.DataFrame({
    "Name": df.loc[y_test.index, "Name"],
    "ActualMetaScoreScaling": y_test,
    "PredictedMetaScoreScaling": predictions,
})

results["Error"] = (
    results["ActualMetaScoreScaling"]
    - results["PredictedMetaScoreScaling"]
)

results = results.reindex(
    results["Error"].abs().sort_values(ascending=False).index
)

print("\nLargest Prediction Errors")
print("=" * 40)
print(results.head(10).to_string(index=False))