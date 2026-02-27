import pandas as pd

print("--- Executing Data Merge ---")

# 1. Table A: The Project Backlog
tasks = pd.DataFrame({
    'Task_ID': [101, 102, 103, 104],
    'Description': ['Update Looker Dashboard', 'Database Migration', 'API Integration', 'Write Documentation'],
    'Owner_ID': [7, 3, 3, 9]
})

# 2. Table B: The Team Roster
team = pd.DataFrame({
    'Emp_ID': [3, 7, 9],
    'Name': ['Sarah', 'Mauricio', 'David'],
    'Role': ['Backend Eng', 'TPM', 'Tech Writer']
})

# 3. The Merge (The Python JOIN)
# We are linking the 'Owner_ID' from the tasks table to the 'Emp_ID' in the team table.
merged_report = pd.merge(tasks, team, left_on='Owner_ID', right_on='Emp_ID', how='left')

# 4. Clean up the redundancy
# We don't need both ID columns in the final report, so we drop one.
merged_report = merged_report.drop(columns=['Emp_ID'])

print("\n--- Final Consolidated Report ---")
print(merged_report.to_string(index=False))