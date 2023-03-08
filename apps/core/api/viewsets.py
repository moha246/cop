from typing import Any, Dict, Iterable

from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from drf_spectacular.utils import extend_schema


class HealthCheckViewSet(ViewSet):
    """Endpoint for checking health status of the COP API."""

    permission_classes = (AllowAny,)

    @extend_schema(request=None, responses=None)
    def list(
        self, request: Request, *args: Iterable, **kwargs: Dict[str, Any]
    ) -> Response:
        """Returns a 200 OK if the service is up and running"""
        return Response(status=HTTP_200_OK)
