import requests
import pandas as pd
import time

print("--- Day 52: API Pagination ---")

base_url = "https://jsonplaceholder.typicode.com/posts"
all_data = []

# 1. The Loop: Fetching 3 pages of data (10 items per page)
for page in range(1, 4):
    print(f"Fetching Page {page}...")
    
    # Dynamically inject the page number into the URL
    response = requests.get(f"{base_url}?_page={page}&_limit=10")
    data = response.json()
    
    # Safety check: If the page is empty, break the loop
    if not data:
        break
        
    # Add this page's data to our master list
    all_data.extend(data)
    
    # Polite fetching: Don't hammer the API server
    time.sleep(0.5) 

# 2. The Transformation: Load all pages into one master DataFrame
df = pd.DataFrame(all_data)
clean_df = df[['id', 'userId', 'title']]

print(f"\n--- Success! Extracted {len(clean_df)} total records across 3 pages ---")
print(clean_df.head(3).to_string(index=False))
print("...")
print(clean_df.tail(3).to_string(index=False))