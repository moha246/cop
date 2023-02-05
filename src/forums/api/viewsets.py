from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema_view

from authentication.permissions.users import IsAdminOrReadOnly
from forums.api.serializers import ForumSerializer
from forums.models import Forum
from users.api.serializers import UserSerializer
from forums.schemas import members_schema


@extend_schema_view(
    members=members_schema,
    members_add=members_schema,
    members_remove=members_schema,
)
class ForumViewSet(ModelViewSet):
    serializer_class = ForumSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = "forum_id"

    def get_queryset(self):
        return Forum.objects.order_by()

    def perform_create(self, serializer: ForumSerializer) -> Forum:
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=("GET",))
    def members(self, request: Request, forum_id: int) -> Response:
        return Response(UserSerializer(self.get_object().members, many=True).data)

    @action(detail=True, methods=("PUT",), url_path="members/<int:member_id>/add")
    def members_add(self, request: Request, forum_id: int, member_id: int) -> Response:
        forum: Forum = self.get_object()
        member = get_object_or_404(User, id=member_id)
        forum.members.add(member)
        return Response(UserSerializer(forum.members, many=True).data)

    @action(detail=True, methods=("DELETE",), url_path="members/<int:member_id>/remove")
    def members_remove(
        self, request: Request, forum_id: int, member_id: int
    ) -> Response:
        forum: Forum = self.get_object()
        member = get_object_or_404(forum.members, id=member_id)
        forum.members.remove(member)
        return Response(UserSerializer(forum.members, many=True).data)
