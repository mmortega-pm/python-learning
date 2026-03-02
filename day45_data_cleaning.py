import pandas as pd
import numpy as np

print("--- Day 45: ETL Data Cleaning ---")

# 1. The Messy Real-World Data 
# Notice the missing dates and missing salary information
raw_data = {
    'Company': ['Amazon', 'Google', 'Microsoft', 'Meta', 'Apple'],
    'Role': ['TPM', 'Product Manager', 'Senior TPM', 'Program Manager', 'TPM'],
    'Status': ['Interview', 'Applied', 'Rejected', 'Applied', 'Offer'],
    'Interview_Date': ['2026-03-05', None, None, '2026-03-10', '2026-02-28'],
    'Expected_Salary': [180000, 195000, None, np.nan, 210000]
}

df = pd.DataFrame(raw_data)

print("\n--- The Problem: Raw Data with Nulls (NaN/None) ---")
print(df)

# 2. The Audit (Finding the holes)
print("\n--- Missing Data Count ---")
print(df.isna().sum())

# 3. The Cleanup Strategy
# Strategy A: Fill missing text with a logical default string
df['Interview_Date'] = df['Interview_Date'].fillna('TBD')

# Strategy B: Fill missing numbers with a safe placeholder (like 0) 
# This ensures it doesn't break math calculations in your dashboard
df['Expected_Salary'] = df['Expected_Salary'].fillna(0)

print("\n--- The Solution: Clean Dashboard-Ready Data ---")
print(df)