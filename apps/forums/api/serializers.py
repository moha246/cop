from rest_framework.serializers import ModelSerializer

from forums import get_forum_model
from posts.api.serializers import SlimUserSerializer


class ForumSerializer(ModelSerializer):
    members = SlimUserSerializer(many=True, read_only=True)

    class Meta:
        model = get_forum_model()
        fields = "__all__"
        read_only_fields = model.READ_ONLY_FIELDS
