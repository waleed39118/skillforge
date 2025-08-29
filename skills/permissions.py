from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user'):
            return obj.user == request.user or request.user.is_staff
        if hasattr(obj, 'skill'):
            return obj.skill.user == request.user or request.user.is_staff
        return False

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated