# Django Docker Redis Celery

## Overview

This is a Django app used to integrate the Celery task manager, Redis as the broker, and using Docker to containerize the application along with starting the redis server. Tasks are in app/tasks.py and the celery integration is in celery_docker_proj/celery.py. More tasks will be added as this app progresses. Currently has an email task which can be tested using tempmail or another service. All you need is to pass a desired email address into the arguments as a string on line 18 of app/tasks.py. Make sure to collectstatic when cloning this repo/

TO DO:
- [X] Model - with file field, datetime field. created_at, updated_at, created_by
- [X] DRF
- [X] serializers - model serializer (do not use __all__)
- [X] Nested serializer displaying the user
- [X] viewset - model viewset class from drf 
- [X] add action to viewset - check drf docs - get request and get the task to run (get all objects created the day before and return.)
- [X] urls.py - use drf routers - extra action should already be included
- [] change .env over to os.environ
- [] refactor app into an api file
- [] template frontend with crud????
- [] more tasks for celery - if object is more than 90 days olds, send update or delete email.
- [] A task that will look at an instance of the DRFModel and get it by id. If a file has been created, then open the file and write something to it. If not, create a txt file and write a standard message. 

@action takes care of urls for us and links to routers.