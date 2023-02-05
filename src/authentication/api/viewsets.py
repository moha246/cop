from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import GenericViewSet, ViewSet

from authentication.api.serializers import SignUpSerializer
from authentication.api.serializers import VerificationSerializer
from authentication.permissions.permissions import AdminOnly


User = get_user_model()

class SignUpViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    throttle_classes = (AnonRateThrottle,)
    serializer_class = SignUpSerializer
    queryset = User.objects.order_by()
    lookup_url_kwarg = "user_id"


class VerificationViewSet(ViewSet):
    permission_classes = (AdminOnly,)
    serializer_class = VerificationSerializer
    lookup_url_kwarg = "user_id"
    queryset = User.objects.order_by()

    @action(detail=True, methods=("POST",))
    def accept(self, *args, **kwargs) -> Response:
        user = self.get_object()
        user.is_verified = True
        user.is_active = True
        user.save(update_fields=["is_verified", "is_active"])
        return Response(data="User's request successfully accepted.'.")

    @action(detail=True, methods=("POST",))
    def decline(self, *args, **kwargs) -> Response:
        user = self.get_object()
        return Response(data="User's request successfully declined.")
