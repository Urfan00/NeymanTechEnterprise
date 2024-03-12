from rest_framework import serializers
from Service.serializers import ServiceSerializer
from .models import Project, ProjectAllImage



class ProjectAllImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAllImage
        fields = ['id', 'original_image', 'compress_image', 'image_is_show', 'project', 'created_at', 'updated_at']


class ProjectCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_slug', 'project_original_image', 'project_compress_image', 'project_link', 'project_is_show', 'service', 'created_at', 'updated_at']


class ProjectREADSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    all_images = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_slug', 'project_original_image', 'project_compress_image', 'project_link', 'project_is_show', 'all_images', 'service', 'created_at', 'updated_at']

    def get_all_images(self, obj):
        request = self.context.get('request')
        if request is not None:
            root_path = request.build_absolute_uri('/')[:-1]  # Get the root path dynamically
            image_data = ProjectAllImageSerializer(ProjectAllImage.objects.filter(project_id=obj), many=True).data
            for image in image_data:
                image['original_image'] = root_path + image['original_image']
                image['compress_image'] = root_path + image['compress_image']
            return image_data
        return None
