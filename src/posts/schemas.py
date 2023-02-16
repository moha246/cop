from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample

from posts.api.serializers import CommentSerializer

extend_get_comments_schema = extend_schema(
    request=None,
    examples=[
        OpenApiExample(
            name="get_comments",
            value=[
                {
                    "id": 1,
                    "content": "I believe you can do better, great job though!",
                    "commented_by": {
                        "id": 1,
                        "username": "cop",
                        "email": "cop@gmail.com",
                        "first_name": "",
                        "last_name": "",
                        "role": "mentee",
                        "is_active": True,
                        "is_verified": True,
                        "last_login": "2023-02-10T11:25:16.232261Z",
                        "date_joined": "2023-02-08T17:45:02.683214Z",
                    },
                    "created": "2023-02-10T11:59:56.721Z",
                    "modified": "2023-02-10T11:59:56.721Z",
                },
                {
                    "id": 3,
                    "content": "This is such an awesome posts, wow!",
                    "commented_by": {
                        "id": 2,
                        "username": "mohmusa",
                        "email": "mohammad@savannah.com",
                        "first_name": "moh",
                        "last_name": "hamed",
                        "role": "mentor",
                        "is_active": True,
                        "is_verified": True,
                        "last_login": "2023-02-08T17:48:25.939374Z",
                        "date_joined": "2023-02-08T17:48:25.939374Z",
                    },
                    "created": "2023-02-10T11:59:56.721Z",
                    "modified": "2023-02-10T11:59:56.721Z",
                },
            ],
        )
    ],
)

extend_add_comment_schema = extend_update_comment_schema = extend_schema(
    request=CommentSerializer,
    responses=CommentSerializer,
)

extend_like_comment_schema = extend_unlike_comment_schema = extend_schema(
    request=None,
    responses=CommentSerializer,
)

extend_remove_comment_schema = extend_schema(
    request=None,
    responses=None,
)


posts_schema_extension = extend_schema_view(
    comments=extend_get_comments_schema,
    add_comment=extend_add_comment_schema,
    update_comment=extend_update_comment_schema,
    remove_comment=extend_remove_comment_schema,
    like_comment=extend_like_comment_schema,
    unlike_comment=extend_unlike_comment_schema,
)
