from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from src.config.settings import DEFAULT_FROM_EMAIL

User = get_user_model()


@receiver(post_save, sender=User)
def send_user_pending_verification_mail(sender, instance: User, **kwargs) -> int:
    if instance.is_superuser or instance.role == instance.ROLES.ADMIN:
        return

    subject = "Account Request Successful"

    message = f"""Dear { instance.full_name },

    Thank you for signing up for our platform. We are excited to have you onboard!

    At { settings.PLATFORM_NAME }, we strive to provide our users with the best experience possible.
    
    We believe that with your support, we can achieve our goal.

    Please hold while an administrator verifies your account within 48 hours from this email reception.

    If you have any questions or concerns, feel free to reach out to us at { settings.SUPPORT_EMAIL }. We're here to help!

    Best regards,
    { settings.PLATFORM_TEAM }
    """

    html_message = f"""
    <p>Dear { instance.full_name },</p>

    <p>Thank you for signing up for our platform. We are excited to have you onboard!</p>

    <p>At <strong>{ settings.PLATFORM_NAME }</strong>, we strive to provide our users with the best experience possible. We believe that with your support, we can achieve our goal.</p>

    <p>Please hold while an administrator verifies your account within 48 hours from this email reception.</p>
    
    <p>If you have any questions or concerns, feel free to reach out to us at <a href="mailto:{ settings.SUPPORT_EMAIL }">{ settings.SUPPORT_EMAIL }</a>. We're here to help!</p>
    
    <p>Best regards,<br>{ settings.PLATFORM_TEAM }</p>
    """

    send_mail(subject, message, "justtega97@gmail.com", [instance.email], fail_silently=False, html_message=html_message)
