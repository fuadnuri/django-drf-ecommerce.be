from rest_framework import serializers
from .models import (Brand, Category, Product)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
