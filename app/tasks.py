from celery import shared_task
# from time import sleep
from django.core.mail import send_mail

from celery_docker_proj.settings import EMAIL_HOST_USER

# @shared_task
# def sleeping(time_delay):
#     sleep(time_delay)
#     return None

@shared_task
def hello():
    print("Hello there!")

@shared_task
def send_email_task():
    send_mail('Celery Test', 'Celery send_email_task is working!', EMAIL_HOST_USER, ['rokeboh251@bomoads.com'], fail_silently=False)
    return None
