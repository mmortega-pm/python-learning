import requests
import pandas as pd

print("--- Day 51: Live API Extraction ---")

# 1. The Endpoint (A free public API that returns dummy user data)
url = "https://jsonplaceholder.typicode.com/users"

print(f"Pinging API Endpoint: {url}...")

# 2. The Request (Knocking on the door and asking for the JSON data)
response = requests.get(url)
data = response.json()

# 3. The Transformation
# Load the raw JSON into Pandas
df = pd.DataFrame(data)

# Filter for only the columns a TPM cares about
clean_df = df[['id', 'name', 'email', 'company']].copy()

# JSON data is often nested. The 'company' column currently holds a dictionary.
# We use a lambda function to extract just the company name string.
clean_df['company_name'] = clean_df['company'].apply(lambda x: x['name'])
clean_df = clean_df.drop(columns=['company'])

print("\n--- Live API Data Extracted & Transformed ---")
print(clean_df.head().to_string(index=False))