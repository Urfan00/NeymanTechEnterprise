from rest_framework import serializers
from .models import ContactInfo, DifferentUs, EmailAddress, PhoneNumber



class DifferentUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentUs
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'phone', 'created_at', 'updated_at']


class EmailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = ['id', 'email', 'created_at', 'updated_at']


class ContactInfoCREATESerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'phone', 'email', 'location_name', 'location_url', 'facebook', 'twitter', 'instagram', 'linkedln', 'youtube', 'github', 'tiktok', 'whatsapp', 'created_at', 'updated_at']


class ContactInfoREADSerializer(serializers.ModelSerializer):
    phone = PhoneNumberSerializer(many=True)
    email = EmailAddressSerializer(many=True)

    class Meta:
        model = ContactInfo
        fields = ['id', 'phone', 'email', 'location_name', 'location_url', 'facebook', 'twitter', 'instagram', 'linkedln', 'youtube', 'github', 'tiktok', 'whatsapp', 'created_at', 'updated_at']
