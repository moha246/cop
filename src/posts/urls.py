from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.api.viewsets import PostViewSet


app_name = "posts"

router = DefaultRouter()
router.register(r"", PostViewSet, basename="posts")


urlpatterns = [
    path("", include(router.urls)),
]
