from django.conf import settings
from django.core.mail import send_mail


def send_welcome_email(to_email):
    subject = "Welcome to Our Service"
    message = "Thank you for signing up for our service! We are excited to have you with us."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [to_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
