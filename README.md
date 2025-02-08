# AI_Microservice
AI-powered Recommendation Microservice

How the Files Interact
main.py:

Imports the RecommendationModel class from models.py to use the AI model.

Imports the UserRequest and RecommendationResponse schemas from schemas.py for request/response validation.

Defines the FastAPI endpoints and uses the RecommendationModel to generate recommendations.

models.py:

Contains the RecommendationModel class, which is responsible for training the AI model and generating recommendations.

This file is called by main.py when the /recommend/ endpoint is hit.

schemas.py:

Defines the data models (UserRequest and RecommendationResponse) used by main.py to validate incoming requests and format outgoing responses.

Flow of Execution
When a POST request is made to the /recommend/ endpoint:

FastAPI validates the incoming request data using the UserRequest schema from schemas.py.

The recommend_products function in main.py calls the get_recommendations method of the RecommendationModel class (from models.py).

The AI model processes the request and returns the recommended products.

The response is formatted using the RecommendationResponse schema and sent back to the client.

Directory Structure
Copy
project/
│
├── main.py               # FastAPI app and endpoints
├── models.py             # AI model logic
├── schemas.py            # Pydantic schemas for data validation
└── requirements.txt      # Dependencies (e.g., fastapi, scikit-learn, numpy)



Test the /recommend/ Endpoint
Option 1: Using Python Script
You can write a Python script to send a POST request to the /recommend/ endpoint. Save the following code in a file called test_client.py:

python
Copy
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
Run the script:

bash
Copy
python test_client.py
Output:
Copy
Status Code: 200
Response JSON: {'user_id': 3, 'recommended_products': [2, 0]}

