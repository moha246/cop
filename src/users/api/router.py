from rest_framework.routers import SimpleRouter

from users.api.viewset import UserViewSet

app_name = "users"

users_router = SimpleRouter()
users_router.register(r"", UserViewSet, basename="users")
