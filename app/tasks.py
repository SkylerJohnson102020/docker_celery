from celery import shared_task
from time import sleep

# @shared_task
# def sleeping(time_delay):
#     sleep(time_delay)
#     return None

@shared_task
def hello():
    print("Hello there!")
