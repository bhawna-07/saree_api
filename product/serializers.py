# products/serializers.py
from rest_framework import serializers
from .models import Sarees

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')  # frontend-friendly
    image = serializers.ImageField()  # will return media URL

    class Meta:
        model = Sarees
        fields = ['id', 'title', 'category', 'description','price',  'image']
