# Target: MetaScoreScaling

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from feature_groups import GAMEPLAY

# -----------------------------
# Configuration
# -----------------------------

DATA_PATH = "data/master_dataset.csv"
TARGET = "MetaScoreScaling"  # Change this to "MetaScoreScaling" or any other target variable as needed

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(DATA_PATH)

# Gameplay features only

feature_columns = GAMEPLAY

X = df[feature_columns]
y = df[TARGET]

# Separate numerical and categorical features
numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object", "string"]).columns.tolist()

# -----------------------------
# Preprocessing
# -----------------------------

# Fill missing numerical values with the median
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
    ]
)

# Fill missing categorical values and one-hot encode them
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

# Apply preprocessing to the appropriate columns
preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_transformer, numeric_cols),
        ("categorical", categorical_transformer, categorical_cols),
    ]
)

# -----------------------------
# Build Model
# -----------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=500,
                random_state=42,
                max_depth=2,
                min_samples_split=10,
                min_samples_leaf=1,
                max_features="log2",
            ),
        ),
    ]
)

# -----------------------------
# Cross-Validation
# -----------------------------

# Cross-validation gives a more reliable estimate than one train/test split,
# especially because this dataset only has 103 brawlers.
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

print("Cross-Validation Results")
print("=" * 40)
print(f"Target: {TARGET}")
print(f"R² scores:  {r2_scores}")
print(f"Mean R²:    {r2_scores.mean():.3f}")
print(f"Std R²:     {r2_scores.std():.3f}")
print()
print(f"MAE scores: {mae_scores}")
print(f"Mean MAE:   {mae_scores.mean():.3f}")
print(f"Std MAE:    {mae_scores.std():.3f}")
print()

# -----------------------------
# Train / Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# -----------------------------
# Evaluate Model
# -----------------------------

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)

print("Random Forest Regression Results")
print("=" * 40)
print(f"Target: {TARGET}")
print(f"Rows: {len(df)}")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print()
print(f"MAE:  {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²:   {r2:.3f}")

# -----------------------------
# Largest Prediction Errors
# -----------------------------

results = pd.DataFrame({
    "Name": df.loc[y_test.index, "Name"],
    f"Actual{TARGET}": y_test,
    f"Predicted{TARGET}": predictions,
})

results["Error"] = (
    results[f"Actual{TARGET}"]
    - results[f"Predicted{TARGET}"]
)

results = results.reindex(
    results["Error"].abs().sort_values(ascending=False).index
)

print("\nLargest Prediction Errors")
print("=" * 40)
print(results.head(10).to_string(index=False))

# -----------------------------
# Feature Importance
# -----------------------------

feature_names = model.named_steps["preprocessor"].get_feature_names_out()
importances = model.named_steps["regressor"].feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances,
}).sort_values("Importance", ascending=False)

print("\nTop 20 Feature Importances")
print("=" * 40)
print(importance_df.head(20).to_string(index=False))