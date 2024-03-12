import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CostumerReviewSerializer
from .models import CostumerReview



# Costumer Review GET & POST
class CostumerReviewListCreateAPIView(ListCreateAPIView):
    queryset = CostumerReview.objects.filter(is_show=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_show']
    search_fields = ['fullname']
    serializer_class = CostumerReviewSerializer


# Costumer Review GET & PUT & PATCH & DELETE
class CostumerReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CostumerReview.objects.filter(is_show=True).all()
    serializer_class = CostumerReviewSerializer
