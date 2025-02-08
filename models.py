import numpy as np
from sklearn.neighbors import NearestNeighbors

class RecommendationModel:
    def __init__(self):
        # Dummy user-product interaction data
        self.user_product_matrix = np.array([
            [1, 0, 1, 0, 1],  # User 1
            [0, 1, 0, 1, 0],  # User 2
            [1, 1, 0, 0, 1],  # User 3
        ])
        self.model = NearestNeighbors(n_neighbors=2, metric="cosine")
        self.model.fit(self.user_product_matrix)

    def get_recommendations(self, user_id: int, product_ids: list[int]):
        # Get recommendations for the user
        distances, indices = self.model.kneighbors([self.user_product_matrix[user_id - 1]])
        recommended_products = [int(i) for i in indices.flatten() if i not in product_ids]
        return recommended_products