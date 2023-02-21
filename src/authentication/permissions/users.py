from rest_framework.permissions import SAFE_METHODS, BasePermission

from authentication.utils import has_admin_privileges
from authentication.utils import is_authenticated


class IsAdminOrAuthenticatedRetrieveOnly(BasePermission):
    """
    The requesting user has an admin role or is a
    read-only request to get a single user.
    """

    def has_permission(self, request, view):
        return bool(
            (view.action == "retrieve" and is_authenticated(request.user))
            or has_admin_privileges(request.user)
        )
