import pandas as pd
from datetime import datetime

print("--- Day 48: Automated Dashboard Export ---")

# 1. The Clean Data (Simulating the final output of your ETL pipeline)
clean_data = {
    'Company': ['Amazon', 'Google', 'Microsoft', 'Meta'],
    'Role': ['TPM', 'Product Manager', 'Senior TPM', 'Program Manager'],
    'Status': ['Interview', 'Applied', 'Rejected', 'Applied'],
    'Days_Active': [14, 2, 21, 5]
}

df = pd.DataFrame(clean_data)

# 2. Generate a dynamic timestamp
# This grabs the exact current date and formats it as YYYY-MM-DD
today_str = datetime.now().strftime('%Y-%m-%d')
filename = f"pipeline_export_{today_str}.csv"

print(f"1. Assembling final DataFrame...")
print(f"2. Generating dynamic filename: {filename}")

# 3. The Export Command
# index=False is crucial here. It prevents Pandas from exporting the 
# meaningless row numbers (0, 1, 2) into your clean Looker dataset.
df.to_csv(filename, index=False)

print("\n[SUCCESS] Pipeline export complete. File is ready for Looker Studio ingestion.")