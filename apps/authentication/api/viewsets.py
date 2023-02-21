from django.contrib.auth import get_user_model
from django.utils import timezone

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import GenericViewSet

from authentication.api.serializers import SignUpSerializer
from authentication.enums import SignalType
from authentication.permissions.permissions import AdminOnly
from authentication.signals.senders import email_verification_signal
from users.api.serializers import UserSerializer

User = get_user_model()


class SignUpViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    throttle_classes = (AnonRateThrottle,)
    serializer_class = SignUpSerializer
    queryset = User.objects.order_by()
    lookup_url_kwarg = "user_id"


class VerificationViewSet(GenericViewSet):
    permission_classes = (AdminOnly,)
    lookup_url_kwarg = "user_id"
    queryset = User.objects.order_by()
    serializer_class = UserSerializer

    @extend_schema(request=None)
    @action(detail=True, methods=("POST",))
    def accept(self, *args, **kwargs) -> Response:
        user = self.get_object()
        user.is_active = user.is_verified = True
        user.date_joined = timezone.now()
        user.save(update_fields=["is_verified", "is_active"])
        email_verification_signal.send(
            sender=User, user=self.get_object(), signal_type=SignalType.ACCEPTED
        )
        return Response(
            data=self.get_serializer(user).data,
        )

    @action(detail=True, methods=("DELETE",))
    def decline(self, *args, **kwargs) -> Response:
        email_verification_signal.send(
            sender=User, user=self.get_object(), signal_type=SignalType.DECLINED
        )
        return Response(status=HTTP_204_NO_CONTENT)
