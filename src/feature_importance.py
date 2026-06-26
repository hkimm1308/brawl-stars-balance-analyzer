import pandas as pd

# Splits our data into training and testing sets
from sklearn.model_selection import train_test_split

# Machine learning model we'll use later
from sklearn.ensemble import RandomForestRegressor

# Read the final cleaned dataset
df = pd.read_csv("data/brawler_final_dataset.csv")

# Checks mean actual error and R^2 score of the model on the test set
from sklearn.metrics import r2_score, mean_absolute_error

# These are the input variables the model will use to predict MetaScore
feature_cols = [
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

# X contains all of the information we give the model
X = df[feature_cols]

# y is what we want the model to predict
y = df["MetaScore"]

# convert bool to 1/0 so the model can use it
X = X.astype(float)

# Split the data:
# 80% is used to train the model
# 20% is hidden and used to test the model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining feature shape:")
print(X_train.shape)

print("\nTesting feature shape:")
print(X_test.shape)

# Create the Random Forest model
# n_estimators=200 means the forest will build 200 decision trees
# random_state=42 makes the results reproducible
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train the model on the training data
model.fit(X_train, y_train)

# Use the trained model to make predictions on the unseen test data
predictions = model.predict(X_test)

print("Model Training Complete.")

# Evaluate the model's performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"\nMean Absolute Error: {mae:.3f}")
print(f"R² Score: {r2:.3f}")

