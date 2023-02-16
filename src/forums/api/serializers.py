import django.contrib.auth.models

from rest_framework.serializers import ModelSerializer

from forums import get_forum_model
from users.api.serializers import UserSerializer


class ForumSerializer(ModelSerializer):
    class Meta:
        model = get_forum_model()
        exclude = ("members",)
        read_only_fields = model.READ_ONLY_FIELDS
