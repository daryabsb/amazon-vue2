from rest_framework import generics, authentication, permissions, viewsets, mixins, status

from rest_framework.authentication import TokenAuthentication

from addresses.serializers import AddressSerializer

from core.models import Address

# Create your views here.
class AddressViewset(viewsets.ModelViewSet):
    """Base viewset for user owned recipe attributes"""
    queryset = Address.objects.order_by('-date_added')
    serializer_class = AddressSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Create a new object"""
        
        serializer.save(user=self.request.user)