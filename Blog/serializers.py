from rest_framework import serializers
from .models import Blog, BlogCategory



class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'blog_category_title', 'is_active', 'created_at', 'updated_at']


class BlogCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'show_date','content','is_show', 'original_blog_image', 'compress_blog_image', 'blog_category', 'created_at', 'updated_at']


class BlogREADSerializer(serializers.ModelSerializer):
    blog_category = BlogCategorySerializer()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'show_date','content','is_show', 'original_blog_image', 'compress_blog_image', 'blog_category', 'created_at', 'updated_at']
