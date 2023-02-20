from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from authentication.permissions.permissions import IsAdminOrReadOnly
from users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    model = User
    lookup_url_kwarg = "user_id"
    serializer_class = UserSerializer
    parser_classes = (JSONParser, MultiPartParser)
    permission_classes = (IsAdminOrReadOnly,)

    @action(detail=False, methods=["GET"])
    def me(self, request) -> Response:
        user_data = UserSerializer(request.user).data
        return Response(user_data)

    def get_queryset(self):
        return User.objects.order_by()
