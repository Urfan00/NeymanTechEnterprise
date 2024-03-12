import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import WebsiteRequestSerializer
from .models import WebsiteRequest



# Costumer Review GET & POST
class WebsiteRequestListCreateAPIView(ListCreateAPIView):
    queryset = WebsiteRequest.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_view']
    search_fields = ['fullname', 'company']
    serializer_class = WebsiteRequestSerializer


# Costumer Review GET & PUT & PATCH & DELETE
class WebsiteRequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = WebsiteRequest.objects.all()
    serializer_class = WebsiteRequestSerializer
