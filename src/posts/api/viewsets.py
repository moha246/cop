from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from posts.api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment, LikedPost, LikedComment
from posts.schemas import posts_schema_extension


@posts_schema_extension
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
        methods=("POST",),
        url_path="comments",
    )
    def add_comment(self, request: Request, post_id: int, comment_id: int) -> Response:
        comment_data = {**request.data, **{"commented_by": request.user, "post": post_id}}
        comment_serializer = CommentSerializer(comment_data)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return Response(comment_serializer.data, status=HTTP_201_CREATED)

    @action(
        detail=True,
        methods=("PATCH",),
        url_path="comments",
    )
    def update_comment(self, request: Request, post_id: int, comment_id: int) -> Response:
        content = request.data.get("content")
        forum = self.get_object()
        comment = get_object_or_404(Comment, comment_id)
        comment_serializer = CommentSerializer(comment, data=request.data)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return Response(data=None, status=HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=("DELETE",),
        url_path="comments/(?P<comment_id>[0-9]+)",
    )
    def remove_comment(
        self, request: Request, post_id: int, comment_id: int
    ) -> Response:
        post = self.get_object()
        comment = get_object_or_404(post.comments, id=comment_id)
        post.comments.remove(comment)
        return Response(CommentSerializer(post.comments, many=True).data)

    @action(
        detail=True,
        methods=("PATCH",),
        url_path="comments/(?P<comment_id>[0-9]+)/like",
    )
    def like_comment(self, request: Request, post_id: int, comment_id: int) -> Response:
        post = self.get_object()
        comment = get_object_or_404(Comment, id=comment_id)
        post.comments.add(comment)
        return Response(CommentSerializer(post.comments, many=True).data)

    @action(
        detail=True,
        methods=("DELETE",),
        url_path="comments/(?P<comment_id>[0-9]+)/unlike",
    )
    def unlike_comment(
        self, request: Request, post_id: int, comment_id: int
    ) -> Response:
        post = self.get_object()
        comment = get_object_or_404(post.comments, id=comment_id)
        post.comments.remove(comment)
        return Response(CommentSerializer(post.comments, many=True).data)
