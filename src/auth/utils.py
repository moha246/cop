from django.contrib.auth.models import AbstractUser
from src.auth.roles import UserRoles


def has_admin_privileges(user: AbstractUser) -> AbstractUser | None:
    if user and all((user.is_authenticated, user.role == UserRoles.ADMIN)):
        return user
