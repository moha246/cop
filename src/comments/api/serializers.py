from rest_framework import serializers

from comments.models import Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ("user", "post", "text", "likes")

    def get_likes(self, comment) -> int:
        return comment.posts.likes.count()
