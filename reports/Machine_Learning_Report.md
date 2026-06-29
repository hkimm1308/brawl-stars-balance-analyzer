# Machine Learning Report

## Objective

The objective of this phase was to determine whether gameplay characteristics can predict a brawler's Meta Score.

---

# Target Variable

Meta Score

---

# Features

Current features included:

- Health
- Damage
- Projectile Count
- Total Damage
- Skill Ceiling
- Gameplay mechanic flags

Examples:

- HasDash
- HasHealing
- HasShield
- HasStun
- HasSplashDamage

---

# Model

Random Forest Regressor

Dataset split:

- 80% Training
- 20% Testing

Evaluation metrics:

- Mean Absolute Error (MAE)
- R² Score

---

# Results

## Model A

Gameplay mechanics only

MAE:

1.98

R²:

-0.035

---

# Interpretation

Although the model performed poorly, this result was informative.

The model performed worse than predicting the average Meta Score.

Rather than indicating a poor algorithm choice, this suggests that the dataset currently lacks sufficient predictive information.

---

# Lessons Learned

The primary limitation is not the Random Forest model.

Instead, the dataset lacks many important gameplay features, including:

- Reload Speed
- DPS
- Attack Cooldown
- Projectile Speed
- Utility strength
- Mobility metrics

This shifted the focus of the project from improving algorithms to improving feature engineering.

---

# Next Steps

The next phase compares multiple feature sets.

Model A

Gameplay mechanics only

Model B

Gameplay mechanics + performance statistics

Model C

Performance statistics only

Comparing these models will help determine which types of information contribute most to accurate prediction.