import django.contrib.auth.models
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from forums import get_forum_model
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer

User = get_user_model()

class ForumSerializer(ModelSerializer):
    members =  UserSerializer(many=True)
    # by_forums_post = PostSerializer(read_only=True)

    class Meta:
        model = get_forum_model()
        fields = '__all__'
        # exclude = ("members",)
        read_only_fields = model.READ_ONLY_FIELDS
