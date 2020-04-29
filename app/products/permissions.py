from rest_framework import permissions




class IsSupplierOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.user.is_anonymous:
            return bool(request.method in permissions.SAFE_METHODS)
        else:
            is_supplier = bool(request.user.is_supplier)

            return request.method in permissions.SAFE_METHODS or is_supplier
    
            
class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        print(request.user)
        print(bool(request.user.is_authenticated))
        # if request.user.is_authenticated:
        return bool(request.user.is_authenticated)
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

  
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# class IsSupplierOrReadOnly2(permissions.BasePermission):

#     def has_permission(self, request, view):

#         if request.method in permissions.SAFE_METHODS:
#             return True

#         if request.user and request.user.is_supplier:
#             is_supplier = request.user.is_supplier
#             return request.method in permissions.SAFE_METHODS or is_supplier