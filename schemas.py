from pydantic import BaseModel

class UserRequest(BaseModel):
    user_id: int
    product_ids: list[int]

class RecommendationResponse(BaseModel):
    user_id: int
    recommended_products: list[int]