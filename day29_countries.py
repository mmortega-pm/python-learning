import requests

print("--- The World Atlas ---")
country = input("Enter a country name: ")

# 1. The URL
url = f"https://restcountries.com/v3.1/name/{country}"

try:
    # 2. The Fetch
    response = requests.get(url)
    
    # 3. The Data (This API returns a LIST of countries, so we take the first one [0])
    data = response.json()[0]

    # 4. The Details
    name = data['name']['common']
    capital = data['capital'][0]  # Capital is also a list
    region = data['region']
    subregion = data['subregion']
    population = data['population']

    print(f"\n--- Data for {name} ---")
    print(f"Capital: {capital}")
    print(f"Region: {region} ({subregion})")
    print(f"Population: {population:,}") # The :, adds commas for readability

except:
    print("Country not found. Check your spelling!")