from rest_framework.serializers import ModelSerializer

from forums import get_forum_model
from users.api.serializers import UserSerializer


class ForumSerializer(ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = get_forum_model()
        fields = "__all__"
        read_only_fields = model.READ_ONLY_FIELDS
