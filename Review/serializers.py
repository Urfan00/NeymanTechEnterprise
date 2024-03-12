from rest_framework import serializers
from .models import CostumerReview



class CostumerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostumerReview
        fields = ['id', 'fullname', 'costumer_company', 'costumer_review', 'is_show', 'created_at', 'updated_at']
