from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.models import Post
from posts.models import Comment
from users.api.serializers import UserSerializer
from src.authentication.roles import UserRoles


User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserSerializer

    class Meta:
        model = Comment
        fields = ("id", "content", "commented_by", "created", "modified")
        read_only_fields = ("id", "commented_by", "created", "modified")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    posted_by = serializers.SlugRelatedField(required=False, queryset=User.objects.all(),slug_field='username')
    # is_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "posted_by", "content", "likes", "comments", "forum")
        read_only_fields = ("id", "posted_by", "likes")

    def get_likes(self, post) -> int:
        return post.likes.count()

    # def get_is_liked(self, post) -> bool:
    #     user = self.context["request"]["user"]
    #     return post.likes.filter(liked_by=user).exists()

    def validate_forum(self, forum) -> int:
        request = self.context.get('request')
        if not request:
            return

        print(request)
        user = request.user

        has_admin_privileges = user.is_superuser or user.role == UserRoles.ADMIN

        if not (has_admin_privileges or forum in user.forums):
            raise serializers.ValidationError(
                "You do not have permission to post to this forum,\n"
                "If you feel there is any misunderstanding, kindly reach "
                "out to an adminstrator to rectify the issue."
            )

        return forum
