# python src/machine_learning/train_models.py

import pandas as pd

# Splits our data into training and testing sets
from sklearn.model_selection import train_test_split

# Machine learning model we'll use
from sklearn.ensemble import RandomForestRegressor

# Checks mean absolute error and R² score of the model
from sklearn.metrics import mean_absolute_error, r2_score

# Read the final cleaned dataset
df = pd.read_csv("data/brawler_final_dataset.csv")


def train_and_evaluate(feature_cols, model_name):
    """
    Trains and evaluates a Random Forest model using the selected features.
    """

    # X contains the information we give the model
    X = df[feature_cols].astype(float)

    # y is what we want the model to predict
    y = df["MetaScore"]

    # Split the data:
    # 80% is used to train the model
    # 20% is hidden and used to test the model
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create the Random Forest model
    # n_estimators=200 means the forest builds 200 decision trees
    # random_state=42 makes the results reproducible
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Use the trained model to make predictions on unseen test data
    predictions = model.predict(X_test)

    # Evaluate how well the model performed
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Calculate feature importance scores
    # Higher values indicate the feature had more influence on predictions
    importance = pd.DataFrame({
        "Feature": feature_cols,
        "Importance": model.feature_importances_
    }).sort_values(
        by="Importance",
        ascending=False
    )

    # Display the results for this model
    print("\n" + "=" * 60)
    print(model_name)
    print("=" * 60)

    print(f"Training Samples: {len(X_train)}")
    print(f"Testing Samples : {len(X_test)}")
    print(f"Number of Features: {len(feature_cols)}")

    print(f"\nMean Absolute Error: {mae:.3f}")
    print(f"R² Score: {r2:.3f}")

    print("\nFeature Importance:")
    print(importance.to_string(index=False))


# ----------------------------------------------------
# Model A
# Gameplay mechanics only
# ----------------------------------------------------

model_a = [
    "Health",
    "ProjectileCount",
    "DamagePerProjectile",
    "TotalDamage",
    "SkillCeiling",
    "HasDash",
    "HasHealing",
    "HasStun",
    "HasSlow",
    "HasPet",
    "HasPiercing",
    "HasSplashDamage",
    "HasWallBreak",
    "HasShield",
    "HasInvisibility",
    "HasKnockback",
    "HasAreaControl"
]

# ----------------------------------------------------
# Model B
# Gameplay mechanics + performance statistics
# Tests how much WinRate and UseRate improve prediction
# ----------------------------------------------------

model_b = model_a + [
    "WinRate",
    "UseRate"
]

# ----------------------------------------------------
# Model C
# Performance statistics only
# Tests whether gameplay mechanics actually add value
# ----------------------------------------------------

model_c = [
    "WinRate",
    "UseRate"
]

# ----------------------------------------------------
# Train and evaluate all three models
# ----------------------------------------------------

RUN_MODELS = False

if RUN_MODELS:
    train_and_evaluate(
        model_a,
        "Model A - Gameplay Mechanics"
    )

    train_and_evaluate(
        model_b,
        "Model B - Mechanics + Performance"
    )


    train_and_evaluate(
        model_c,
        "Model C - Performance Statistics"
    )

print(df[["MetaScore", "UseRate", "WinRate"]].corr())