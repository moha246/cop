from django.contrib.auth import get_user_model

from authentication.roles import UserRoles

User = get_user_model()


def is_authenticated(user: User) -> bool:
    return bool(
        request.user.is_authenticated
        and request.user.is_active
        and request.user.is_verified
    )


def has_admin_privileges(user: User) -> bool:
    return bool(
        is_authenticated(user) and user.role == UserRoles.ADMIN or user.is_superuser
    )
