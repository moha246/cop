from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from authentication.utils import has_admin_privileges
from posts.api.serializers import PostSerializer, CommentSerializer
from posts.models import Post, LikedPost, LikedComment
from posts.schemas import posts_schema_extension


@posts_schema_extension
class PostViewSet(ModelViewSet):
    model = Post
    serializer_class = PostSerializer
    lookup_url_kwarg = "post_id"

    def get_queryset(self):
        user = self.request.user
        if has_admin_privileges(user):
            return self.model.objects.order_by('-created')
        forums = self.model.forum.objects.filter(members=user).prefetch_related("posts")
        return forums.posts.all()

    def perform_create(self, serializer: PostSerializer) -> Post:
        serializer.save(posted_by=self.request.user)

    @action(detail=True, methods=("GET",), url_path="comments",)
    def comments(self, request: Request, post_id: int) -> Response:
        return Response(CommentSerializer(self.get_object().comments, many=True).data)

    @action(
        detail=True,
        methods=("POST",),
        url_path="comments",
    )
    def add_comment(self, request: Request, post_id: int) -> Response:
        comment_serializer = CommentSerializer(data=request.data)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save(post=self.get_object(), commented_by=request.user)
        return Response(comment_serializer.data, status=HTTP_201_CREATED)

    @action(
        detail=True,
        methods=("PATCH",),
        url_path="comments",
    )
    def update_comment(self, request: Request, post_id: int) -> Response:
        comment = get_object_or_404(self.get_object().comments, comment_id)
        comment_serializer = CommentSerializer(comment, data=request.data)
        comment_serializer.is_valid(raise_exception=True)
        comment_serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=("DELETE",),
        url_path="comments/(?P<comment_id>[0-9]+)",
    )
    def remove_comment(
        self, request: Request, post_id: int, comment_id: int
    ) -> Response:
        post = self.get_object()
        get_object_or_404(post.comments, id=comment_id).delete()
        return Response(status=HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=("POST",),
        url_path="comments/(?P<comment_id>[0-9]+)/like",
    )
    def like_comment(self, request: Request, post_id: int, comment_id: int) -> Response:
        post = self.get_object()
        comment = get_object_or_404(post.comments, id=comment_id)
        comment.likes.get_or_create(liked_by=request.user, comment=comment)
        return Response(CommentSerializer(comment).data)

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
        get_object_or_404(comment.likes, liked_by=request.user).delete()
        return Response(CommentSerializer(post.comments, many=True).data)
