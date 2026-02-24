import sqlite3
import pandas as pd

print("--- Building a Database with Python ---")

# 1. Create a local SQL database file (or connect if it exists)
conn = sqlite3.connect('tpm_metrics.db')
cursor = conn.cursor()

# 2. The SQL logic: CREATE TABLE
# We use triple quotes (''') in Python to write multi-line strings easily
cursor.execute('''
    CREATE TABLE IF NOT EXISTS project_tracking (
        task_id INTEGER PRIMARY KEY,
        initiative TEXT,
        tool TEXT,
        status TEXT
    )
''')

# 3. Insert some data into our new table
# We use INSERT OR IGNORE so it doesn't duplicate if you run the script twice
cursor.execute('''
    INSERT OR IGNORE INTO project_tracking (task_id, initiative, tool, status)
    VALUES (1, 'Job Search Tracking', 'Looker Studio', 'In Progress')
''')

# Save the changes
conn.commit()

# 4. The Magic: Read the SQL table directly into a Pandas DataFrame
query = "SELECT * FROM project_tracking"
df = pd.read_sql_query(query, conn)

print("\n--- Output from SQL Database ---")
print(df)

# 5. Close the database connection
conn.close()