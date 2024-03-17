from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    ProjectAllImageListCreateAPIView,
    ProjectAllImageRetrieveUpdateDestroyAPIView,
)



urlpatterns = [
    # Project URLs
    path('projects/', ProjectListCreateAPIView.as_view(), name='project_list_create'),
    path('projects/<slug:project_slug>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project_detail'),

    # Project All Image URLs
    path('project_all_images/', ProjectAllImageListCreateAPIView.as_view(), name='project_all_image_list_create'),
    path('project_all_images/<int:pk>/', ProjectAllImageRetrieveUpdateDestroyAPIView.as_view(), name='project_all_image_detail'),
]
