import requests

# The API Endpoint
url = "http://api.open-notify.org/astros.json"

print("--- Connecting to ISS ---")
response = requests.get(url)
data = response.json()

# How many people are up there?
count = data['number']
print(f"There are currently {count} humans in space.")

# Who are they?
for person in data['people']:
    print(f"- {person['name']} on {person['craft']}")