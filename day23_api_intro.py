import requests

# Option B: CoinGecko (Another major crypto source)
# This URL asks for the price of 'bitcoin' in 'usd'
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

print("--- Connecting to CoinGecko API ---")
response = requests.get(url)

# The data structure is slightly different: {'bitcoin': {'usd': 96123}}
data = response.json()
price = data['bitcoin']['usd']

print(f"Bitcoin Price: ${price}")