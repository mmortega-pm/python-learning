import pandas as pd

data = {
    'Ticket_ID': [101, 102, 103, 104, 105, 106],
    'Priority': ['High', 'Low', 'High', 'Medium', 'Critical', 'High'],
    'Department': ['Eng', 'Sales', 'Eng', 'HR', 'Eng', 'Product'],
    'Days_Open': [5, 12, 1, 30, 2, 8]
}
df = pd.DataFrame(data)

print("--- Filter 1: Only Engineering ---")
# "Hey df, give me rows where df['Department'] is Eng"
print(df[df['Department'] == 'Eng']) 

print("\n--- Filter 2: Days Open > 5 ---")
print(df[df['Days_Open'] > 5])

print("\n--- Filter 3: Eng AND High Priority ---")
# Notice the parentheses around each condition! Crucial.
print(df[(df['Department'] == 'Eng') & (df['Priority'] == 'High')])