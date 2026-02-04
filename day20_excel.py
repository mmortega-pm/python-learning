import pandas as pd

# --- PART 1: Create a Dummy Excel File ---
data = {
    'Task': ['Scope Refinement', 'Stakeholder Meeting', 'Budget Approval'],
    'Owner': ['Mauricio', 'Wil', 'Derick'],
    'Status': ['Done', 'Pending', 'Blocked']
}
df_create = pd.DataFrame(data)

# 'index=False' removes the annoying 0,1,2 row numbers
df_create.to_excel('project_tracker.xlsx', index=False)
print("Files created: project_tracker.xlsx")


# --- PART 2: The Actual Skill (Reading it) ---
print("\n--- Reading Excel File ---")

# engine='openpyxl' is the secret key for .xlsx files
df_loaded = pd.read_excel('project_tracker.xlsx', engine='openpyxl')

print(df_loaded)