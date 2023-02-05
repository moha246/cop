from django.db import models

from django_extensions.db.models import TimeStampedModel
from core.str_models import USER_MODEL


class Task(TimeStampedModel):
    assigner = models.ForeignKey(
        USER_MODEL, on_delete=models.CASCADE, related_name="tasks_assigned"
    )
    assignee = models.ManyToManyField(USER_MODEL, related_name="assigned_tasks")
