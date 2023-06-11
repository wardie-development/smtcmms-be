from rest_framework.permissions import BasePermission


class CustomerPermissions(BasePermission):
    def has_permission(self, request, _):
        user = request.user

        if not user.is_superuser:
            return False

        return True
