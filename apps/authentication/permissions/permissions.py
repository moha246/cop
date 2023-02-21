from rest_framework.permissions import SAFE_METHODS, BasePermission

from authentication.utils import is_authenticated, has_admin_privileges


class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    The requesting user has an admin role or is a
    read-only request to get a single user.
    """

    def has_permission(self, request, view) -> bool:
        return bool(
            (
                is_authenticated(request.user)
                and view.action != "list"
                and request.method in SAFE_METHODS
            )
            or has_admin_privileges(request.user)
        )


class AdminOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return has_admin_privileges(request.user)
