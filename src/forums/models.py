from django.db import models
from django.utils.translation import gettext_lazy as _

from src.core.mixins import TimeStampMixin
from src.core.str_models import USER_MODEL


class Forum(TimeStampMixin):
    name = models.CharField(_("Forum name"), max_length=65)
    members = models.ManyToManyField(USER_MODEL, related_name="forums")
    creator = models.CharField(_("Creator"), max_length=20)
