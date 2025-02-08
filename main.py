from fastapi import FastAPI
from models import RecommendationModel
from schemas import UserRequest, RecommendationResponse

# Initialize FastAPI app
app = FastAPI()

# Initialize the recommendation model
recommendation_model = RecommendationModel()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Recommendation Service!"}

@app.post("/recommend/", response_model=RecommendationResponse)
def recommend_products(request: UserRequest):
    # Get recommendations using the RecommendationModel
    recommended_products = recommendation_model.get_recommendations(request.user_id, request.product_ids)
    return {"user_id": request.user_id, "recommended_products": recommended_products}