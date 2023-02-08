from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

from forums.models import Forum

User = get_user_model()


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    text = models.TextField()


class LikedPost(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_liked")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
