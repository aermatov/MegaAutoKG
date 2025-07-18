from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and (
                obj.user == request.user or request.user.role == 'admin'
            )
        )
