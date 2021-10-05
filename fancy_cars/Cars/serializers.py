from rest_framework import serializers
from .models import Cars

class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            'make',
            'model',
            'nation_of_orign',
            'image',
        ]

class CarsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            'id',
            'make',
            'model',
            'price',
            'color',
            'year',
            'nation_of_orign',
            'horsepower',
            'image',
            'description'
        ]