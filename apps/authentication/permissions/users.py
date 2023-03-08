from rest_framework.permissions import SAFE_METHODS, BasePermission

from authentication.utils import has_admin_privileges, is_authenticated


class IsAdminOrActionIsMe(BasePermission):
    """
    The requesting user has an admin role or is a
    read-only request to get object details via the me action.
    """

    def has_permission(self, request, view) -> bool:
        return bool(
            (
                is_authenticated(request.user)
                and request.method in SAFE_METHODS
                and view.action == "me"
            )
            or has_admin_privileges(request.user)
        )
