from django.urls import path
from .views import (
    DifferentUsListCreateAPIView,
    DifferentUsRetrieveUpdateDestroyAPIView,
    PhoneNumberListCreateAPIView,
    PhoneNumberRetrieveUpdateDestroyAPIView,
    EmailAddressListCreateAPIView,
    EmailAddressRetrieveUpdateDestroyAPIView,
    ContactInfoListCreateAPIView,
    BlogRetrieveUpdateDestroyAPIView,
)



urlpatterns = [
    # Different Us URLs
    path('different_us/', DifferentUsListCreateAPIView.as_view(), name='different_us_list_create'),
    path('different_us/<int:pk>/', DifferentUsRetrieveUpdateDestroyAPIView.as_view(), name='different_us_detail'),

    # Phone Number URLs
    path('phone_number/', PhoneNumberListCreateAPIView.as_view(), name='phone_number_list_create'),
    path('phone_number/<int:pk>/', PhoneNumberRetrieveUpdateDestroyAPIView.as_view(), name='phone_number_detail'),

    # Email Address URLs
    path('email_address/', EmailAddressListCreateAPIView.as_view(), name='email_address_list_create'),
    path('email_address/<int:pk>/', EmailAddressRetrieveUpdateDestroyAPIView.as_view(), name='email_address_detail'),

    # Contact Info URLs
    path('contact_info/', ContactInfoListCreateAPIView.as_view(), name='contact_info_list_create'),
    path('contact_info/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='contact_info_detail'),
]
