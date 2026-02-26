import pandas as pd

print("--- Executing Data Aggregation ---")

# 1. The Raw Data (Your Pipeline)
data = {
    'Company': ['Amazon', 'Microsoft', 'Google', 'Spotify', 'Meta', 'Apple', 'Netflix', 'Airbnb'],
    'Role': ['TPM', 'Senior TPM', 'Product Manager', 'TPM', 'Program Manager', 'TPM', 'PM', 'TPM'],
    'Status': ['Interview', 'Rejected', 'Applied', 'Applied', 'Interview', 'Rejected', 'Applied', 'Offer']
}

# Load into Pandas
df = pd.DataFrame(data)

# 2. The Aggregation (The Python Pivot Table)
# We group by 'Status', count the occurrences, and reset the index to keep it as a clean table.
pipeline_summary = df.groupby('Status')['Company'].count().reset_index()

# 3. Clean up the column names for the final report
pipeline_summary.rename(columns={'Company': 'Total_Applications'}, inplace=True)

# Sort it so the biggest numbers are at the top
pipeline_summary = pipeline_summary.sort_values(by='Total_Applications', ascending=False)

print("\n--- Executive Pipeline Summary ---")
print(pipeline_summary.to_string(index=False)) # index=False hides the row numbers for a cleaner look