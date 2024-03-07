from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import WebsiteRequest



class WebsiteRequestAdmin(ImportExportModelAdmin):
    list_display = ['id', 'fullname', 'phone_number', 'request', 'company', 'is_view', 'admin_comment', 'created_at', 'updated_at']
    list_display_links = ['id', 'fullname']
    list_filter = ['is_view']
    search_fields = ['fullname', 'company']


admin.site.register(WebsiteRequest, WebsiteRequestAdmin)
