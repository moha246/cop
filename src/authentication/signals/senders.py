from django.dispatch import Signal

email_verification_signal = Signal(["user", "signal_type"])
