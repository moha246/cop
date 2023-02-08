from django.urls import include, path
from rest_framework.routers import DefaultRouter

from comments.api.viewsets import CommentViewSet

comments_router = DefaultRouter()
comments_router.register(r"", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(comments_router.urls)),
]
