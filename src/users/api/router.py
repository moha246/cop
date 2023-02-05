from rest_framework.routers import SimpleRouter

from users.api.viewsets import UserViewSet

app_name = "users"

users_router = SimpleRouter()
users_router.register(r"", UserViewSet, basename="users")
