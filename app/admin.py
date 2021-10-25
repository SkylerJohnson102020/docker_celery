from django.contrib import admin
from .models import DRFModel, Report

admin.site.register([DRFModel, Report])