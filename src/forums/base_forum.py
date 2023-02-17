from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
# from posts.models import Post


class BaseForum(TimeStampedModel):
    NAME_FIELD = "name"
    READ_ONLY_FIELDS = ("id", "members", "creator", "created", "modified", "by_forums_post")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.get_forum_name()

    def get_forum_name(self) -> str:
        """Return the name for this Forum."""
        return getattr(self, self.NAME_FIELD)


class AbstractBaseForum(BaseForum):
    name = models.CharField(_("name"), max_length=65)

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="members", db_index=True
    )
   
    creator = models.CharField(_("creator"), max_length=20)

    class Meta:
        verbose_name = _("forum")
        verbose_name_plural = _("forums")
        abstract = True
