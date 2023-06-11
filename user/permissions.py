from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    protected_methods = ("GET", "PATCH", "PUT", "DELETE")

    def has_permission(self, request, _):
        user = request.user
        method = request.method

        if method in self.protected_methods and not user.is_authenticated:
            return False

        return True
