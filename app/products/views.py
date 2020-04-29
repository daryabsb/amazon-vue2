from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import generics

from rest_framework.exceptions import ValidationError

from rest_framework import viewsets, mixins, status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from core.models import Tag, Category, Product, Review
from products import serializers, permissions


class BaseProductAttrViewset(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (permissions.IsSupplierOrReadOnly,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)

class TagViewSet(BaseProductAttrViewset):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class CategoryViewSet(BaseProductAttrViewset):
    # Manage ingredients in the database
    queryset = Category.objects.order_by('id')
    serializer_class = serializers.CategorySerializer


class ReviewViewset(viewsets.ModelViewSet):
    """Base viewset for user owned recipe attributes"""
    queryset = Review.objects.order_by('-created_at')
    serializer_class = serializers.ReviewSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsReviewAuthorOrReadOnly,)

    def perform_create(self, serializer):
        """Create a new object"""
        
        serializer.save(user=self.request.user)

class ReviewCreateAPIView(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
       
        request_user = self.request.user
        # print(request_user)

        kwarg_slug = self.kwargs.get("slug")
        product = generics.get_object_or_404(Product, slug=kwarg_slug)
        # print(product)
        # if product.reviews.filter(author=request_user).exists():
        #     raise ValidationError("You have already answered this Question!")
        serializer.save(user=request_user, product=product)



class ReviewListAPIView(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Review.objects.filter(product__slug=kwarg_slug).order_by("-created_at")


class ReviewRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an answer instance to it's author."""
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated, permissions.IsAuthorOrReadOnly]




class MyProductViewset(viewsets.ModelViewSet):
    # Manage recipes in the database

    serializer_class = serializers.MyProductSerializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    lookup_field = "slug"
    # permission_classes = (IsAuthenticated,)
    permission_classes = (permissions.IsSupplierOrReadOnly,)

    # def get_queryset(self):
    #     # Retrieve the recipes to the authenticated user
    #     return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        # return apropriate serializer class
        if self.action == 'retrieve':
            return serializers.MyProductSerializer
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