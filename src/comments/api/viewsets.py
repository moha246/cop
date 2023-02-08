from rest_framework.viewsets import ModelViewSet

from comments.models import Comment, Like
from comments.api.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = "comment_id"
