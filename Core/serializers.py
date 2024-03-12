from rest_framework import serializers
from .models import FAQ, Partner, Subscribe



class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'faq', 'answer', 'is_active', 'created_at', 'updated_at']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email', 'is_active', 'created_at', 'updated_at']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'partner_name', 'original_partner_logo', 'compress_partner_logo', 'is_active', 'created_at', 'updated_at']
