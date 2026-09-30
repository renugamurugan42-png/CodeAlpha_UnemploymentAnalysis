# Unemployment Analysis with Python

## 📌 Project Overview

This project analyzes unemployment rate data using Python. The analysis focuses on unemployment trends, the impact of the COVID-19 pandemic, monthly patterns, and regional differences in unemployment rates.

The project uses data cleaning, exploratory data analysis, and data visualization techniques to identify important patterns and insights.

## 🎯 Objectives

* Analyze unemployment rate data.
* Clean and prepare the dataset.
* Explore unemployment trends over time.
* Visualize unemployment rates using charts.
* Investigate the impact of COVID-19 on unemployment.
* Identify monthly and seasonal patterns.
* Compare unemployment rates across states and areas.
* Generate insights that can support economic and social policy planning.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook / VS Code

## 📂 Dataset

The project uses the **Unemployment in India** dataset containing unemployment-related information such as:

* Region / State
* Date
* Estimated Unemployment Rate
* Estimated Employed
* Labour Participation Rate
* Area

Dataset file used:
Unemployment_Rate_upto_11_2020.csv

## 🔍 Data Analysis Performed

### 1. Data Cleaning

* Removed unnecessary spaces from column names.
* Converted dates into datetime format.
* Removed duplicate records.
* Handled missing values.
* Created year and month columns.

### 2. Exploratory Data Analysis

Calculated:

* Average unemployment rate
* Minimum unemployment rate
* Maximum unemployment rate
* State-wise average unemployment
* Monthly unemployment patterns

### 3. Unemployment Trend Analysis

A time-series visualization was created to understand how unemployment changed over time.

### 4. COVID-19 Impact Analysis

The unemployment rate was compared across:

* Before COVID-19
* COVID-19 lockdown period
* After the initial lockdown period

This helps identify changes in unemployment during the pandemic.

### 5. State-wise Analysis

Average unemployment rates were compared across different states to identify regions with relatively higher or lower unemployment levels.

### 6. Urban vs Rural Analysis

The project also compares unemployment rates between urban and rural areas.

### 7. Labour Participation Analysis

The relationship between labour participation rate and unemployment rate is explored using a scatter plot.

## 📊 Visualizations

The project generates visualizations for:

* Overall unemployment trend
* COVID-19 impact
* Monthly unemployment pattern
* State-wise unemployment
* Top 10 states with high unemployment
* Urban vs rural unemployment
* Labour participation vs unemployment

## 💡 Key Insights

The analysis can help identify:

* Changes in unemployment during economic disruptions.
* The impact of COVID-19 on employment.
* Regions experiencing higher unemployment.
* Monthly variations in unemployment.
* Differences between urban and rural unemployment.
* The relationship between labour participation and unemployment.

## 🏛️ Policy Relevance

The findings can support economic and social planning by helping policymakers:

* Identify regions requiring employment support.
* Design targeted skill-development programmes.
* Plan employment-generation initiatives.
* Monitor unemployment trends regularly.
* Develop support measures during major economic disruptions.

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Open the Project

```bash
cd CodeAlpha_UnemploymentAnalysis
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 5: Run the Program

```bash
python unemployment_analysis.py
```

## 📁 Project Structure


CodeAlpha_UnemploymentAnalysis/
│
├── unemployment_analysis.py
├── Unemployment_Rate_upto_11_2020.csv
├── README.md
├── .gitignore
└── .venv/

## 👩‍💻 Author

RENUGA M

B.Tech Artificial Intelligence and Data Science
