# Brawl Stars Balance Analyzer

A Python data science project exploring Brawl Stars balance, meta rankings, and gameplay characteristics.

## Project Overview

This project analyzes Brawl Stars performance data to identify:

- Underused brawlers
- Overused brawlers
- Relationships between win rate and meta rankings
- Factors that contribute to brawler strength

## Current Datasets

### Performance Dataset

Contains:

- Rank
- Name
- WinRate
- UseRate
- MetaScore

### Attributes Dataset

Contains:

- Name
- Class
- Health
- RangeCategory

## Key Findings

### 1. MetaScore and WinRate Are Weakly Related

Correlation:

```text
0.184
```

This suggests MetaScore captures factors beyond raw win rate.

### 2. Tanks Have High Win Rates

Tanks have the highest average win rate among analyzed classes.

### 3. Range Influences MetaScore

Very-long-range brawlers have higher average MetaScores despite lower win rates.

## Technologies

- Python
- Pandas
- Matplotlib
- Git
- GitHub

## Future Work

- Additional attributes
- Machine learning models
- MetaScore prediction
- Feature importance analysis
