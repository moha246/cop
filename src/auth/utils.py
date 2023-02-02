from django.contrib.auth import get_user_model

User = get_user_model()


def has_admin_privileges(user: User) -> User | None:
    if user and all((user.is_authenticated, user.role == UserRoles.ADMIN)):
        return user
