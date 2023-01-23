from rest_framework import serializers
from .models import User, Group, Post,Comment
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


class GroupSerializer(serializers.ModelSerializer):
    # members = UserSerializer(many=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'members')

class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # group = GroupSerializer()
    class Meta:
        model = Post
        fields = ('id', 'user', 'group', 'content')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')        