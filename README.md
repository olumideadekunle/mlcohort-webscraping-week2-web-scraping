# Week 2 — Web Scraping Project

Cohort: ML Flipped Cohort  
Author: Olumide Buari  

## Objective
Scrape data from a publicly available website for use in future machine learning projects.  

## Tools
- Python 3
- Requests
- BeautifulSoup4 (or Selenium)

## Dataset Source
- Website: <link of the website you scraped>  

## How to run
```bash
pip install -r requirements.txt
python scrape.py









README.md
Week 3: Database Querying & Exploratory Data Analysis (EDA)
📊 Dataset Used

For this assignment, I used the Titanic Survival Dataset
 from Kaggle.
This dataset contains passenger details such as age, sex, ticket class, and whether they survived.

🧹 Data Cleaning

Removed missing/null values in Age and Embarked columns.

Converted categorical features (Sex, Embarked) into numeric form for analysis.

Standardized column names for readability.

🔍 Exploratory Data Analysis (EDA)

Key insights from the dataset:

Most passengers were in 3rd class, but the survival rate was highest in 1st class.

Females had a higher survival rate than males.

Younger passengers (children) had a higher chance of survival.

The Fare distribution was skewed, with a few very expensive tickets.

📈 Visualizations

Bar chart of survival rate by gender.

Histogram of passenger ages.

Boxplot of fare vs. passenger class.

✅ Conclusion

The Titanic dataset shows that gender, age, and passenger class were strong indicators of survival chances.
