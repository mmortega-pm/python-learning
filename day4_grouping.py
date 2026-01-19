import pandas as pd

# 1. The Data (Notice we have two TPMs and two Engineers now)
data = {
    'Employee': ['Mauricio', 'Jake', 'Annie', 'Sophie', 'Carlos', 'Lionel'],
    'Role': ['TPM', 'Manager', 'Engineer', 'Analyst', 'TPM', 'Engineer'],
    'Salary': [120000, 150000, 110000, 135000, 125000, 115000]
}
df = pd.DataFrame(data)

# 2. The Grouping (The "Pivot Table" Step)
# SQL Equivalent: SELECT Role, AVG(Salary) FROM table GROUP BY Role;
avg_salary_by_role = df.groupby('Role')['Salary'].mean()

# 3. The Count (How many people in each role?)
# SQL Equivalent: SELECT Role, COUNT(*) FROM table GROUP BY Role;
count_by_role = df.groupby('Role')['Employee'].count()

print("--- Average Salary by Role ---")
print(avg_salary_by_role)

print("\n--- Headcount by Role ---")
print(count_by_role)