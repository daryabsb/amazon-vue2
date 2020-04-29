from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('categories', views.CategoryViewSet)
router.register('products', views.MyProductViewset)
router.register('reviews', views.ReviewViewset)


app_name = 'products'

urlpatterns = [
    path('', include(router.urls)),
    
    path("products/<slug:slug>/reviews/", 
         views.ReviewListAPIView.as_view(),
         name="review-list"),

    path("products/<slug:slug>/review/", 
         views.ReviewCreateAPIView.as_view(),
         name="review-create"),

    path("reviews/<int:pk>/", 
         views.ReviewRUDAPIView.as_view(),
         name="review-detail")
         
]
