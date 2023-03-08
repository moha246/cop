from django.contrib.auth import get_user_model

User = get_user_model()


def is_authenticated(user: User) -> bool:
    return user.is_authenticated and user.is_active and user.is_verified


def has_admin_privileges(user: User) -> bool:
    return (is_authenticated(user) and user.role == User.ROLES.ADMIN) or user.is_superuser
