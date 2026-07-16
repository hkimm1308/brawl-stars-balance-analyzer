# Brawl Stars Balance Analyzer

An end-to-end machine learning project analyzing which gameplay characteristics contribute most to a Brawl Stars brawler’s competitive performance.

The project combines gameplay attributes, engineered mechanics, and rank-based performance data into a reusable machine learning pipeline. Its broader goal is to evaluate whether a brawler’s competitive strength can be estimated from design characteristics alone.

---

## Project Overview

The project follows a complete applied data science workflow:

* Collect and clean gameplay and performance data
* Validate and merge multiple datasets
* Engineer gameplay, combat, and mechanical features
* Perform exploratory data analysis
* Compare feature groups
* Train and tune regression models
* Evaluate models with cross-validation
* Perform systematic feature selection
* Visualize model performance and results

The long-term objective is to build a **New Brawler Predictor** capable of estimating the expected competitive strength of an unreleased brawler using only its design characteristics.

---

## Current Results

The project currently includes:

* A master dataset containing **103 brawlers and 107 columns**
* Rank-based performance data across Silver, Gold, Diamond, Mythic, Legendary, and Masters
* More than **70 engineered gameplay attributes**
* Reusable feature groups for core stats, combat, gameplay, mechanics, and categorical features
* Linear Regression and Random Forest baselines
* Random Forest hyperparameter tuning
* Five-fold cross-validation
* Feature-group ablation
* Leave-one-feature-out analysis
* Recursive feature elimination with cross-validation

The strongest current model uses a tuned Random Forest with six selected gameplay features.

### Best Selected Features

* Mobility Score
* Escape Score
* Positioning Importance
* Decision Complexity
* Skill Ceiling
* Survivability Score

RFECV reduced the gameplay feature set from 16 features to 6 while slightly improving cross-validated MAE.

---

## Model Performance

![Model performance comparison](charts/model_comparison.png)

Tree-based models substantially outperformed the Linear Regression baseline.

Current results include:

| Model                 |   MAE |
| --------------------- | ----: |
| Linear Regression     | 3.878 |
| Initial Random Forest | 1.618 |
| Tuned Random Forest   | 1.507 |
| RFECV Random Forest   | 1.498 |

The largest improvement came from replacing the linear model with a nonlinear tree-based model. Hyperparameter tuning and recursive feature elimination produced smaller but measurable improvements while reducing model complexity.

---

## Dataset

The final master dataset is located at:

```text
data/master_dataset.csv
```

Current dimensions:

```text
103 brawlers
107 columns
```

The dataset combines three main categories of information.

### Performance Data

For each rank:

* Win Rate
* Use Rate
* Meta Score

Ranks included:

* Silver
* Gold
* Diamond
* Mythic
* Legendary
* Masters

Derived performance metrics include:

* Average Meta Score
* Average Win Rate
* Average Use Rate
* Meta Score Standard Deviation
* Win Rate Standard Deviation
* Use Rate Standard Deviation
* Meta Score Range
* Win Rate Range
* Use Rate Range
* Meta Score Scaling
* Win Rate Scaling
* Use Rate Scaling

### Core Character Statistics

Examples include:

* Health
* Total Damage
* Effective Range
* Range Score
* Ammo Count
* Movement Speed
* Class
* Rarity

### Engineered Gameplay Features

Examples include:

* Mobility Score
* Engage Score
* Escape Score
* Aim Precision
* Positioning Importance
* Decision Complexity
* Mechanical Difficulty
* Skill Floor
* Skill Ceiling
* Area Control Score
* Lane Control Score
* Objective Pressure Score
* Team Utility Score
* Survivability Score
* Poke Pressure Score
* Close Range Threat Score

### Combat Features

Examples include:

* Reload Speed Score
* Attack Cooldown Score
* Projectile Speed Score
* Projectile Width Score
* Burst Damage Score
* Sustained DPS Score
* Super Charge Rate Score

### Binary Mechanics

Examples include:

* Dash
* Jump or Teleport
* Healing
* Stun
* Slow
* Knockback
* Pull
* Silence
* Shield
* Invisibility
* Pets or Summons
* Piercing
* Splash Damage
* Wall Break
* Area Control
* Bush Scouting

---

## Machine Learning

The primary prediction target is:

```text
MetaScoreScaling
```

This target measures how strongly a brawler’s competitive Meta Score changes across ranks.

### Linear Regression

The Linear Regression baseline performed poorly:

```text
MAE: 3.878
R²: approximately -2.08
```

This suggested that the relationship between gameplay characteristics and competitive performance is not adequately represented by a simple linear model.

### Random Forest

The initial Random Forest showed meaningful improvement:

```text
Single-split MAE: approximately 1.95
Single-split R²: approximately 0.09
```

Cross-validation later showed that the original single train-test split was optimistic.

### Tuned Random Forest

Randomized hyperparameter search identified the following model configuration:

```python
RandomForestRegressor(
    n_estimators=500,
    max_depth=2,
    min_samples_split=10,
    min_samples_leaf=1,
    max_features="log2",
    random_state=42,
)
```

The tuned gameplay-only model achieved:

```text
Cross-validated MAE: 1.5072
Cross-validated R²: 0.0881
```

### Recursive Feature Elimination

Recursive feature elimination with cross-validation selected six gameplay features:

```text
MobilityScore
EscapeScore
PositioningImportance
DecisionComplexity
SkillCeiling
SurvivabilityScore
```

The selected model achieved:

```text
Cross-validated MAE: 1.4975
```

This reduced the number of gameplay features by 62.5% while slightly improving predictive performance.

---

## Feature Analysis

### Feature-Group Ablation

Multiple feature groups were compared:

* Core Stats
* Combat
* Gameplay
* Mechanics
* Categories
* Combined feature sets
* All Features

The gameplay feature group consistently performed best.

The full feature set performed worse than the gameplay-only set, suggesting that additional variables introduced redundancy and noise.

### Leave-One-Feature-Out Analysis

Each gameplay feature was removed individually and the model was retrained.

The strongest negative impact occurred when removing:

```text
SurvivabilityScore
```

Removing Survivability Score increased MAE by approximately:

```text
0.0405
```

Other useful features included:

* Decision Complexity
* Objective Pressure Score
* Positioning Importance
* Mobility Score
* Team Utility Score

These experiments showed that some engineered gameplay scores contain meaningful predictive signal, while others appear redundant when used together.

---

## Exploratory Data Analysis

Completed analyses include:

* Correlation heatmap
* Class performance comparison
* Range-category analysis
* Health versus Win Rate
* Health versus Meta Score
* Gameplay mechanic comparisons
* Rank-based performance analysis
* Feature importance analysis
* Feature-group ablation
* Leave-one-feature-out analysis

These analyses helped identify relationships between gameplay mechanics and competitive performance while also highlighting the limitations of static character attributes.

---

## Project Workflow

```text
Collect Data
      ↓
Clean and Validate Data
      ↓
Engineer Gameplay Features
      ↓
Build Master Dataset
      ↓
Exploratory Data Analysis
      ↓
Baseline Modeling
      ↓
Cross-Validation
      ↓
Hyperparameter Tuning
      ↓
Feature-Group Ablation
      ↓
Leave-One-Feature-Out Analysis
      ↓
Recursive Feature Elimination
      ↓
Model Comparison
      ↓
Final Evaluation
```

---

## Project Structure

```text
brawl-stars-balance-analyzer/

├── charts/
│   ├── model_comparison.png
│   ├── correlation heatmap
│   ├── class analysis
│   ├── mechanic analysis
│   └── gameplay relationships
│
├── data/
│   ├── raw datasets
│   ├── cleaned datasets
│   ├── brawler_features_v3_ml_ready.csv
│   ├── performance_by_rank.csv
│   └── master_dataset.csv
│
├── results/
│   ├── leave_one_feature_out.csv
│   ├── rfecv_feature_rankings.csv
│   └── rfecv_performance_curve.csv
│
├── reports/
│   ├── EDA_Report.md
│   ├── Machine_Learning_Report.md
│   └── Dataset_v2_Plan.md
│
├── src/
│   ├── data_collection/
│   ├── data_processing/
│   ├── exploratory_analysis/
│   ├── feature_engineering/
│   ├── machine_learning/
│   │   ├── baseline_linear_regression.py
│   │   ├── random_forest_regression.py
│   │   ├── tune_random_forest.py
│   │   ├── feature_ablation.py
│   │   ├── leave_one_feature_out.py
│   │   ├── rfecv_feature_selection.py
│   │   └── feature_groups.py
│   │
│   └── visualization/
│       ├── model_comparison.py
│       └── __init__.py
│
├── .gitignore
└── README.md
```

---

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* BeautifulSoup
* Git
* GitHub

---

## Key Findings

### Gameplay features contain the strongest signal

Manually engineered gameplay scores consistently outperformed core statistics, combat features, mechanics, and categorical variables.

### More features do not always improve performance

The full feature set underperformed the gameplay-only feature set, suggesting that additional variables introduced redundancy and noise.

### Static characteristics explain only part of competitive performance

The models identified some predictive relationships, but overall performance remains limited.

Competitive strength likely also depends on factors such as:

* Map rotation
* Game mode
* Team composition
* Player behavior
* Balance updates
* Pick rate
* Counter relationships
* Meta changes over time

### Simpler models can generalize better

RFECV reduced the gameplay feature set from 16 features to 6 while slightly improving cross-validated MAE.

### Better data may matter more than model complexity

The primary limitation is not necessarily the choice of algorithm. Static character attributes alone may not contain enough information to accurately predict a constantly changing competitive meta.

---

## Remaining Work

### Model Comparison

Compare the current Random Forest against:

* Gradient Boosting Regressor
* HistGradientBoostingRegressor
* XGBoost

### Final Visualizations

Create:

* RFECV performance curve
* Final feature importance chart
* Final model comparison chart

### Documentation

* Update the machine learning report
* Add final conclusions
* Document model limitations
* Finalize resume and portfolio descriptions

---

## Long-Term Direction

A future version of the project could incorporate dynamic competitive data such as:

* Map-specific performance
* Game-mode-specific performance
* Team composition
* Matchup and counter data
* Balance-change history
* Time-series Meta Score
* Pick and ban rates
* Player skill distributions

These additions could support a more advanced system capable of predicting how a new or rebalanced brawler might perform within a specific competitive environment.

---

## Additional Documentation

For more detailed analyses, see:

* [Exploratory Data Analysis Report](reports/EDA_Report.md)
* [Machine Learning Report](reports/Machine_Learning_Report.md)
* [Dataset Version 2 Plan](reports/Dataset_v2_Plan.md)
