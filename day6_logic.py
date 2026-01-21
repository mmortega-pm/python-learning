import pandas as pd

# 1. The Data
data = {
    'Employee': ['Mauricio', 'Jake', 'Annie', 'Sophie'],
    'Role': ['TPM', 'Manager', 'Engineer', 'Analyst'],
    'Salary': [120000, 150000, 110000, 95000]
}
df = pd.DataFrame(data)

# 2. Define the Logic (The "Mini-Program")
# logic: If salary > 120k, they are "High Tier". Otherwise "Standard Tier".
def classify_salary(salary):
    if salary > 120000:
        return 'High Tier'
    else:
        return 'Standard Tier'

# 3. Apply the Logic
# ACTION: Run 'classify_salary' on every number in the 'Salary' column
df['Tier'] = df['Salary'].apply(classify_salary)

print("--- Categorized Data ---")
print(df)