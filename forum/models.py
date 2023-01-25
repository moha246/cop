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
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    user_type = models.CharField(
        max_length=20, null=True, blank=True, choices=USER_TYPES, default=MENTEE
    )

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="creator", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, related_name="modifier", on_delete=models.CASCADE
    )


class Admins(models.Model):
    members = models.ManyToManyField(User, related_name="admin_groups")


class Group(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    admins = models.OneToOneField(
        Admins, related_name="admins", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="groups")


class Post(BaseModel):
    groups = models.ForeignKey(Group, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField(max_length=800)


class Comment(BaseModel):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=450)
