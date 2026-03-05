import pandas as pd

print("--- Day 49: Date Math and Cycle Times ---")

# 1. The Raw Data (Dates are just text strings right now)
pipeline_data = {
    'Company': ['Amazon', 'Google', 'Microsoft', 'Meta'],
    'Role': ['TPM', 'Senior TPM', 'Product Manager', 'Program Manager'],
    'Applied_Date': ['2026-02-15', '2026-02-28', '2026-03-01', '2026-01-20'],
    'Status': ['Interview', 'Applied', 'Applied', 'Rejected']
}

df = pd.DataFrame(pipeline_data)

# 2. The Conversion
# Transform the text strings into actual Pandas datetime objects
df['Applied_Date'] = pd.to_datetime(df['Applied_Date'])

# 3. Establish the baseline (Today's Date)
df['Today'] = pd.to_datetime('2026-03-05') 

# 4. The Math: Calculate 'Days_Active'
# Subtracting the dates, then extracting just the integer value
df['Days_Active'] = (df['Today'] - df['Applied_Date']).dt.days

# 5. The Polish
# Drop the 'Today' column since we only needed it for the math, 
# and sort the table to show the oldest items at the top.
df = df.drop(columns=['Today'])
df = df.sort_values(by='Days_Active', ascending=False)

print("\n--- Pipeline Aging Report ---")
print(df.to_string(index=False))