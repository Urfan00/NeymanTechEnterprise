from rest_framework import serializers
from .models import WebsiteRequest



class WebsiteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteRequest
        fields = ['id', 'fullname', 'phone_number', 'request', 'company', 'is_view', 'admin_comment', 'created_at', 'updated_at']
