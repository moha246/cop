from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import GenericViewSet

from auth.api.serializer import SignUpSerializer


class SignUpViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    throttle_classes = (AnonRateThrottle,)
    serializer_class = SignUpSerializer
