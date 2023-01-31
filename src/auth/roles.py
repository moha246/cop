from enum import Enum

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    ADMIN = "admin", _("admin")
    MENTOR = "mentor", _("mentor")
    MENTEE = "mentee", _("mentee")
    CONSORTIUM_MEMBER = "consortium_member", _("consortium_member")

    @classmethod
    def is_valid(cls, role: str) -> bool:
        return role in cls.choices
