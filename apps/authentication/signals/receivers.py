from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import mail_admins, send_mail
from django.dispatch import receiver

from authentication.enums import SignalType
from authentication.signals.senders import email_verification_signal


User = get_user_model()

@receiver(email_verification_signal, sender=User)
def pending_verification_mail(
    sender, user: User, signal_type: SignalType, **kwargs
) -> int | None:
    is_an_admin = user.is_superuser or user.role == user.ROLES.ADMIN
    is_active_and_verified = user.is_verified and user.is_active

    if is_an_admin or signal_type != SignalType.PENDING:
        return None

    if is_active_and_verified:
        return -1

    subject = "Account Request Pending"

    user_message = f"""
Dear { user.full_name },

Thank you for signing up for our platform. We are excited to have you onboard!

At { settings.PLATFORM_NAME }, we strive to provide our users with the best experience possible.

We believe that with your support, we can achieve our goal.

Please hold while an administrator verifies your account within 48 hours from this email reception.

If you have any questions or concerns, feel free to reach out to us at { settings.SUPPORT_EMAIL }. We're here to help!

Best regards,
{ settings.PLATFORM_TEAM }
    """

    user_html_message = f"""
<p>Dear { user.full_name },</p>

<p>Thank you for signing up for our platform. We are excited to have you onboard!</p>

<p>At <strong>{ settings.PLATFORM_NAME }</strong>, we strive to provide our users with the best experience possible. 

We believe that with your support, we can achieve our goal.</p>

<p>Please hold while an administrator verifies your account within 48 hours from this email reception.</p>

<p>If you have any questions or concerns, feel free to reach out to us at 

<a href="mailto:{ settings.SUPPORT_EMAIL }">{ settings.SUPPORT_EMAIL }</a>. We're here to help!</p>

<p>Best regards,<br>{ settings.PLATFORM_TEAM }</p>
    """

    admin_mail_subject = "Account Request - Verification Needed"

    admin_message = f"""
This is to inform you of a new account request by { user.full_name }.

The user's details can be found here: { user.get_absolute_url() },

Ensure to respond within the next 48 hours.
    """

    admin_html_message = f"""
<p>This is to inform you of a new account request by <strong>{ user.full_name }</strong>.</p><br />"

<p>The user's details can be found here: { user.get_absolute_url() }</p><br />,"

<p><i>Ensure to respond within the next 48 hours.</i></p>"
    """

    send_mail(
        subject=subject,
        message=user_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
        html_message=user_message,
    )
    mail_admins(
        subject=admin_mail_subject,
        message=admin_message,
        fail_silently=False,
        html_message=admin_html_message,
    )
    return 1


@receiver(email_verification_signal, sender=User)
def verification_success_mail(
    sender, user: User, signal_type: SignalType, **kwargs
) -> int | None:
    is_an_admin = user.is_superuser or user.role == user.ROLES.ADMIN
    is_active_and_verified = user.is_verified and user.is_active

    if is_an_admin or signal_type != SignalType.ACCEPTED:
        return None

    if not is_active_and_verified:
        return -1

    subject = "Account Request Successful"

    user_message = f"""
Dear { user.full_name },

Thank you for signing up for our platform. We are excited to have you onboard!

As promised, your account has been verified and found to be acceptable by our admins.

Please visit { user.get_absolute_url() } to view your profile.

If you have any questions or concerns, feel free to reach out to us at { settings.SUPPORT_EMAIL }.

Sincerely,
{ settings.PLATFORM_TEAM }
    """

    html_message = f"""
<p>Hello { user.full_name },</p><br/>

<p>As promised, your account has been verified and found to be acceptable by our admins.</p><br/>

<p>Please visit { user.get_absolute_url() } to view your profile.</p><br/>

<p>If you have any questions or concerns, feel free to reach out to us at { settings.SUPPORT_EMAIL }.</p><br/>

<p>Best Wishes,</p></br/>
<p>{ settings.PLATFORM_TEAM }</p>
    """
    send_mail(
        subject=subject,
        message=user_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
        html_message=html_message,
    )
    return 1


@receiver(email_verification_signal, sender=User)
def verification_declined_mail(
    sender, user: User, signal_type: SignalType, **kwargs
) -> int | None:
    is_an_admin = user.is_superuser or user.role == user.ROLES.ADMIN
    is_active_and_verified = user.is_verified and user.is_active

    if is_an_admin or signal_type != SignalType.DECLINED:
        return None

    if is_active_and_verified:
        return -1

    subject = "Account Request Declined"

    user_message = f"""
Hello { user.full_name },

Thank you for signing up for our platform. We appreciate the value you place on us!

As promised, your account request has been reviewed but sadly found to be unacceptable by our admins.

If you have any questions or concerns, feel free to reach out to us at { settings.SUPPORT_EMAIL }.

Best Wishes,
{ settings.PLATFORM_TEAM }
    """

    html_message = f"""
<p>Hello { user.full_name },</p><br/>

<p>Thank you for signing up for our platform. We appreciate the value you place on us!</p><br/>

<p>As promised, your account request has been reviewed but sadly found to be unacceptable by our admins.</p><br/>

<p>If you have any questions or concerns, feel free to reach out to us at { settings.SUPPORT_EMAIL }.</p><br/>

<p>Best Wishes,</p></br/>
<p>{ settings.PLATFORM_TEAM }</p>
    """
    send_mail(
        subject=subject,
        message=user_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
        html_message=html_message,
    )
    user.delete()
    return 1
