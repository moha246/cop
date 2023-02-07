from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


    

