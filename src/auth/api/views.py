from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import GenericViewSet

from src.auth.api.serializer import SignUpSerializer


class SignUpView(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    throttle_classes = AnonRateThrottle
    serializer_class = SignUpSerializer
