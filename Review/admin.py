from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CostumerReview



class CostumerReviewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'fullname', 'costumer_company', 'costumer_review', 'is_show', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    list_filter = ['is_show']
    search_fields = ['fullname', 'costumer_company']


admin.site.register(CostumerReview, CostumerReviewAdmin)
