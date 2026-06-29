# Brawl Stars Balance Analyzer

An end-to-end machine learning project exploring what makes a Brawl Stars brawler strong.

The goal of this project is to investigate which gameplay characteristics contribute most to a brawler's success, engineer meaningful features from game mechanics, and build machine learning models capable of predicting overall competitive strength.

---

## Project Goals

This project follows a complete data science workflow:

- Collect gameplay and performance data
- Clean and validate datasets
- Engineer meaningful gameplay features
- Perform exploratory data analysis
- Visualize trends and relationships
- Train and evaluate machine learning models
- Improve the dataset through iterative feature engineering

Ultimately, the long-term goal is to predict the expected strength of an entirely new brawler before release using only its design characteristics.

---

## Current Results

- Built a merged dataset containing gameplay, attribute, and performance data for over 100 brawlers.
- Engineered 15+ gameplay mechanic features.
- Created multiple exploratory visualizations including class analysis, health analysis, and a correlation heatmap.
- Trained an initial Random Forest regression model to predict Meta Score.
- Identified feature engineering as the primary limitation to predictive performance, and made a plan to enrich the dataset.

---

## Data Sources

The project combines multiple datasets into one machine learning dataset.

### Performance Data

- Win Rate
- Use Rate
- Meta Score
- Overall Rank

### Gameplay Attributes

- Class
- Health
- Damage
- Projectile Count
- Damage per Projectile
- Total Damage
- Movement Speed
- Range Category
- Rarity

### Engineered Gameplay Features

Binary gameplay mechanics including:

- Dash
- Healing
- Stun
- Slow
- Shield
- Wall Break
- Splash Damage
- Piercing
- Knockback
- Area Control
- Pets
- Invisibility

Additional engineered features include:

- Attack Style
- Super Type
- Skill Ceiling

---

## Project Workflow

```
Collect Data
      ↓
Clean Data
      ↓
Feature Engineering
      ↓
Dataset Validation
      ↓
Exploratory Data Analysis
      ↓
Visualization
      ↓
Machine Learning
      ↓
Model Evaluation
      ↓
Feature Engineering Improvements
```

---

## Current Project Structure

```
brawl-stars-balance-analyzer/

├── data/
│   ├── raw datasets
│   ├── cleaned datasets
│   └── brawler_final_dataset.csv
│
├── src/
│   ├── data collection
│   ├── data cleaning
│   ├── feature engineering
│   ├── exploratory analysis
│   ├── visualization
│   └── machine learning
│
├── charts/
│   ├── correlation heatmap
│   ├── class analysis
│   ├── mechanic analysis
│   ├── health relationships
│   └── additional visualizations
│
├── reports/
│   ├── EDA_Report.md
│   ├── Machine_Learning_Report.md
│   └── Feature_Engineering_Notes.md
│
└── README.md
```

---

## Exploratory Data Analysis

Current analyses include:

- Correlation heatmap
- Class performance analysis
- Range analysis
- Gameplay mechanic analysis
- Health vs. Win Rate
- Health vs. Meta Score
- Feature correlation analysis

These analyses helped identify relationships between gameplay characteristics and competitive performance while also revealing limitations within the dataset.

---

## Machine Learning

Current target:

**Meta Score**

Current model:

- Random Forest Regressor

Evaluation metrics:

- Mean Absolute Error (MAE)
- R² Score

Initial results demonstrated that the current feature set is insufficient for accurate prediction. Rather than indicating a poor algorithm choice, this finding highlights the importance of richer feature engineering and higher-quality input data.

This insight guides the next phase of the project.

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Git
- GitHub

---

## Future Work

### Short Term

- Compare multiple machine learning models
- Evaluate different feature sets
- Analyze feature importance
- Improve project documentation

### Long Term

Build Version 2 of the dataset with richer gameplay features including:

- Reload Speed
- Attack Cooldown
- DPS
- Projectile Speed
- Healing Amount
- Shield Strength
- Stun Duration
- Mobility metrics
- Utility metrics

The final objective is to develop a **New Brawler Predictor** capable of estimating a brawler's expected competitive strength before release based solely on its design characteristics.

---

## Key Takeaways

This project has evolved from a simple exploratory data analysis into a complete machine learning pipeline emphasizing:

- Data collection
- Feature engineering
- Statistical analysis
- Visualization
- Predictive modeling
- Iterative model improvement

One of the most important findings so far is that **better data is often more valuable than a more complex algorithm**, reinforcing the central role of feature engineering in successful machine learning projects.

## Additional Documentation

For more detailed analyses, see:

- [Exploratory Data Analysis Report](reports/EDA_Report.md)
- [Machine Learning Report](reports/Machine_Learning_Report.md)
- [Dataset Version 2 Plan](reports/Dataset_v2_Plan.md)
