from datetime import timedelta

from django.core import mail
from rest_framework_simplejwt.tokens import RefreshToken


class EmailToken(RefreshToken):
    lifetime = timedelta(days=30)


class Utils:
    @staticmethod
    def send_email(subject, body, to, **kwargs):
        message = mail.EmailMessage(subject, body, to=to, **kwargs)
        message.send()

    @staticmethod
    def create_email_token(user):
        return EmailToken().for_user(user).access_token

