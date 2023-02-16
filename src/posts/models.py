from django.contrib.auth import get_user_model
from django.db import models

from django_extensions.db.models import TimeStampedModel

from forums import get_forum_model

User = get_user_model()
Forum = get_forum_model()


class Post(TimeStampedModel):
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", db_index=True
    )
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, db_index=True)
    content = models.TextField(max_length=500)


class LikedPost(TimeStampedModel):
    liked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts_liked", db_index=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes", db_index=True
    )


class Comment(TimeStampedModel):
    commented_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_made", db_index=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", db_index=True
    )
    content = models.TextField(max_length=250)


class LikedComment(TimeStampedModel):
    liked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_liked", db_index=True
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="likes", db_index=True
    )
