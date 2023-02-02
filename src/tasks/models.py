from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseTimeStampModel

User = get_user_model()


class Task(BaseTimeStampModel):
    assigner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks_assigned"
    )
    assignee = models.ManyToManyField(User, related_name="assigned_tasks")
