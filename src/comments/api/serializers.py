from rest_framework import serializers
from comments.models import Comment,Like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'post', 'text')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'comment')

