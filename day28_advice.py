import requests

# 1. The Source
url = "https://api.adviceslip.com/advice"

print("--- Asking the Internet for Wisdom ---")

# 2. The Fetch
response = requests.get(url)
data = response.json()

# 3. The Fortune
slip = data['slip']
print(f"Advice: {slip['advice']}")