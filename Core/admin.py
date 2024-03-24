import os
import shutil
from django.conf import settings
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FAQ, Partner, Subscribe
from modeltranslation.admin import TranslationAdmin



class FAQAdmin(ImportExportModelAdmin, TranslationAdmin):
    fieldsets = (
        ('EN', {'fields': ('faq_en', 'answer_en')}),  # English fields
        ('AZ', {'fields': ('faq_az', 'answer_az')}),  # Azerbaijani fields
        ('TR', {'fields': ('faq_tr', 'answer_tr')}),  # Turkish fields
        ('RU', {'fields': ('faq_ru', 'answer_ru')}),  # Russian fields
        ('Additional', {'fields': ('is_active', )}),  # Non-translated fields
    )
    list_display = ['id', 'faq', 'answer', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'faq']
    list_filter = ['is_active']
    search_fields = ['faq']


class SubscribeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'email', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'email']
    search_fields = ['email']
    list_filter = ['is_active']


class PartnerAdmin(ImportExportModelAdmin):
    list_display = ['id', 'partner_name', 'original_partner_logo', 'compress_partner_logo', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'partner_name']
    list_filter = ['is_active']
    search_fields = ['partner_name']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Get the paths to the original and compressed blog folders
            original_blog_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Partner', obj.partner_name)
            compress_blog_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Partner', obj.partner_name)

            # Delete the original blog folder and its contents
            if os.path.exists(original_blog_folder):
                shutil.rmtree(original_blog_folder)

            # Delete the compressed blog folder and its contents
            if os.path.exists(compress_blog_folder):
                shutil.rmtree(compress_blog_folder)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)




admin.site.register(FAQ, FAQAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Partner, PartnerAdmin)
