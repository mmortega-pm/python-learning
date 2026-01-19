import pandas as pd

# 1. The Data (Added a 4th person to make sorting more interesting)
data = {
    'Employee': ['Mauricio', 'Jake', 'Annie', 'Sophie'],
    'Role': ['TPM', 'Manager', 'Engineer', 'Analyst'],
    'Salary': [120000, 150000, 110000, 135000]
}
df = pd.DataFrame(data)

# 2. The Sort
# 'ascending=False' means Highest to Lowest
sorted_df = df.sort_values(by='Salary', ascending=False)

# 3. The Output
print("--- Salary Leaderboard ---")
print(sorted_df)