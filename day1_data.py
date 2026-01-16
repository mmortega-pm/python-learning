import pandas as pd

# 1. Create raw data (This is a Dictionary)
# Think of this like manually typing rows into Excel
raw_data = {
    'Employee': ['Mauricio', 'Jake', 'Annie'],
    'Role': ['TPM', 'Manager', 'Engineer'],
    'Salary': [120000, 150000, 110000]
}

# 2. Convert it to a DataFrame (The Magic Step)
# This turns the raw list into a smart table
df = pd.DataFrame(raw_data)

# 3. Show the table
print("--- My First DataFrame ---")
print(df)

# 4. Do a quick calculation (The "SQL" part)
# This is like SELECT AVG(Salary)
print("\n--- Average Salary ---")
print(df['Salary'].mean())