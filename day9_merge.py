import pandas as pd

# Table 1: The Project Status
projects_data = {
    'Project_ID': [101, 102, 103, 104],
    'Name': ['Alpha', 'Beta', 'Gamma', 'Delta'],
    'Status': ['Done', 'In Progress', 'Stuck', 'Done']
}
df_projects = pd.DataFrame(projects_data)

# Table 2: The Project Leads (Notice 'Project_ID' matches above)
leads_data = {
    'Project_ID': [101, 102, 104],
    'Lead': ['Mauricio', 'Amy', 'Mauricio']
    # Note: Project 103 (Gamma) has no lead assigned yet!
}
df_leads = pd.DataFrame(leads_data)

# 3. The Merge (Left Join)
# "how='left'" means: Keep ALL projects, even if they don't have a lead.
merged_df = pd.merge(df_projects, df_leads, on='Project_ID', how='left')

print("--- Master Project List ---")
print(merged_df)