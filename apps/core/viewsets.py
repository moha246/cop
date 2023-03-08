from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from core.mixins import PartialUpdateMixin


class PartialModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    PartialUpdateMixin,
    GenericViewSet,
):
    pass
