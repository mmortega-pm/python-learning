import requests
import json

print("--- Day 54: API POST Requests (Sending Data) ---")

# 1. The Target Endpoint
# This test API simulates creating a new database record
url = "https://jsonplaceholder.typicode.com/posts"

# 2. The Payload (The data you want to send)
# Think of this as filling out the fields of a new ticket automatically
new_ticket = {
    "title": "[AUTO-ALERT] Server Connectivity Drop",
    "body": "Node 4 in the primary cluster is unresponsive. Diagnostic required.",
    "userId": 101
}

# 3. The Headers
# We must explicitly tell the server that the package we are handing it is formatted as JSON
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

print("Executing POST request. Sending payload to server...")

# 4. The Action
# We convert our Python dictionary into a JSON string using json.dumps()
response = requests.post(url, data=json.dumps(new_ticket), headers=headers)

# 5. The Verification
# HTTP 201 means "Created"
if response.status_code == 201:
    print(f"\n[SUCCESS] HTTP {response.status_code}: Record Created.")
    print("The server processed the payload and returned the new record:")
    
    # The API will echo back our data along with a brand new simulated 'id'
    print(response.json())
else:
    print(f"\n[ERROR] Request failed with status code: {response.status_code}")