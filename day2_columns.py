import pandas as pd

# 1. Create our data again
data = {
    'Employee': ['Mauricio', 'Jake', 'Annie'],
    'Role': ['TPM', 'Manager', 'Engineer'],
    'Salary': [120000, 150000, 110000]
}
df = pd.DataFrame(data)

# 2. The Magic: Vectorization
# We add a new column 'Bonus' by multiplying the whole 'Salary' column by 10%
# No loops. No "for i in rows. Jusrt one line.
df['Bonus'] = df['Salary'] * 0.10

# 3. Filter the data (The "WHERE" clause)
# Show me only people who earn more than 115k
high_earners = df[df['Salary'] > 115000]

print("--- Full Table with Bonus ---")
print(df)

print("\n--- High Earners Only ---")
print(high_earners)