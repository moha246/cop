from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Forum(TimeStampedModel):
    name = models.CharField(_("name"), max_length=65)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="forums", verbose_name=_("members")
    )
    creator = models.CharField(_("creator"), max_length=20)
