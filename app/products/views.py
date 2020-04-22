from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets, mixins, status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Category, Product
from products import serializers


class BaseRecipeAttrViewset(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)

class TagViewSet(BaseRecipeAttrViewset):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class CategoryViewSet(BaseRecipeAttrViewset):
    # Manage ingredients in the database
    queryset = Category.objects.order_by('id')
    serializer_class = serializers.CategorySerializer

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    # Manage recipes in the database
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        # Retrieve the recipes to the authenticated user
        return self.queryset.all()


class MyProductViewset(viewsets.ModelViewSet):
    # Manage recipes in the database

    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Retrieve the recipes to the authenticated user
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        # return apropriate serializer class
        if self.action == 'retrieve':
            return serializers.ProductDetailSerializer
        elif self.action == 'upload_image':
            return serializers.ProductImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new product"""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        # Upload an image to the product
        product = self.get_object()
        serializer = self.get_serializer(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )