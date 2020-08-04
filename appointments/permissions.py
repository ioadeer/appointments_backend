from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it
    """
    def has_object_permission(seld, request, view,obj):
        # Read permissions are allowed to any request
        # allow GET, HEAD and OPTIONS 
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
