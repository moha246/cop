from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import User

ADMIN = "Admin"
MENTOR = "Mentor"
MENTEE = "Mentee"
CONSORTIUM_MEMBER = "Consortium Member"

USER_TYPES = (
    (ADMIN, _(ADMIN)),
    (MENTOR, _(MENTOR)),
    (MENTEE, _(MENTEE)),
    (CONSORTIUM_MEMBER, _(CONSORTIUM_MEMBER)),
)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, null=True, blank=True, choices=USER_TYPES, default=MENTEE)

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='groups')


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    