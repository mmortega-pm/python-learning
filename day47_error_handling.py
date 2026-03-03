import sqlite3
import pandas as pd
import sys

print("--- Day 47: Pipeline Error Handling ---")

try:
    print("Attempting to connect to the database...")
    conn = sqlite3.connect('dashboard_backend.db')
    
    print("Executing extraction query...")
    # Triggering the failure intentionally
    query = "SELECT * FROM a_table_that_does_not_exist"
    df = pd.read_sql_query(query, conn)
    
    print("Data extracted successfully.")

# 2. The Catch (Updated to look for Pandas Database Errors)
except pd.errors.DatabaseError as e:
    print(f"\n[PIPELINE ALERT] Pandas Database Operation Failed.")
    print(f"Error Details: {e}")
    print("TPM Action: Verify table names and SQL syntax.")
    # We don't need sys.exit() here if it's the end of the script, but it's good practice
    # if you have more code below this block that relies on this data.

except Exception as e:
    print(f"\n[CRITICAL ERROR] Unknown failure: {e}")

finally:
    print("\nExecuting final cleanup...")
    if 'conn' in locals():
        conn.close()
        print("Database connection safely closed.")