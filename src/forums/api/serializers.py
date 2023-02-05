import django.contrib.auth.models

from rest_framework.serializers import ModelSerializer

from forums.models import Forum
from users.api.serializers import UserSerializer


class ForumSerializer(ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = Forum
        fields = "__all__"
        read_only_fields = ("creator",)
