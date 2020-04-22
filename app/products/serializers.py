from rest_framework import serializers
from django.conf import settings
from users.serializers import UserSerializer
from core.models import User, Tag, Category, Product

class TagSerializer(serializers.ModelSerializer):
    # Serializer for tag objects
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class CategorySerializer(serializers.ModelSerializer):
    # Serializer for ingredient objects
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)

class ProductSerializer(serializers.ModelSerializer):
    # Serialize a recipe

    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all()
    # )
    tags = TagSerializer(many=True, read_only=True)

    # Get name of the categories for customers
    category = CategorySerializer(read_only=True)

    # Get name of the user for customers
    user = UserSerializer(read_only=True)
   
    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'tags', 'stock',
                  'price', 'link', 'user', 'image'
                  )
        read_only_Fields = ('id',)

class ProductDetailSerializer(ProductSerializer):
    # Serializer a recipe detail
    tags = TagSerializer(many=True, read_only=True)


class ProductImageSerializer(serializers.ModelSerializer):
    # Serializer for uploading images for recipes

    class Meta:
        model = Product
        fields = ('id', 'image')
        read_only_Fields = ('id',)

