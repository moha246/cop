from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from authentication.roles import UserRoles


class User(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    ROLES = UserRoles

    last_name = models.CharField(_("last name"), max_length=150)
    first_name = models.CharField(_("first name"), max_length=150)
    email = models.EmailField(_("email address"), unique=True, db_index=True)
    is_verified = models.BooleanField(_("verified"), default=False)
    user_type = models.CharField(
        _("usertype"),
        max_length=20,
        choices=ROLES.choices,
        default=ROLES.MENTEE,
        db_index=True,
    )
    avatar = models.ImageField(_("Avatar"), upload_to='images/avatars/', default='images/avatars/default.png')
    # user_group = models.ForeignKey(UserGroup, null=True, blank=True, on_delete=models.SET_NULL)
    # user_type = models.CharField(max_length=20, null=True, blank=True, choices=USER_TYPES, default=MENTEE)
    address = models.CharField(max_length=255, blank=True)
    organisation = models.CharField(max_length=255, blank=True)
    dob = models.DateField(auto_now_add=False, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    current_state = models.CharField(max_length=255, blank=True)
    # is_active = models.BooleanField(default=True)

    @classmethod
    def get_response_fields(cls) -> tuple[str]:
        return (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "user_type",
            "is_active",
            "is_verified",
            "last_login",
            "date_joined",
            "address",
            "organisation",
            "dob",
            "phone",
            "designation",
            "gender",
            "current_state",
        )

    @property
    def full_name(self) -> str:
        return f"{ self.last_name } { self.first_name }".title()

    def get_absolute_url(self):
        return reverse("users:users-detail", kwargs={"user_id": self.pk})
