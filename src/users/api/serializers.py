from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = User.get_response_fields()

    def validate_avatar(self, avatar) -> str:
        username = self.initial_data['username']
        avatar.name = F'{ username.strip() }-{ avatar.name }'
        return avatar
