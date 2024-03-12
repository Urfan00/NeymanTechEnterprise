import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BlogCREATESerializer, BlogCategorySerializer, BlogREADSerializer
from .models import Blog, BlogCategory
from django.utils import timezone


current_date = timezone.now().date()

class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Blog Category GET & POST
class BlogCategoryListCreateAPIView(ListCreateAPIView):
    queryset = BlogCategory.objects.filter(is_active=True).all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['blog_category_title']
    serializer_class = BlogCategorySerializer


# Blog Category GET & PUT & PATCH & DELETE
class BlogCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.filter(is_active=True).all()
    serializer_class = BlogCategorySerializer


# Blog GET & POST
class BlogListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Blog.objects.filter(show_date__gte=current_date, is_show=True, blog_category__is_active=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['blog_category', 'is_show']
    search_fields = ['title']
    serializer_classes = {
        'GET' : BlogREADSerializer,
        'POST' : BlogCREATESerializer
    }


# Blog GET & PUT & PATCH & DELETE
class BlogRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(show_date__gte=current_date, is_show=True, blog_category__is_active=True).all()
    lookup_field = "slug"
    serializer_classes = {
        'GET' : BlogREADSerializer,
        'PUT' : BlogCREATESerializer,
        'PATCH' : BlogCREATESerializer
    }
