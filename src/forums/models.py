from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseTimeStampModel
from core.str_models import USER_MODEL


class Forum(BaseTimeStampModel):
    name = models.CharField(_("forum name"), max_length=65)
    members = models.ManyToManyField(USER_MODEL, related_name="forums")
    creator = models.CharField(_("Creator"), max_length=20)
