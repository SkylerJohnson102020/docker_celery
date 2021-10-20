from celery import shared_task
# from time import sleep
from django.core.mail import message, send_mail, send_mass_mail

from celery_docker_proj.settings import EMAIL_HOST_USER

# @shared_task
# def sleeping(time_delay):
#     sleep(time_delay)
#     return None

@shared_task
def hello():
    print("Hello there! EMAILS SENDING BELOW!")

@shared_task
def send_email_task():
    send_mail(
        subject='Celery Test',
        message='Celery send_email_task is working!', 
        from_email=EMAIL_HOST_USER, 
        recipient_list=['rokeboh251@bomoads.com'], 
        fail_silently=False)
    return None

@shared_task
def send_bulk_email_task():
    message_1 = (
        'Email 1 from Celery_Docker', 
        'Test for send mass mail', 
        EMAIL_HOST_USER, 
        ['tegnisalto@vusra.com', 'rokeboh251@bomoads.com'])

    message_2 = (
        'Email 2 from Celery_Docker', 
        'Test 2 for send mass mail',
         EMAIL_HOST_USER,
        ['tegnisalto@vusra.com', 'rokeboh251@bomoads.com'])
        
    send_mass_mail((message_1, message_2), fail_silently=False)
    return None
