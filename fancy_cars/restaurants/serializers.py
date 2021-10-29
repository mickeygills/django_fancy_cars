from rest_framework import serializers
from .models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'tag',
            'rating'
        ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'tag',
            'rating',
            'phone',
            'address',
            'city',
            'state',
            'zip_code',
            'photo',
            'price',
        ]