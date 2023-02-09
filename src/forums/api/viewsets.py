from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view
from rest_framework import request
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions.permissions import AdminOnly
from forums.api.serializers import ForumSerializer
from forums.models import Forum
from forums.schemas import members_schema
from users.api.serializers import UserSerializer

User = get_user_model()


@extend_schema_view(
    members=members_schema,
    members_add=members_schema,
    members_remove=members_schema,
)
class ForumViewSet(ModelViewSet):
    serializer_class = ForumSerializer
    permission_classes = (AdminOnly,)
    lookup_url_kwarg = "forum_id"

    def get_queryset(self):
        return Forum.objects.order_by()

    def perform_create(self, serializer: ForumSerializer) -> Forum:
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=("GET",))
    def members(self, request: Request, forum_id: int) -> Response:
        return Response(UserSerializer(self.get_object().members, many=True).data)

    @action(
        detail=True,
        methods=("PATCH",),
        url_path="members/(?P<member_id>[0-9]+)/add",
    )
    def members_add(self, request: Request, forum_id: int, member_id: int) -> Response:
        forum = self.get_object()
        member = get_object_or_404(User, id=member_id)
        forum.members.add(member)
        return Response(UserSerializer(forum.members, many=True).data)

    @action(
        detail=True,
        methods=("DELETE",),
        url_path="members/(?P<member_id>[0-9]+)/remove",
    )
    def members_remove(
        self, request: Request, forum_id: int, member_id: int
    ) -> Response:
        forum = self.get_object()
        member = get_object_or_404(forum.members, id=member_id)
        forum.members.remove(member)
        return Response(UserSerializer(forum.members, many=True).data)
