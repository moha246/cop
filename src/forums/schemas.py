from drf_spectacular.utils import OpenApiExample, extend_schema, extend_schema_view

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
)

add_members_schema = extend_schema(
    examples=[
        OpenApiExample(
            name="members_response_schema",
            response_only=True,
            value={
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
        )
    ],
    request=None,
)

remove_members_schema = extend_schema(
    request=None,
    responses=None,
)


extend_forums_schema = extend_schema_view(
    members=members_schema,
    add_members=add_members_schema,
    remove_members=remove_members_schema,
)
