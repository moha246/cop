from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


ADMIN = "Admin"
MENTOR = "Mentor"
MENTEE = "Mentee"
CONSORTIUM_MEMBER = "Consortium Member"

UserRoles = (
    (ADMIN, _(ADMIN)),
    (MENTOR, _(MENTOR)),
    (MENTEE, _(MENTEE)),
    (CONSORTIUM_MEMBER, _(CONSORTIUM_MEMBER)),
)


class User(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    is_verified = models.BooleanField(_("verified"), default=False)
    role = models.CharField(_("role"), max_length=20, choices=UserRoles, default=MENTEE)
