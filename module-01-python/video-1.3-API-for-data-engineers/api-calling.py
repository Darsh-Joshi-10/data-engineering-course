import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users", 
    timeout = 10
)
response.raise_for_status()
users = response.json()
print(f"Got {len(users)} users")