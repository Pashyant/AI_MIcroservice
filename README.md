# AI_Microservice

## AI-powered Recommendation Microservice

This microservice leverages AI to generate personalized product recommendations based on user interactions. It is built using FastAPI and follows a structured approach for handling requests and responses.

---

## How the Files Interact

### `main.py`
- Imports the `RecommendationModel` class from `models.py` to use the AI model.
- Imports the `UserRequest` and `RecommendationResponse` schemas from `schemas.py` for request/response validation.
- Defines FastAPI endpoints and uses the `RecommendationModel` to generate recommendations.

### `models.py`
- Contains the `RecommendationModel` class responsible for training the AI model and generating recommendations.
- This file is utilized by `main.py` when the `/recommend/` endpoint is hit.

### `schemas.py`
- Defines the data models (`UserRequest` and `RecommendationResponse`) used by `main.py` to validate incoming requests and format outgoing responses.

---

## Flow of Execution

When a POST request is made to the `/recommend/` endpoint:

1. FastAPI validates the incoming request data using the `UserRequest` schema from `schemas.py`.
2. The `recommend_products` function in `main.py` calls the `get_recommendations` method of the `RecommendationModel` class (from `models.py`).
3. The AI model processes the request and returns the recommended products.
4. The response is formatted using the `RecommendationResponse` schema and sent back to the client.

---

## Directory Structure

```
project/
│
├── main.py               # FastAPI app and endpoints
├── models.py             # AI model logic
├── schemas.py            # Pydantic schemas for data validation
└── requirements.txt      # Dependencies (e.g., fastapi, scikit-learn, numpy)
```

---

## Testing the `/recommend/` Endpoint

### Option 1: Using a Python Script
You can write a Python script to send a POST request to the `/recommend/` endpoint. Save the following code in a file called `test_client.py`:

```python
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
```

### Running the Script
Execute the script using the following command:

```bash
python test_client.py
```

### Sample Output
```
Status Code: 200
Response JSON: {'user_id': 3, 'recommended_products': [2, 0]}
```

---

## Dependencies
Ensure you have the required dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

---

## Running the Microservice
To start the FastAPI application, run:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## Future Enhancements
- Implement a more sophisticated recommendation algorithm.
- Add database support for storing user preferences.
- Integrate authentication for secure API access.

---

This AI-powered microservice is designed to be modular and scalable, enabling personalized recommendations with minimal setup.

