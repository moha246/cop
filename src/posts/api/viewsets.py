from rest_framework.viewsets import ModelViewSet

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"
