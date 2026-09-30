import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 1. LOAD DATASET
# ---------------------------------------------------------

df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

print("\n========== ORIGINAL DATASET ==========")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)


# ---------------------------------------------------------
# 2. DATA CLEANING
# ---------------------------------------------------------

# Remove unwanted spaces from column names
df.columns = df.columns.str.strip()

# Rename columns for easy use
df.rename(columns={
    "Region": "State",
    "Date": "Date",
    "Frequency": "Frequency",
    "Estimated Unemployment Rate (%)": "Unemployment_Rate",
    "Estimated Employed": "Employed",
    "Estimated Labour Participation Rate (%)": "Labour_Participation_Rate",
    "Area": "Area"
}, inplace=True)

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(
    df["Date"].astype(str).str.strip(),
    dayfirst=True,
    errors="coerce"
)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Display missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Remove rows containing missing important values
df.dropna(
    subset=["Date", "Unemployment_Rate"],
    inplace=True
)

# Create Year and Month columns
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()

print("\n========== CLEANED DATA ==========")
print(df.head())


# ---------------------------------------------------------
# 3. BASIC EXPLORATORY DATA ANALYSIS
# ---------------------------------------------------------

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\nAverage Unemployment Rate:")
print(round(df["Unemployment_Rate"].mean(), 2), "%")

print("\nMaximum Unemployment Rate:")
print(round(df["Unemployment_Rate"].max(), 2), "%")

print("\nMinimum Unemployment Rate:")
print(round(df["Unemployment_Rate"].min(), 2), "%")


# ---------------------------------------------------------
# 4. OVERALL UNEMPLOYMENT TREND
# ---------------------------------------------------------

monthly_trend = (
    df.groupby("Date")["Unemployment_Rate"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=monthly_trend,
    x="Date",
    y="Unemployment_Rate",
    marker="o"
)

plt.title("Unemployment Rate Trend in India")
plt.xlabel("Date")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 5. COVID-19 IMPACT ANALYSIS
# ---------------------------------------------------------

pre_covid = df[df["Date"] < "2020-03-01"]

covid_period = df[
    (df["Date"] >= "2020-03-01") &
    (df["Date"] <= "2020-06-30")
]

post_lockdown = df[df["Date"] > "2020-06-30"]

pre_covid_rate = pre_covid["Unemployment_Rate"].mean()
covid_rate = covid_period["Unemployment_Rate"].mean()
post_covid_rate = post_lockdown["Unemployment_Rate"].mean()

print("\n========== COVID-19 IMPACT ==========")

print(
    "Average Unemployment Rate Before Covid:",
    round(pre_covid_rate, 2),
    "%"
)

print(
    "Average Unemployment Rate During Covid Lockdown:",
    round(covid_rate, 2),
    "%"
)

print(
    "Average Unemployment Rate After Initial Lockdown:",
    round(post_covid_rate, 2),
    "%"
)


covid_comparison = pd.DataFrame({
    "Period": [
        "Before Covid",
        "Covid Lockdown",
        "After Initial Lockdown"
    ],
    "Unemployment Rate": [
        pre_covid_rate,
        covid_rate,
        post_covid_rate
    ]
})

plt.figure(figsize=(8, 5))

sns.barplot(
    data=covid_comparison,
    x="Period",
    y="Unemployment Rate"
)

plt.title("Impact of Covid-19 on Unemployment")
plt.xlabel("Period")
plt.ylabel("Average Unemployment Rate (%)")

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 6. MONTHLY / SEASONAL TREND
# ---------------------------------------------------------

monthly_average = (
    df.groupby(
        ["Month", "Month_Name"]
    )["Unemployment_Rate"]
    .mean()
    .reset_index()
    .sort_values("Month")
)

plt.figure(figsize=(10, 6))

sns.lineplot(
    data=monthly_average,
    x="Month_Name",
    y="Unemployment_Rate",
    marker="o"
)

plt.title("Monthly Pattern of Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 7. STATE-WISE UNEMPLOYMENT ANALYSIS
# ---------------------------------------------------------

state_unemployment = (
    df.groupby("State")["Unemployment_Rate"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

print("\n========== STATE-WISE UNEMPLOYMENT ==========")
print(state_unemployment)

plt.figure(figsize=(12, 8))

sns.barplot(
    data=state_unemployment,
    x="Unemployment_Rate",
    y="State"
)

plt.title("Average Unemployment Rate by State")
plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("State")

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 8. TOP 10 STATES WITH HIGH UNEMPLOYMENT
# ---------------------------------------------------------

top_10_states = state_unemployment.head(10)

print("\n========== TOP 10 STATES ==========")
print(top_10_states)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_10_states,
    x="Unemployment_Rate",
    y="State"
)

plt.title("Top 10 States with Highest Average Unemployment")
plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("State")

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 9. AREA ANALYSIS - URBAN VS RURAL
# ---------------------------------------------------------

if "Area" in df.columns:

    area_analysis = (
        df.groupby("Area")["Unemployment_Rate"]
        .mean()
        .reset_index()
    )

    print("\n========== URBAN VS RURAL ==========")
    print(area_analysis)

    plt.figure(figsize=(7, 5))

    sns.barplot(
        data=area_analysis,
        x="Area",
        y="Unemployment_Rate"
    )

    plt.title("Urban vs Rural Unemployment Rate")
    plt.xlabel("Area")
    plt.ylabel("Average Unemployment Rate (%)")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 10. LABOUR PARTICIPATION ANALYSIS
# ---------------------------------------------------------

if "Labour_Participation_Rate" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x="Labour_Participation_Rate",
        y="Unemployment_Rate"
    )

    plt.title(
        "Labour Participation Rate vs Unemployment Rate"
    )

    plt.xlabel(
        "Labour Participation Rate (%)"
    )

    plt.ylabel(
        "Unemployment Rate (%)"
    )

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 11. KEY INSIGHTS
# ---------------------------------------------------------

highest_state = state_unemployment.iloc[0]

highest_month = monthly_average.loc[
    monthly_average["Unemployment_Rate"].idxmax()
]

print("\n==========================================")
print("           KEY INSIGHTS")
print("==========================================")

print(
    "\n1. The average unemployment rate increased"
    " significantly during the Covid-19 lockdown period."
)

print(
    "\n2. Average unemployment before Covid was:",
    round(pre_covid_rate, 2),
    "%"
)

print(
    "   During the lockdown it increased to:",
    round(covid_rate, 2),
    "%"
)

print(
    "\n3. State with the highest average unemployment:"
)

print(
    highest_state["State"],
    "-",
    round(highest_state["Unemployment_Rate"], 2),
    "%"
)

print(
    "\n4. Month with the highest average unemployment:"
)

print(
    highest_month["Month_Name"],
    "-",
    round(highest_month["Unemployment_Rate"], 2),
    "%"
)

print(
    "\n5. The analysis shows that economic shocks such as"
    " Covid-19 can cause sudden increases in unemployment."
)

print(
    "\n6. Regions with persistently high unemployment may"
    " require targeted employment and skill-development"
    " programmes."
)

print(
    "\n7. Policymakers can use unemployment trends to"
    " identify vulnerable regions and plan employment"
    " support programmes."
)

print(
    "\n8. Monitoring monthly unemployment can help"
    " governments respond faster to economic disruptions."
)

print("\n==========================================")
print("        ANALYSIS COMPLETED")
print("==========================================")