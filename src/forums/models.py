from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from src.authentication.roles import UserRoles


class Forum(TimeStampedModel):
    name = models.CharField(_("name"), max_length=65)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="members", db_index=True
    )
    creator = models.CharField(_("creator"), max_length=20)

    def clean(self) -> None:
        if not self.members:
            return

        mentors = self.members.filter(role=UserRoles.MENTOR)
        mentees = self.members.filter(role=UserRoles.MENTEE)

        if mentors.count() == settings.COMMITTEE_OF_PRACTICE["MENTORS_PER_FORUM"]:
            raise ValidationError("")
