import pandas as pd
from datetime import datetime

print("--- Generating Looker Studio Export ---")

# 1. The Raw Data (Your Job Search Tracker)
data = {
    'Company': ['Amazon', 'Microsoft', 'Google', 'Spotify', 'Meta'],
    'Role': ['Technical Program Manager', 'Senior TPM', 'Product Manager', 'TPM', 'Program Manager'],
    'Application_Date': ['2026-02-10', '2026-02-12', '2026-02-15', '2026-02-18', '2026-02-22'],
    'Status': ['Interview', 'Rejected', 'Phone Screen', 'Applied', 'Applied']
}

# 2. Load into Pandas
df = pd.DataFrame(data)

# 3. The Transformation (Cleaning the data for the dashboard)
# Looker Studio needs dates to be actual datetime objects, not just text.
df['Application_Date'] = pd.to_datetime(df['Application_Date'])

# Let's add a column that calculates how many days ago you applied
today = pd.to_datetime(datetime.now().strftime('%Y-%m-%d'))
df['Days_Since_Applied'] = (today - df['Application_Date']).dt.days

print("\n--- Clean Data Preview ---")
print(df)

# 4. The Export
filename = 'job_search_data.csv'
# index=False ensures we don't export the row numbers (0, 1, 2, 3...)
df.to_csv(filename, index=False)

print(f"\nSuccess! Clean dataset exported as '{filename}'. Ready for ingestion.")