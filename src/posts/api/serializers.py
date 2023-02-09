from rest_framework import serializers

from posts.models import Post
from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "content", "commented_by", "created", "modified")

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = serializers.SerializerMethodField(read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ("posted_by", "content", "is_liked", "likes", "comments")
    
    def get_likes(self, post) -> int:
        return post.likes.count()

    def get_is_liked(self, post) -> bool:
        user = self.context["request"]["user"]
        return post.likes.filter(liked_by=user).exists()
