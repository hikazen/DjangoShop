from rest_framework import serializers

from .models import Product, Category, Tag, Review


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), read_only=True)

    class Meta:
        fields = '__all__'
        model = Product


class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)
    products = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        fields = ('id', 'name', 'description', 'products')
        model = Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product', 'text', 'rating')
