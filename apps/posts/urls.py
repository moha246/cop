from django.urls import include, path

from rest_framework.routers import DefaultRouter
from nested_routers.routers import NestedDefaultRouter

from posts.api.viewsets import PostViewSet, CommentViewSet


app_name = "posts"

posts_router = DefaultRouter()
posts_router.register(r"posts", PostViewSet, basename="posts")

comments_router = NestedDefaultRouter(posts_router, "posts", lookup="post_id")
comments_router.register(r"comments", CommentViewSet, basename="comments")


urlpatterns = [
    path("", include(posts_router.urls)),
    path("", include(comments_router.urls)),
]
