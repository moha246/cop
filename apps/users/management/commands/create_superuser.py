import django.contrib.auth.models
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser with default credentials'

    def handle(self, *args, **options) -> None:
        superuser_details = {
            "email": "justtega97@gmail.com",
            "first_name": "Tega",
            "last_name": "Israel",
            "username": "code-intensive",
            "password": "CopU$Er01",
            "role": "admin",
            "is_superuser": True,
            "is_active": True,
            "is_verified": True,
            "phone_number": "09025594767",
            "designation": "Admin Building",
            "current_state": "Best",
            "gender": "male",
        }
        if not User.objects.filter(superuser_details["email"]).exists():
            password = superuser_details.pop("password")
            created = User(**superuser_details)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS("Successfully created superuser"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))

