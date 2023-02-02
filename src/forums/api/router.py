from rest_framework.routers import DefaultRouter

from forums.api.viewset import ForumViewSet

app_name = "forums"

forums_router = DefaultRouter()
forums_router.register(r"", ForumViewSet, basename="forums")
