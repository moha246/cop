from forums.api.viewsets import ForumViewSet
from rest_framework.routers import DefaultRouter

app_name = "forums"

forums_router = DefaultRouter()
forums_router.register("", ForumViewSet, basename="forums")

urlpatterns = forums_router.urls
