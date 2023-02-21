from django.contrib.auth import get_user_model

from authentication.roles import UserRoles

User = get_user_model()


def is_authenticated(user: User) -> bool:
    return bool(
        user.is_authenticated
        and user.is_active
        and user.is_verified
    )


def has_admin_privileges(user: User) -> bool:
    return bool(
        (is_authenticated(user) and user.role == UserRoles.ADMIN) or user.is_superuser
    )
