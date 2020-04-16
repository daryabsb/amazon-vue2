from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('categories', views.CategoryViewSet)
router.register('myproducts', views.MyProductViewset, base_name='myproducts')
router.register('products', views.ProductViewset, base_name='products')


app_name = 'products'

urlpatterns = [
    path('', include(router.urls))
]
