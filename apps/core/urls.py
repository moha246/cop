from django.urls import path

from rest_framework.routers import DefaultRouter

from core.api.viewsets import HealthCheckViewSet


core_router = DefaultRouter()
core_router.register("", HealthCheckViewSet, basename="health-check")

urlpatterns = core_router.urls
