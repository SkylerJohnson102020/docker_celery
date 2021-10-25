from os import read, write
from celery import shared_task
from django.core.files.storage import default_storage
# from time import sleep
from django.core.mail import message, send_mail, send_mass_mail
from django.db.models import fields
from app.models import Report
from celery_docker_proj.settings import EMAIL_HOST_USER
from django.core.files.base import ContentFile

# @shared_task
# def sleeping(time_delay):
#     sleep(time_delay)
#     return None

@shared_task
def hello():
    print("Hello there! TASKS NOW RUNNING!")


'''Email task below designed to send a test email. This can be designed to pull from the API list of users to send a welcome email.'''
@shared_task
def send_email_task():
    print("Hello there! EMAILS FROM send_email_task SENDING BELOW!")
    send_mail(
        subject='Celery Test',
        message='Celery send_email_task is working!', 
        from_email=EMAIL_HOST_USER, 
        recipient_list=['rokeboh251@bomoads.com'], 
        fail_silently=False)
    return None

'''This task can be used to send out multiple messages to different users depending on different scenarios. One could be for welcome new users that were just added and the other can be used for saying goodbye to users deleting their account.'''
@shared_task
def send_bulk_email_task():
    print("Hello there! EMAILS FROM send_bulk_email_task SENDING BELOW!")
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

# ADD TASK HERE for file task

@shared_task
def get_file_task(report_id):
    report = Report.objects.get(id=report_id)
    # WILL NEVER get into this conditional from the UI since the POST command requires a file to be uploaded.
    if not hasattr(report, 'output_file'):
        output_file = ContentFile('Hello!!! Added from get_file_task from celery!!!! YOU MUST ADD A FILE!!')
        report.output_file.save(f'/{report.id}/test_file.txt', output_file)
    with open(report.output_file.file, 'w') as my_file:
        my_file.write("Test\n")

    return None

        