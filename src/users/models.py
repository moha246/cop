from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from auth.roles import UserRoles


class User(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    ROLES = UserRoles

    last_name = models.CharField(_("last name"), max_length=150)
    first_name = models.CharField(_("first name"), max_length=150)
    is_verified = models.BooleanField(_("verified"), default=False)
    role = models.CharField(
        _("role"), max_length=20, choices=ROLES.choices, default=ROLES.MENTEE
    )

    @classmethod
    def get_response_fields(cls) -> tuple[str]:
        return (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "is_active",
            "is_verified",
            "last_login",
            "date_joined",
        )

    @property
    def full_name(self) -> str:
        return f"{ self.last_name } { self.first_name }".title()
