from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from posts.api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment, LikedPost, LikedComment


class PostViewSet(ModelViewSet):
    model = Post
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"

    def get_queryset(self):
        return self.model.objects.order_by()

    def perform_create(self, serializer: PostSerializer) -> Post:
        serializer.save(posted_by=self.request.user)

    @action(detail=True, methods=("GET",))
    def comments(self, request: Request, post_id: int) -> Response:
        return Response(ComentSerializer(self.get_object().comments, many=True).data)

    @action(
        detail=True,
        methods=("PATCH",),
        url_path="comments/(?P<comment_id>[0-9]+)/add",
    )
    def comments_add(self, request: Request, post_id: int, comment_id: int) -> Response:
        post = self.get_object()
        comment = get_object_or_404(Comment, id=comment_id)
        post.comments.add(comment)
        return Response(CommentSerializer(post.comments, many=True).data)

    @action(
        detail=True,
        methods=("DELETE",),
        url_path="comments/(?P<comment_id>[0-9]+)/remove",
    )
    def comments_remove(
        self, request: Request, post_id: int, comment_id: int
    ) -> Response:
        post = self.get_object()
        comment = get_object_or_404(post.comments, id=comment_id)
        post.comments.remove(comment)
        return Response(CommentSerializer(post.comments, many=True).data)
