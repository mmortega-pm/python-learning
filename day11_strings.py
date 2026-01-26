import pandas as pd

data = {
    'Employee': ['  Mauricio  ', 'Jake', 'Annie'], # Extra spaces
    'Salary_Text': ['$120,000', '$150,000', '$110,000'] # Symbols
}
df = pd.DataFrame(data)

print("--- Dirty Data ---")
print(df)

# 1. Clean the Names (Strip whitespace)
# .str accessor lets you use string methods on the whole column
df['Employee'] = df['Employee'].str.strip()

# 2. Clean the Money (Remove '$' and ',')
# We replace '$' with nothing, and ',' with nothing
df['Salary_Text'] = df['Salary_Text'].str.replace('$', '').str.replace(',', '')

# 3. Convert to Real Numbers
# Now that it looks like "120000", we can turn it into an integer
df['Salary_Num'] = pd.to_numeric(df['Salary_Text'])

print("\n--- Cleaned Data ---")
print(df)
print(f"\nAverage Salary: ${df['Salary_Num'].mean():,.0f}")