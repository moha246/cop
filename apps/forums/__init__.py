from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_forum_model():
    """
    Return the Forum model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.FORUM_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "FORUM_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "FORUM_MODEL refers to model '%s' that has not been installed"
            % settings.FORUM_MODEL
        )
