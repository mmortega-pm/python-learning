import pandas as pd

data = {
    'Department': ['Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales', 'Engineering'],
    'Budget': [150000, 80000, 200000, 50000, 100000, 120000]
}
df = pd.DataFrame(data)

print("\n--- Total Budget by Department ---")
print(df.groupby('Department')['Budget'].sum().reset_index().sort_values('Budget', ascending=False))