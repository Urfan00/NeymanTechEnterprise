from django.urls import path
from .views import WebsiteRequestListCreateAPIView, WebsiteRequestRetrieveUpdateDestroyAPIView



urlpatterns = [
    # URL pattern for list and create operations
    path('website_requests/', WebsiteRequestListCreateAPIView.as_view(), name='website_request_list_create'),

    # URL pattern for retrieve, update, and delete operations
    path('website_requests/<int:pk>/', WebsiteRequestRetrieveUpdateDestroyAPIView.as_view(), name='website_request_retrieve_update_destroy'),
]
