from django.shortcuts import get_object_or_404, redirect

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_403_FORBIDDEN
from rest_framework.exceptions import PermissionDenied

from drf_spectacular.utils import extend_schema

from authentication.utils import has_admin_privileges
from core.viewsets import PartialModelViewSet
from posts.api.serializers import CommentSerializer, PostSerializer
from posts.models import Comment, LikedComment, LikedPost, Post


class PostViewSet(PartialModelViewSet):
    model = Post
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"

    def get_queryset(self):
        user = self.request.user
        if not has_admin_privileges(user):
            raise PermissionDenied()
        return self.model.objects.order_by("-created")

    def perform_create(self, serializer: PostSerializer) -> Post:
        serializer.save(posted_by=self.request.user)


class CommentViewSet(PartialModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    lookup_url_kwarg = "comment_id"
    parent_regex = "(?P<post_id>[0-9]+)"

    def get_post_id(self) -> int:
        return self.kwargs.get("post_id")

    def get_queryset(self):
        return self.model.objects.filter(post_id=self.get_post_id())

    def perform_create(self, serializer: CommentSerializer) -> Comment:
        serializer.save(commented_by=self.request.user, post_id=self.get_post_id())

    @extend_schema(request=None, responses=None)
    @action(
        detail=True,
        methods=("POST",),
        url_path="like",
    )
    def like_comment(self, request: Request, post_id: int, comment_id: int) -> Response:
        comments = get_object_or_404(Post, pk=post_id).comments
        comment = get_object_or_404(comments, pk=comment_id)
        comment.likes.get_or_create(liked_by=request.user)
        return Response({"likes": comment.likes.count()})

    @extend_schema(request=None, responses=None)
    @action(
        detail=True,
        methods=("POST",),
        url_path="unlike",
    )
    def unlike_comment(
        self, request: Request, post_id: int, comment_id: int
    ) -> Response:
        comments = get_object_or_404(Post, pk=post_id).comments
        comment = get_object_or_404(comments, pk=comment_id)
        get_object_or_404(comment.likes, liked_by=request.user).delete()
        return Response({"likes": comment.likes.count()})
