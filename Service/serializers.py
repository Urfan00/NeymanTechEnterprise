from rest_framework import serializers
from .models import Service, ServiceCard



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_title', 'service_slug', 'service_original_icon', 'service_compress_icon', 'description', 'service_is_show', 'created_at', 'updated_at']


class ServiceCardCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCard
        fields = ['id', 'service_card_title', 'service_card_content', 'service_card_is_show', 'service', 'created_at', 'updated_at']


class ServiceCardREADSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = ServiceCard
        fields = ['id', 'service_card_title', 'service_card_content', 'service_card_is_show', 'service', 'created_at', 'updated_at']
