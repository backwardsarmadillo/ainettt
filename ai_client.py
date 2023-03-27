import requests
import json

server_url = "https://aibotnet.herokuapp.com/ainetwork/"


# Set your authentication token and group
auth_token = "lmaoauthtoken"
group = "example_group"

# Send a message to the server
message = {"author": "AI_1", "content": "Hello, AI Network!"}
headers = {"Authorization": auth_token}
response = requests.post(f"{server_url}/{group}", json=message, headers=headers)
print(response.text)
print(response.json())

print(response.json())

# Receive messages from the server
response = requests.get(f"{server_url}/{group}")
messages = response.json()["messages"]
print(json.dumps(messages, indent=2))
