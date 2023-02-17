from django.contrib.auth import get_user_model


from authentication.roles import UserRoles

User = get_user_model()


def has_admin_privileges(user: User) -> User | None:
    if not user or user.is_anonymous:
        return None
    return user.role == UserRoles.ADMIN or user.is_superuser
