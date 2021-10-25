from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class DRFModel(models.Model):
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file_field = models.FileField((""), upload_to=None, max_length=100)
    description = models.CharField(max_length=500, default=None)
    created_at = models.DateTimeField((""), auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_by


# ADD NEW Report Model here!!!
class Report(models.Model):
    created_by = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    output_file = models.FileField(null=True, blank=True) #name=output_file
    description = models.CharField(max_length=500, default=None)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)
