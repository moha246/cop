from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

from posts.models import Post

User = get_user_model()


class Comment(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_made"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()


class LikedComment(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_liked"
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
