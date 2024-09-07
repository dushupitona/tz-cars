from rest_framework.permissions import BasePermission

class OwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE']:
            return obj.owner.id == request.user.id
        return True