from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ContactInfo, DifferentUs, EmailAddress, PhoneNumber
from modeltranslation.admin import TranslationAdmin



class ContactInfoAdmin(ImportExportModelAdmin):
    list_display = ['id', 'location_name', 'location_url', 'facebook', 'twitter', 'instagram', 'linkedln', 'youtube', 'github', 'tiktok', 'whatsapp', 'created_at', 'updated_at']


class DifferentUsAdmin(ImportExportModelAdmin, TranslationAdmin):
    fieldsets = (
        ('EN', {'fields': ('title_en', 'content_en')}),  # English fields
        ('AZ', {'fields': ('title_az', 'content_az')}),  # Azerbaijani fields
        ('TR', {'fields': ('title_tr', 'content_tr')}),  # Turkish fields
        ('RU', {'fields': ('title_ru', 'content_ru')}),  # Russian fields
    )
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']


class EmailAddressAdmin(ImportExportModelAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']
    list_display_links = ['id', 'email']
    search_fields = ['email']


class PhoneNumberAdmin(ImportExportModelAdmin):
    list_display = ['id', 'phone', 'created_at', 'updated_at']
    list_display_links = ['id', 'phone']
    search_fields = ['phone']



admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(DifferentUs, DifferentUsAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
