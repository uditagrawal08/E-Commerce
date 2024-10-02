from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email,email_token):

    subject = 'Your account need to verify'
    email_from=settings.EMAIL_HOST_USER
    message = f'Click on the link to verify your account http://127.0.0.1:8000/accounts/activate/{email_token}'

    send_mail(subject,message,email_from,[email]) 