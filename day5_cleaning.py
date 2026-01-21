import pandas as pd

# 1. The Dirty Data
# We have a missing salary for Sophie and a missing role for the new hire.
data = {
    'Employee': ['Mauricio', 'Jake', 'Annie', 'Sophie', 'NewGuy'],
    'Role': ['TPM', 'Manager', 'Engineer', 'Analyst', None],
    'Salary': [120000, 150000, 110000, None, 90000]
}
df = pd.DataFrame(data)

print("--- The Dirty Data ---")
print(df)

# 2. The Clean Up (SQL Equivalent: COALESCE or UPDATE)
# ACTION: Fill the 'Salary' column's empty spots with the average salary
# We use .mean() to get the number, then .fillna() to plug it in
avg_pay = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(avg_pay)

# ACTION: Fill the 'Role'column's empty spots with a text label
df['Role'] = df['Role'].fillna('TBD')

print("\n--- The Cleaned Data ---")
print(df)