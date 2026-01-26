import pandas as pd
import numpy as np

# 1. The Dirty Data
# 'np.nan' creates a fake missing value so we can test
data = {
    'Task': ['Design', 'Code', 'Test', 'Deploy'],
    'Owner': ['Mauricio', 'Jake', np.nan, 'Mauricio'], # Test has no owner!
    'Hours': [10, 20, 15, np.nan] # Deploy has no estimate!
}
df = pd.DataFrame(data)

print("--- Original Messy Data ---")
print(df)

# 2. Solution A: Fill the Blanks (The "Safe" Way)
# Great for text. Replaces NaN with "TBD" or "0"
df_filled = df.fillna('TBD')

print("\n--- Filled Data (Safe for Reports) ---")
print(df_filled)

# 3. Solution B: Drop the Rows (The "Strict" Way)
# If a row has ANY missing data, delete it entirely.
df_dropped = df.dropna()

print("\n--- Dropped Data (Strict) ---")
print(df_dropped)