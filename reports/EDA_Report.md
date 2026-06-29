# Exploratory Data Analysis Report

## Objective

The goal of this project is to better understand what gameplay characteristics contribute to a brawler's overall competitive strength in Brawl Stars.

Using a merged dataset containing performance statistics, gameplay attributes, and engineered gameplay mechanics, I explored relationships between variables before beginning machine learning.

---

# Dataset

Current dataset contains approximately 100 brawlers with features including:

### Performance

- Win Rate
- Use Rate
- Meta Score
- Rank

### Gameplay Attributes

- Health
- Damage
- Projectile Count
- Damage per Projectile
- Total Damage
- Class
- Movement Speed
- Range Category
- Rarity

### Gameplay Mechanics

- Dash
- Healing
- Stun
- Slow
- Splash Damage
- Wall Break
- Shield
- Piercing
- Knockback
- Area Control
- Pets
- Invisibility
- Attack Style
- Super Type
- Skill Ceiling

---

# Analyses Performed

## Correlation Analysis

A correlation heatmap was generated to understand relationships between numerical variables.

Key observations:

- Meta Score and Win Rate showed only a weak positive relationship.
- Health showed little correlation with Meta Score.
- Damage-related statistics were highly correlated with one another, as expected.

---

## Class Analysis

Average Meta Score was calculated for each brawler class.

This analysis highlighted which classes generally perform better in the current game balance.

---

## Gameplay Mechanics Analysis

Average Meta Score was compared between brawlers that possess certain mechanics and those that do not.

Examples:

- Healing
- Stun
- Dash
- Shield
- Wall Break
- Splash Damage

This helped identify mechanics that appear more frequently among stronger brawlers.

---

## Health Analysis

Scatter plots were created showing:

- Health vs Win Rate
- Health vs Meta Score

These visualizations demonstrated that higher health alone does not strongly predict competitive success.

---

# Key Findings

## 1. Win Rate alone does not explain Meta Score.

Competitive strength appears to depend on many additional gameplay characteristics.

---

## 2. Binary gameplay mechanics provide useful information.

Mechanics such as stun, healing, and mobility appear to influence Meta Score.

---

## 3. Many variables have weak individual relationships.

This suggests Meta Score is influenced by many interacting factors rather than a single dominant statistic.

---

# Conclusion

Exploratory data analysis provided valuable insight into the structure of the dataset and informed the transition into machine learning.

More importantly, it identified opportunities for richer feature engineering that will improve future predictive models.