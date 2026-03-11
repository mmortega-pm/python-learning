import requests
import json

print("--- Day 55: API Updates and Deletions (PUT & DELETE) ---")

# 1. The Target Record
# We are specifically targeting record ID #1
url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

# -----------------------------------------
# Part 1: The PUT Request (Updating a record)
# -----------------------------------------
print("\n[ACTION 1] Executing PUT request to update record #1...")

# The modified payload. We are changing the title to mark it as resolved.
updated_ticket = {
    "id": 1,
    "title": "[RESOLVED] Server Connectivity Drop",
    "body": "Node 4 has been rebooted and is successfully responding.",
    "userId": 101
}

# requests.put() replaces the existing data with our new payload
put_response = requests.put(url, data=json.dumps(updated_ticket), headers=headers)

if put_response.status_code == 200:
    print(f"-> SUCCESS (HTTP 200). Record updated.")
    print(f"-> Server echoed back: {put_response.json()['title']}")
else:
    print(f"-> ERROR: Update failed with status {put_response.status_code}")

# -----------------------------------------
# Part 2: The DELETE Request (Removing a record)
# -----------------------------------------
print("\n[ACTION 2] Executing DELETE request to clear record #1...")

# requests.delete() doesn't need a payload. We just point it at the URL.
delete_response = requests.delete(url)

# A successful deletion usually returns a 200 (OK) or a 204 (No Content)
if delete_response.status_code in [200, 204]:
    print(f"-> SUCCESS (HTTP {delete_response.status_code}). Record deleted from system.")
else:
    print(f"-> ERROR: Deletion failed with status {delete_response.status_code}")