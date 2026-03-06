import pandas as pd
import glob
import os

print("--- Day 50: Automated File Merging ---")

# 1. Setup: Creating two fragmented CSV files to simulate downloaded reports
pd.DataFrame({'Sprint': [1, 1], 'Task': ['API Spec', 'DB Design'], 'Hours': [10, 15]}).to_csv('sprint1_report.csv', index=False)
pd.DataFrame({'Sprint': [2, 2], 'Task': ['QA Testing', 'Deployment'], 'Hours': [8, 5]}).to_csv('sprint2_report.csv', index=False)

# 2. The Target: Use glob to find any file in the folder ending with '_report.csv'
file_list = glob.glob('*_report.csv')
print(f"Discovered {len(file_list)} files to merge: {file_list}")

# 3. The Merge: Read all files into a list, then concatenate them
df_list = [pd.read_csv(file) for file in file_list]
master_df = pd.concat(df_list, ignore_index=True)

print("\n--- Consolidated Master Report ---")
print(master_df.to_string(index=False))

# 4. Cleanup (Keeping your workspace clean)
os.remove('sprint1_report.csv')
os.remove('sprint2_report.csv')