import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import FAQSerializer, PartnerSerializer, SubscribeSerializer
from .models import FAQ, Partner, Subscribe



# FAQ GET & POST
class FAQListCreateAPIView(ListCreateAPIView):
    queryset = FAQ.objects.filter(is_active=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['faq']
    serializer_class = FAQSerializer


# FAQ GET & PUT & PATCH & DELETE
class FAQRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.filter(is_active=True).all()
    serializer_class = FAQSerializer


# Subscribe GET & POST
class SubscribeListCreateAPIView(ListCreateAPIView):
    queryset = Subscribe.objects.filter(is_active=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['phone']
    serializer_class = SubscribeSerializer


# Subscribe GET & PUT & PATCH & DELETE
class SubscribeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subscribe.objects.filter(is_active=True).all()
    serializer_class = SubscribeSerializer


# Partner GET & POST
class PartnerListCreateAPIView(ListCreateAPIView):
    queryset = Partner.objects.filter(is_active=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['email']
    serializer_class = PartnerSerializer


# Partner GET & PUT & PATCH & DELETE
class PartnerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.filter(is_active=True).all()
    serializer_class = PartnerSerializer
