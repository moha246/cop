from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.api.viewsets import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='comment')



urlpatterns = [
    path('', include(router.urls)),
]