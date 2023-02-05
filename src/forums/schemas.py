from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample
from users.api.serializers import UserSerializer

members_schema = extend_schema(
        examples=[
            OpenApiExample(
                name="members_response_schema",
                response_only=True,
                value=[
                        {
                            "id": 2,
                            "username": "adesandra",
                            "email": "adekunle.sandra@cop.com",
                            "first_name": "sandra",
                            "last_name": "adekunle",
                            "role": "mentor",
                            "is_active": True,
                            "is_verified": True,
                            "last_login": "2023-02-03T19:03:33.650952Z",
                            "date_joined": "2023-02-03T18:57:33.650952Z",
                        },
                        {
                            "id": 13,
                            "username": "georgina-roberts",
                            "email": "robertsgeorgina@yahoo.com",
                            "first_name": "georgina",
                            "last_name": "roberts",
                            "role": "mentee",
                            "is_active": True,
                            "is_verified": True,
                            "last_login": "2023-02-04T13:00:43.588280Z",
                            "date_joined": "2023-02-03T19:00:43.588280Z",
                        },
                ],
            )
        ],
        request=None,
        responses=UserSerializer
    )
