import os
import shutil
from django.conf import settings
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CostumerReview



class CostumerReviewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'fullname', 'costumer_company', 'costumer_review', 'original_costumer_image', 'compress_costumer_image', 'is_show', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    list_filter = ['is_show']
    search_fields = ['fullname', 'costumer_company']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Get the paths to the original and compressed service folders
            original_costumer_image_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Costumer-Image', obj.fullname)
            compress_costumer_image_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Costumer-Image', obj.fullname)

            # Delete the original service folder and its contents
            if os.path.exists(original_costumer_image_folder):
                shutil.rmtree(original_costumer_image_folder)

            # Delete the compressed service folder and its contents
            if os.path.exists(compress_costumer_image_folder):
                shutil.rmtree(compress_costumer_image_folder)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)

admin.site.register(CostumerReview, CostumerReviewAdmin)
