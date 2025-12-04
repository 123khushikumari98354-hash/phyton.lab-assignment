  khushi kumari

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------
# Task 1: Load Dataset
# -----------------------------------------------

# Example dataset (if your real CSV is available, replace file name)
df = pd.read_csv("weather.csv")

print("\n--- HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())

# -----------------------------------------------
# Task 2: Cleaning & Preprocessing
# -----------------------------------------------

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Handle missing values
df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
df["rainfall"] = df["rainfall"].fillna(0)
df["humidity"] = df["humidity"].fillna(method="ffill")

# Extract month
df["month"] = df["date"].dt.month

# -----------------------------------------------
# Task 3: NumPy Statistical Analysis
# -----------------------------------------------

temps = df["temperature"].values

print("\n--- TEMPERATURE STATS ---")
print("Mean:", np.mean(temps))
print("Min:", np.min(temps))
print("Max:", np.max(temps))
print("Std Dev:", np.std(temps))

# Monthly statistics
monthly_stats = df.groupby("month")["temperature"].agg(["mean", "min", "max", "std"])
print("\n--- MONTHLY STATS ---")
print(monthly_stats)

# -----------------------------------------------
# Task 4: Visualizations
# -----------------------------------------------

# 1. Daily Temperature Line Chart
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("daily_temperature.png")
plt.close()

# 2. Monthly Rainfall Bar Chart
monthly_rain = df.groupby("month")["rainfall"].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall")
plt.xlabel("Mo
