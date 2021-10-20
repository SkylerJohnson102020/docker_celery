from django.db import models
from django.contrib.auth import get_user_model

class DRFModel(models.Model):
    file_field = models.FileField((""), upload_to=None, max_length=100)
    created_at = models.DateTimeField((""), auto_now=True, auto_now_add=False)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_by