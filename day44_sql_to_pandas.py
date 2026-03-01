import sqlite3
import pandas as pd

print("--- Day 44: Secure SQL to Pandas Pipeline ---")

# 1. Connect to a secure, local SQLite database (No passwords required!)
conn = sqlite3.connect('learning_metrics.db')
cur = conn.cursor()

# 2. Setup: Build a quick table and insert data so we have something to query
cur.execute('''
    CREATE TABLE IF NOT EXISTS certifications (
        cert_id INTEGER PRIMARY KEY,
        name TEXT,
        status TEXT,
        target_date TEXT
    )
''')
# Insert some dummy data
cur.execute("INSERT OR IGNORE INTO certifications VALUES (1, 'PMP', 'In Progress', '2026-06-01')")
cur.execute("INSERT OR IGNORE INTO certifications VALUES (2, 'SQL Bootcamp', 'Completed', '2026-02-27')")
cur.execute("INSERT OR IGNORE INTO certifications VALUES (3, 'Python 100 Days', 'In Progress', '2026-05-15')")
conn.commit()

# 3. The Core Lesson: Query the data
cur.execute('SELECT * FROM certifications')
raw_data = cur.fetchall()

# 4. The Magic Trick: Extract the column headers dynamically
# cur.description holds the metadata. We isolate just the names.
col_names = [desc[0] for desc in cur.description]

# 5. The Transformation: Load it all into Pandas
df = pd.DataFrame(raw_data, columns=col_names)

print("\n--- Clean Pandas DataFrame ---")
print(df.to_string(index=False))

# 6. Close the connections (TPM Best Practice)
cur.close()
conn.close()