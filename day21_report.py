import pandas as pd

# 1. The Raw Data (The Weeds)
data = {
    'Project': ['Alpha', 'Alpha', 'Beta', 'Beta', 'Gamma'],
    'Expense_Type': ['Software', 'Hardware', 'Software', 'Travel', 'Software'],
    'Cost': [1000, 5000, 2000, 1500, 3000]
}
df_raw = pd.DataFrame(data)

# 2. The Summary (Pivot Table for the Boss)
# Group by Project to get total costs
df_summary = df_raw.groupby('Project')['Cost'].sum().reset_index()

print("--- Generating Multi-Tab Report ---")

# 3. The Writer Logic
# We use a 'with' block to safely open and save the file
with pd.ExcelWriter('project_financials.xlsx', engine='openpyxl') as writer:
    
    # Write the Summary to the first tab (Managers look here first)
    df_summary.to_excel(writer, sheet_name='Executive Summary', index=False)
    
    # Write the Details to the second tab
    df_raw.to_excel(writer, sheet_name='Raw Data', index=False)

print("Success! File 'project_financials.xlsx' created.")