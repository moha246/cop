from django.urls import path

from rest_framework_simplejwt.views import (
    token_blacklist,
    token_obtain_pair,
    token_refresh,
)

from authentication.api.viewsets import SignUpViewSet, VerificationViewSet,LogoutAPIView

app_name = "authentication"

urlpatterns = [
    path("refresh/", token_refresh, name="refresh"),
    path("sign-in/", token_obtain_pair, name="sign-in"),
    # path("sign-out/", token_blacklist, name="sign-out"),
    path('sign-out/', LogoutAPIView.as_view(), name='sign-out'),
    path("sign-up/", SignUpViewSet.as_view(dict(post="create")), name="sign-up"),
    path(
        "verification/<int:user_id>/accept/",
        VerificationViewSet.as_view(dict(post="accept")),
        name="accept",
    ),
    path(
        "verification/<int:user_id>/decline/",
        VerificationViewSet.as_view(dict(delete="decline")),
        name="decline",
    ),
]
