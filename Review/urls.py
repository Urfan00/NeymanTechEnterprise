from django.urls import path
from .views import CostumerReviewListCreateAPIView, CostumerReviewRetrieveUpdateDestroyAPIView



urlpatterns = [
    # URL pattern for list and create operations
    path('costumer_reviews/', CostumerReviewListCreateAPIView.as_view(), name='costumer_review_list_create'),

    # URL pattern for retrieve, update, and delete operations
    path('costumer_reviews/<int:pk>/', CostumerReviewRetrieveUpdateDestroyAPIView.as_view(), name='costumer_review_retrieve_update_destroy'),
]
