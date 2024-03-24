import os
import shutil
from django.conf import settings
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Blog, BlogCategory
from modeltranslation.admin import TranslationAdmin



class BlogAdmin(ImportExportModelAdmin, TranslationAdmin):
    fieldsets = (
        ('EN', {'fields': ('title_en', 'slug_en', 'content_en')}),  # English fields
        ('AZ', {'fields': ('title_az', 'slug_az', 'content_az')}),  # Azerbaijani fields
        ('TR', {'fields': ('title_tr', 'slug_tr', 'content_tr')}),  # Turkish fields
        ('RU', {'fields': ('title_ru', 'slug_ru', 'content_ru')}),  # Russian fields
        ('Additional', {'fields': ('show_date', 'is_show', 'blog_category', 'original_blog_image', 'compress_blog_image')}),  # Non-translated fields
    )
    list_display = ['id', 'title', 'slug', 'show_date', 'content', 'is_show', 'original_blog_image', 'compress_blog_image', 'blog_category', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_filter = ['is_show']
    search_fields = ['title', 'blog_category__blog_category_title']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Get the paths to the original and compressed blog folders
            original_blog_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Blog', obj.blog_category.blog_category_title, obj.title)
            compress_blog_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Blog', obj.blog_category.blog_category_title, obj.title)

            # Delete the original blog folder and its contents
            if os.path.exists(original_blog_folder):
                shutil.rmtree(original_blog_folder)

            # Delete the compressed blog folder and its contents
            if os.path.exists(compress_blog_folder):
                shutil.rmtree(compress_blog_folder)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)


class BlogCategoryAdmin(ImportExportModelAdmin, TranslationAdmin):
    list_display = ['id', 'blog_category_title', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'blog_category_title']
    list_filter = ['is_active']
    search_fields = ['blog_category_title']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Get the paths to the original and compressed blog folders
            original_blog_category_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Blog', obj.blog_category_title)
            compress_blog_category_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Blog', obj.blog_category_title)

            # Delete the original blog folder and its contents
            if os.path.exists(original_blog_category_folder):
                shutil.rmtree(original_blog_category_folder)

            # Delete the compressed blog folder and its contents
            if os.path.exists(compress_blog_category_folder):
                shutil.rmtree(compress_blog_category_folder)

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)



admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
