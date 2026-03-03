import sqlite3
import pandas as pd

print("--- Day 46: Loading Data to SQL ---")

# 1. The Clean Data (Your perfectly formatted dashboard data)
clean_data = {
    'Company': ['Amazon', 'Google', 'Microsoft', 'Meta'],
    'Role': ['TPM', 'Product Manager', 'Senior TPM', 'Program Manager'],
    'Status': ['Interview', 'Applied', 'Rejected', 'Applied'],
    'Days_Active': [14, 2, 21, 5]
}

df = pd.DataFrame(clean_data)
print("1. Pandas DataFrame Ready:")
print(df.to_string(index=False))

# 2. Connect to our local SQLite database from Saturday
# (It will create the file if it doesn't exist yet)
conn = sqlite3.connect('dashboard_backend.db')

# 3. The Magic Load Command
# We are pushing the entire DataFrame into a new SQL table called 'job_pipeline'
table_name = 'job_pipeline'
df.to_sql(table_name, conn, if_exists='replace', index=False)

print(f"\n2. Success! Data successfully loaded into SQL table: '{table_name}'")

# 4. The Verification (Let's prove it worked using standard SQL)
print("\n3. Verifying the SQL Table:")
query = f"SELECT * FROM {table_name} WHERE Status = 'Applied'"
verification_df = pd.read_sql_query(query, conn)
print(verification_df.to_string(index=False))

# 5. Close the door
conn.close()