from django.urls import path
from .views import (
    FAQListCreateAPIView,
    FAQRetrieveUpdateDestroyAPIView,
    SubscribeListCreateAPIView,
    SubscribeRetrieveUpdateDestroyAPIView,
    PartnerListCreateAPIView,
    PartnerRetrieveUpdateDestroyAPIView,
)



urlpatterns = [
    # FAQ URLs
    path('faq/', FAQListCreateAPIView.as_view(), name='faq_list_create'),
    path('faq/<int:pk>/', FAQRetrieveUpdateDestroyAPIView.as_view(), name='faq_detail'),

    # Subscribe URLs
    path('subscribe/', SubscribeListCreateAPIView.as_view(), name='subscribe_list_create'),
    path('subscribe/<int:pk>/', SubscribeRetrieveUpdateDestroyAPIView.as_view(), name='subscribe_detail'),

    # Partner URLs
    path('partner/', PartnerListCreateAPIView.as_view(), name='partner_list_create'),
    path('partner/<int:pk>/', PartnerRetrieveUpdateDestroyAPIView.as_view(), name='partner_detail'),
]
