from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id','original_url', 'short_code','created_at_time']
        read_only_fields = ['short_code','created_at_time']