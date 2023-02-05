from rest_framework.routers import DefaultRouter

from tasks.api.viewsets import TaskViewSet

app_name = "tasks"

tasks_router = DefaultRouter()
tasks_router.register(r"", TaskViewSet, basename="tasks")
