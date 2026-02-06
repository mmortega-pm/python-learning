import pandas as pd

# --- SETUP: Creating a messy file to simulate work ---
data = {
    'Department': ['Sales', 'Sales', 'Eng', 'Eng', 'HR'],
    'Employee': ['Jim', 'Dwight', 'Pam', 'Toby', 'Michael'],
    'Bonus': [1000, 2000, None, 500, None] # <--- Note the missing data
}
df_setup = pd.DataFrame(data)
df_setup.to_excel('raw_payroll.xlsx', index=False)
print("Setup Complete: 'raw_payroll.xlsx' created.")


print("\n--- PROCESSING REPORT ---")

# TODO 1: Read 'raw_payroll.xlsx' into a variable called df
# Hint: use pd.read_excel() and remember the engine='openpyxl'
df_raw = pd.read_excel('raw_payroll.xlsx', engine='openpyxl')

# TODO 2: Fill the missing Bonus values with 0
# Hint: use .fillna()
df_clean = df_raw.fillna({'Bonus': 0})

# TODO 3: Create a summary table (Group by Dept, sum the Bonus)
# Hint: .groupby('Department')['Bonus'].sum().reset_index()
df_summary = df_clean.groupby('Department')['Bonus'].sum().reset_index()


print("--- WRITING FINAL REPORT ---")
# This part I'll give you, since the syntax is tricky
with pd.ExcelWriter('final_payroll_report.xlsx', engine='openpyxl') as writer:
    df_summary.to_excel(writer, sheet_name='Summary', index=False)
    df_clean.to_excel(writer, sheet_name='Clean Data', index=False)

print("Success! Check 'final_payroll_report.xlsx'")