from django.urls import path, include
from rest_framework.routers import DefaultRouter

from addresses import views

router = DefaultRouter()
router.register('addresses', views.AddressViewset)


app_name = 'address'

urlpatterns = [
    path('', include(router.urls)),         
]