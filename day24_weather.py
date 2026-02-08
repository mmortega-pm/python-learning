import requests

print("--- Checking Weather for NYC ---")

# 1. The URL (The Question)
# We are asking for the weather at Lat 40.71, Long -74.01 (NYC)
url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"

# 2. The Request (Send the Runner)
response = requests.get(url)

# 3. The Data (Open the Package)
data = response.json()

# 4. Extract the Temperature
# The API gives us a dictionary called 'current_weather'
temp = data['current_weather']['temperature']
wind = data['current_weather']['windspeed']

print(f"Temperature: {temp}°C")
print(f"Wind Speed: {wind} km/h")