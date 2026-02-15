import requests

# The "Bored" API (hosted by Le Wagon)
url = "https://bored.api.lewagon.com/api/activity/"

print("--- What should I do today? ---")

# 1. Fetch the idea
response = requests.get(url)
data = response.json()

# 2. Extract the details
activity = data['activity']
kind = data['type']
participants = data['participants']

# 3. The Suggestion
print(f"Suggestion: {activity}")
print(f"Type: {kind}")
print(f"People needed: {participants}")