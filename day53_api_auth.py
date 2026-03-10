import requests

print("--- Day 53: API Authentication ---")

# 1. The Secure Endpoint
# This specific URL expects a "Bearer" token to grant access.
url = "https://httpbin.org/bearer"

# 2. The Key (Security Best Practice)
# NEVER hardcode real API keys in production scripts pushed to GitHub!
# We are using a fake token here for practice.
my_api_key = "tpm_super_secret_token_123"

# 3. The Headers (Your Digital ID Card)
# This dictionary gets packaged with your request. 
headers = {
    "Authorization": f"Bearer {my_api_key}",
    "Content-Type": "application/json"
}

print("Knocking on secure API door with authorization token...")

# 4. The Request
# Notice how we pass the headers dictionary into the requests.get() function
response = requests.get(url, headers=headers)

# 5. The Verification
# HTTP Status 200 means "OK" / Success. 401 or 403 means "Unauthorized".
if response.status_code == 200:
    print(f"\n[SUCCESS] HTTP {response.status_code}: Access Granted.")
    data = response.json()
    
    # The server confirms it read our token correctly
    print(f"Server acknowledged token: {data['token']}")
    print(f"Server confirms user is authenticated: {data['authenticated']}")
else:
    print(f"\n[DENIED] Access Failed. HTTP Status: {response.status_code}")