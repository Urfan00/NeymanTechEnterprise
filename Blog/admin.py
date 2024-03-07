import os
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Blog, BlogCategory


class BlogAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'slug', 'show_date', 'content', 'original_blog_image', 'compress_blog_image', 'blog_category', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'blog_category__blog_category_title']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            # Delete the images associated with each blog instance
            if obj.original_blog_image:
                storage, path = obj.original_blog_image.storage, obj.original_blog_image.path
                storage.delete(path)
                folder_path = os.path.dirname(path)
                os.rmdir(folder_path)  # Delete the folder

            if obj.compress_blog_image:
                storage, path = obj.compress_blog_image.storage, obj.compress_blog_image.path
                storage.delete(path)
                folder_path = os.path.dirname(path)
                os.rmdir(folder_path)  # Delete the folder

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog_category_title', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'blog_category_title']
    list_filter = ['is_active']
    search_fields = ['blog_category_title']

    def delete_queryset(self, request, queryset):
        for category in queryset:
            # Delete related blog images
            for blog in category.related_blog_category.all():
                if blog.original_blog_image:
                    storage, path = blog.original_blog_image.storage, blog.original_blog_image.path
                    storage.delete(path)
                    folder_path = os.path.dirname(path)
                    os.rmdir(folder_path)  # Delete the folder

                if blog.compress_blog_image:
                    storage, path = blog.compress_blog_image.storage, blog.compress_blog_image.path
                    storage.delete(path)
                    folder_path = os.path.dirname(path)
                    os.rmdir(folder_path)  # Delete the folder

        # Call the delete_queryset method of the parent class
        super().delete_queryset(request, queryset)



admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
