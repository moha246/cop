from django.conf import settings
from django.db.models import Q
import django.contrib.auth.models
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a superuser with default credentials"

    def handle(self, *args, **options) -> None:
        email_filter = Q(email=settings.DEFAULT_SUPERUSER_DETAILS["email"])
        username_filter = Q(username=settings.DEFAULT_SUPERUSER_DETAILS["username"])
        if not User.objects.filter(email_filter | username_filter).exists():
            password = settings.DEFAULT_SUPERUSER_DETAILS.pop("password")
            user = User(**settings.DEFAULT_SUPERUSER_DETAILS)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS("Successfully created superuser"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
