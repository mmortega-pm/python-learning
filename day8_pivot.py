import pandas as pd

# 1. The Data (Adding a 'Region' column)
data = {
    'Employee': ['Mauricio', 'Jake', 'Annie', 'Sophie', 'Carlos', 'Lionel'],
    'Role': ['TPM', 'Manager', 'Engineer', 'Analyst', 'TPM', 'Engineer'],
    'Region': ['US', 'US', 'US', 'EU', 'EU', 'EU'],
    'Salary': [120000, 150000, 110000, 135000, 125000, 115000]
}
df = pd.DataFrame(data)

# 2. The Pivot Table
# index = Rows
# columns = Columns
# values = The numbers to crunch
# aggfunc = The math to do (mean, sum, count)
pivot = df.pivot_table(index='Role', columns='Region', values='Salary', aggfunc='mean')

print("--- Salary by Role & Region ---")
print(pivot)