from django.db import models

from src.core.str_models import USER_MODEL


class CreatorMixin(models.Model):
    creator = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
