from django.urls import include, path
from rest_framework.routers import DefaultRouter

from forums.api.viewsets import ForumViewSet

app_name = "forums"

forums_router = DefaultRouter()
forums_router.register("", ForumViewSet, basename="forums")

urlpatterns = [
    path("", include(forums_router.urls)),
]
