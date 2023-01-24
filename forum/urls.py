from django.urls import path

from . import viewsets

urlpatterns = [
    # path('users/', viewsets.UserView.as_view(), name='users'),
    path("login/", viewsets.PhemTokenPairView.as_view(), name="login"),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('groups/', views.UserGroupView.as_view(), name='user-groups'),
    # path('user_types/', views.user_types, name='user-types'),
    path("logout/", viewsets.LogoutAPIView.as_view(), name="auth_logout"),
    # path('me/', views.me, name='user-profile'),
    # path('users/<int:pk>/', views.UserViewDetail.as_view()),
    # path('tasks/', views.AssignTaskView.as_view()),
]
