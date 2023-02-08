from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Task(TimeStampedModel):
    assigner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks_assigned",
    )
    assignee = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="assigned_tasks"
    )
