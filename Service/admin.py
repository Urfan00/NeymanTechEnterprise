import os
import shutil
from django.conf import settings
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Service, ServiceCard



class ServiceAdmin(ImportExportModelAdmin):
    list_display = ['id', 'service_title', 'service_slug', 'service_original_icon', 'service_compress_icon', 'description', 'service_is_show', 'created_at', 'updated_at']
    list_display_links = ['id', 'service_title']
    list_filter = ['service_is_show']
    search_fields = ['service_title']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Get the paths to the original and compressed service folders
            original_service_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Service', obj.service_title)
            compress_service_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Service', obj.service_title)
            
            # Delete the original service folder and its contents
            if os.path.exists(original_service_folder):
                shutil.rmtree(original_service_folder)

            # Delete the compressed service folder and its contents
            if os.path.exists(compress_service_folder):
                shutil.rmtree(compress_service_folder)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)


class ServiceCardAdmin(ImportExportModelAdmin):
    list_display = ['id', 'service_card_title', 'service_card_content', 'service_card_is_show', 'service', 'created_at', 'updated_at']
    list_display_links = ['id', 'service_card_title']
    list_filter = ['service_card_is_show']
    search_fields = ['service_card_title']



admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCard, ServiceCardAdmin)
