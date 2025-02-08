import requests

# Define the API endpoint
url = "http://127.0.0.1:8000/recommend/"

# Sample request data
data = {
    "user_id": 3,
    "product_ids": [1, 3]
}

# Send a POST request
response = requests.post(url, json=data)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())