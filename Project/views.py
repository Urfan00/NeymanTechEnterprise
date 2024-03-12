import django_filters.rest_framework
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProjectAllImageSerializer, ProjectCREATESerializer, ProjectREADSerializer
from .models import Project, ProjectAllImage



class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


# Project All Image GET & POST
class ProjectAllImageListCreateAPIView(ListCreateAPIView):
    queryset = ProjectAllImage.objects.filter(image_is_show=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['project', 'image_is_show']
    search_fields = ['project']
    serializer_class = ProjectAllImageSerializer


# Project All Image GET & PUT & PATCH & DELETE
class ProjectAllImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProjectAllImage.objects.filter(image_is_show=True).all()
    lookup_field = "service_slug"
    serializer_class = ProjectAllImageSerializer


# Project GET & POST
class ProjectListCreateAPIView(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Project.objects.filter(service__service_is_show=True, project_is_show=True).all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['service', 'project_is_show']
    search_fields = ['project_title']
    serializer_classes = {
        'GET' : ProjectREADSerializer,
        'POST' : ProjectCREATESerializer
    }


# Project GET & PUT & PATCH & DELETE
class ProjectRetrieveUpdateDestroyAPIView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.filter(service__service_is_show=True, project_is_show=True).all()
    serializer_classes = {
        'GET' : ProjectREADSerializer,
        'PUT' : ProjectCREATESerializer,
        'PATCH' : ProjectCREATESerializer
    }
