from rest_framework import serializers
from django.contrib.auth import get_user_model

from authentication.roles import UserRoles
from posts.models import Comment, Post


User = get_user_model()


class SlimUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "avatar",
        )


class CommentSerializer(serializers.ModelSerializer):
    commented_by = SlimUserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "content", "commented_by", "created", "modified", "likes")
        read_only_fields = ("id", "commented_by", "created", "modified", "likes")

    def get_likes(self, comment) -> int:
        return comment.likes.count()


class PostSerializer(serializers.ModelSerializer):
    posted_by = SlimUserSerializer(read_only=True)
    # is_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "posted_by", "content", "likes", "forum")
        read_only_fields = ("id", "posted_by", "likes")

    # def get_is_liked(self, post) -> bool:
    #     user = self.context["request"]["user"]
    #     return post.likes.filter(liked_by=user).exists()
