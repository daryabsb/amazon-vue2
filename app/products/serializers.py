from rest_framework import serializers
from django.conf import settings
from users.serializers import UserSerializer
from core.models import User, Tag, Category, Product, Review

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

class ReviewSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
       

    class Meta:
        model = Review
        exclude = ["product","updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

class MyProductSerializer(serializers.ModelSerializer):
    # Serialize a recipe
    
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    reviews_count = serializers.SerializerMethodField()

    # reviews = ReviewSerializer(many=True)

    slug = serializers.SlugField(read_only=True)

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'tags', 'stock',
                  'price', 'slug', 'user', 'image', 'reviews_count'
                  )
        read_only_Fields = ('id',)

    def get_reviews_count(self, instance):
        return instance.reviews.count()

# class ProductDetailSerializer(ProductSerializer):
#     # Serializer a recipe detail
#     tags = TagSerializer(many=True, read_only=True)
#     reviews = ReviewSerializer(many=True)


class ProductImageSerializer(serializers.ModelSerializer):
    # Serializer for uploading images for recipes

    class Meta:
        model = Product
        fields = ('id', 'image')
        read_only_Fields = ('id',)
        
