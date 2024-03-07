import os
import shutil
from django.conf import settings
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Project, ProjectAllImage



class ProjectAdmin(ImportExportModelAdmin):
    list_display = ['id', 'project_title', 'project_slug', 'project_original_image', 'project_compress_image', 'project_link', 'project_is_show', 'service', 'created_at', 'updated_at']
    list_display_links = ['id', 'project_title']
    list_filter = ['project_is_show']
    search_fields = ['project_title', 'service__service_title']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Get the paths to the original and compressed service folders
            original_project_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Service', obj.service.service_title, 'Project-Image', obj.project_title)
            compress_project_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Service', obj.service.service_title, 'Project-Image', obj.project_title)
            
            # Delete the original service folder and its contents
            if os.path.exists(original_project_folder):
                shutil.rmtree(original_project_folder)

            # Delete the compressed service folder and its contents
            if os.path.exists(compress_project_folder):
                shutil.rmtree(compress_project_folder)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)


class ProjectAllImageAdmin(ImportExportModelAdmin):
    list_display = ['id', 'original_image', 'compress_image', 'image_is_show', 'project', 'created_at', 'updated_at']
    list_filter = ['image_is_show']
    search_fields = ['project__project_title']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.original_image:
                storage, path = obj.original_image.storage, obj.original_image.path
                storage.delete(path)

            if obj.compress_image:
                storage, path = obj.compress_image.storage, obj.compress_image.path
                storage.delete(path)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)



admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectAllImage, ProjectAllImageAdmin)
