from django.urls import path
from .views import (
    ServiceListCreateAPIView,
    ServiceRetrieveUpdateDestroyAPIView,
    ServiceCardListCreateAPIView,
    ServiceCardRetrieveUpdateDestroyAPIView,
)



urlpatterns = [
    # Service URLs
    path('services/', ServiceListCreateAPIView.as_view(), name='service_list_create'),
    path('services/<slug:service_slug>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service_detail'),

    # Service Card URLs
    path('service_cards/', ServiceCardListCreateAPIView.as_view(), name='service_card_list_create'),
    path('service_cards/<int:pk>/', ServiceCardRetrieveUpdateDestroyAPIView.as_view(), name='service_card_detail'),
]
