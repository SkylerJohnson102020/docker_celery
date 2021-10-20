# Django Docker Redis Celery

## Overview

This is a Django app used to integrate the Celery task manager, Redis as the broker and backend, and using docker to containerize the application along with starting the redis server. Tasks are in app/tasks.py and the celery integration is in celery_docker_proj/celery.py. More tasks will be added as this app progresses. Currently has an email task which can be tested using tempmail or another service. All you need is to pass a desired email address into the arguments as a string on line 18 of app/tasks.py.

TO DO:
Model - with file field, datetime field. created_at, updated_at, created_by
DRF
serializers - model serializer (do not use __all__)
viewset - model viewset class from drf 
add action to viewset - check drf docs - get request and get the task to run
urls.py - use drf routers - extra action should already be included
