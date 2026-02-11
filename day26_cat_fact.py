import requests

# 1. The Source
url = "https://catfact.ninja/fact"

print("--- Calling the Cat Hotline ---")

# 2. The Fetch
response = requests.get(url)
data = response.json()

# 3. The Fact
print(f"Fact: {data['fact']}")