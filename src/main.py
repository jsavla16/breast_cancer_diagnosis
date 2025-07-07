# src/main.py

# 1. Load Dataset
import pandas as pd
import os

# Define the path to the dataset
DATA_PATH = os.path.join("data", "breast_cancer.csv")

# Load the dataset
try:
    df = pd.read_csv(DATA_PATH)
    print("✅ Data loaded successfully.")
except FileNotFoundError:
    print(f"❌ File not found at {DATA_PATH}")
    exit(1)

# Display basic info
print("\n📊 Dataset Preview:")
print(df.head())

print("\n🔍 Dataset Info:")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())
