from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.api.viewsets import PostViewSet

router = DefaultRouter()
router.register(r"", PostViewSet, basename="comment")


urlpatterns = [
    path("", include(router.urls)),
]
