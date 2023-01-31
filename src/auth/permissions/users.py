from rest_framework.permissions import BasePermission, SAFE_METHODS

from src.auth.utils import has_admin_privileges


class IsAdminOrReadOnly(BasePermission):
    """
    The requesting user has an admin role or is a
    read-only request to get a single user.
    """

    def has_permission(self, request, view):
        return bool(
            view.action != "list"
            and request.method in SAFE_METHODS
            or has_admin_privileges(request.user)
        )
