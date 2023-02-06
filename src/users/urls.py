from django.urls import path, include

from rest_framework.routers import SimpleRouter

from users.api.viewsets import UserViewSet

app_name = "users"

users_router = SimpleRouter()
users_router.register(r"", UserViewSet, basename="users")


urlpatterns = [
    path(r"", include(users_router.urls)),
]
