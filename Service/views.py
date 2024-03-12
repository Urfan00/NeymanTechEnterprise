import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ServiceCardCREATESerializer, ServiceCardREADSerializer, ServiceSerializer
from .models import Service, ServiceCard



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Service GET & POST
class ServiceListCreateAPIView(ListCreateAPIView):
    queryset = Service.objects.filter(service_is_show=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['service_is_show']
    search_fields = ['service_title']
    serializer_class = ServiceSerializer


# Service GET & PUT & PATCH & DELETE
class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.filter(service_is_show=True).all()
    lookup_field = "service_slug"
    serializer_class = ServiceSerializer


# Service Card GET & POST
class ServiceCardListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ServiceCard.objects.filter(service_card_is_show=True, service__service_is_show=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['service', 'service_card_is_show']
    search_fields = ['service_card_title']
    serializer_classes = {
        'GET' : ServiceCardREADSerializer,
        'POST' : ServiceCardCREATESerializer
    }


# Service Card GET & PUT & PATCH & DELETE
class ServiceCardRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = ServiceCard.objects.filter(service_card_is_show=True, service__service_is_show=True).all()
    serializer_classes = {
        'GET' : ServiceCardREADSerializer,
        'PUT' : ServiceCardCREATESerializer,
        'PATCH' : ServiceCardCREATESerializer
    }
