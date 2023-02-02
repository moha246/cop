from rest_framework.viewsets import ModelViewSet

from auth.permissions.users import IsAdminOrReadOnly
from forums.api.serializers import ForumSerializer


class ForumViewSet(ModelViewSet):
    serializer_class = ForumSerializer
    permission_classes = (IsAdminOrReadOnly,)
