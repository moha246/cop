from django.conf import settings


def prefix_api_endpoint(
    path: str, version: str = settings.API_VERSION, append_slash: bool = True
) -> str:
    """Prepends api version to the url path, the settings ``API_VERSION``
    variable is used by default.
    A different api version can optionally be passed to the function
    via the ``version`` argument"""
    return f"api/{version}/{path}/" if append_slash else f"api/{version}/{path}"
