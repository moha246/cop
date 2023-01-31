from rest_framework.routers import SimpleRouter

from src.users.api.views import UserViewSet

app_name = "users"

user_router = SimpleRouter()
user_router.register(r"", UserViewSet, basename="users")
