import requests

print("--- The AI Age Guesser ---")

# 1. The Input (Dynamic)Zor
# We ask the user for a name, instead of hardcoding it
name = input("Enter a name: ")

# 2. The URL Construction
# We inject the variable 'name' directly into the API address
url = f"https://api.agify.io?name={name}"

print(f"Checking the database for '{name}'...")

# 3. The Fetch
response = requests.get(url)
data = response.json()

# 4. The Prediction
predicted_age = data['age']
count = data['count']  # How many people provided data for this

print(f"Based on {count} records...")
print(f"I predict '{name}' is {predicted_age} years old.")