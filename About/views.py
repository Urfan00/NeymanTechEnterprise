from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactInfoCREATESerializer, ContactInfoREADSerializer, DifferentUsSerializer, EmailAddressSerializer, PhoneNumberSerializer
from .models import ContactInfo, DifferentUs, EmailAddress, PhoneNumber



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Different Us GET & POST
class DifferentUsListCreateAPIView(ListCreateAPIView):
    queryset = DifferentUs.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    serializer_class = DifferentUsSerializer


# Different Us GET & PUT & PATCH & DELETE
class DifferentUsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DifferentUs.objects.all()
    serializer_class = DifferentUsSerializer


# Phone Number GET & POST
class PhoneNumberListCreateAPIView(ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['phone']
    serializer_class = PhoneNumberSerializer


# Phone Number GET & PUT & PATCH & DELETE
class PhoneNumberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


# Email Address GET & POST
class EmailAddressListCreateAPIView(ListCreateAPIView):
    queryset = EmailAddress.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']
    serializer_class = EmailAddressSerializer


# Email Address GET & PUT & PATCH & DELETE
class EmailAddressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressSerializer


# Contact Info GET & POST
class ContactInfoListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_classes = {
        'GET' : ContactInfoREADSerializer,
        'POST' : ContactInfoCREATESerializer
    }


# Contact Info GET & PUT & PATCH & DELETE
class BlogRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_classes = {
        'GET' : ContactInfoREADSerializer,
        'PUT' : ContactInfoCREATESerializer,
        'PATCH' : ContactInfoCREATESerializer
    }
