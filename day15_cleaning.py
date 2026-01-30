import pandas as pd

data = {
    'Project': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'],
    'Status': ['Green', None, 'Red', 'Green', None],
    'Budget': [10000, 5000, None, 12000, 8000],
    'Owner': ['T. Stark', 'S. Rogers', 'N. Romanoff', None, 'B. Banner']
}
df = pd.DataFrame(data)

print("--- Task 1: Rows with ANY Missing Data ---")
print(df[df.isna().any(axis=1)])

print("\n--- Task 2: Status Filled with 'Draft' ---")
df_filled = df.fillna({'Status': 'Draft'})
print(df_filled)

print("\n--- Task 3: Rows with Valid Budget Only ---")
df_clean = df.dropna(subset=['Budget'])
print(df_clean)