# 🏏 IPL 2022 Capstone Project – Data Analysis

## 📌 Project Overview

This project analyzes **IPL 2022 match-level data** to uncover insights related to team performance, toss decisions, winning patterns, and match outcomes. The analysis demonstrates practical Exploratory Data Analysis (EDA) skills using Python and data visualization libraries.

## 📂 Dataset Information

* **Tournament:** Indian Premier League (IPL) 2022
* **Data Source:** Match-level CSV dataset (`IPL.csv`)
* **Rows & Columns:** Derived programmatically using pandas
* **Key Columns:**

  * match_id
  * team1, team2
  * match_winner
  * toss_winner
  * toss_decision
  * venue
  * won_by (Runs / Wickets)

## 🛠 Tools & Technologies

* **Python**
* **Pandas & NumPy** – Data manipulation
* **Matplotlib & Seaborn** – Data visualization
* **Jupyter Notebook** – Analysis environment

## 🧹 Data Loading & Understanding

* Imported dataset using `pandas.read_csv()`
* Inspected data structure with `df.head()` and `df.info()`
* Checked dataset shape and missing values using `df.shape` and `df.isnull().sum()`

## 📊 Exploratory Data Analysis (EDA)

The following analytical questions were explored in the notebook:

### 1️⃣ Which team won the most matches?

* Calculated win counts using `value_counts()`
* Identified top-performing teams of IPL 2022

### 2️⃣ Toss Decision Trends

* Analyzed frequency of **Bat vs Field** decisions
* Visualized toss decisions using count plots

### 3️⃣ Toss Winner vs Match Winner

* Compared toss winners with match winners
* Measured how often winning the toss leads to winning the match

### 4️⃣ How Do Teams Win? (Runs vs Wickets)

* Studied win types based on runs and wickets
* Identified dominant winning strategies

## 📈 Visualizations

* Bar charts for team-wise wins
* Count plots for toss decisions and win types
* All visualizations created using **Seaborn & Matplotlib**

## 🔍 Key Insights

* A few teams consistently dominated the season
* Fielding after winning the toss was a common strategy
* Winning the toss did not always guarantee match victory
* Win-by-wickets was more frequent than win-by-runs

## ✅ Conclusion

This project highlights strong **EDA, data visualization, and analytical thinking skills** using real sports data. It is well-suited for showcasing hands-on experience in **Data Analyst and Data Scientist portfolios**.

---

📌 *Notebook-based project converted into a clean, professional README.md for GitHub and resume use.*
