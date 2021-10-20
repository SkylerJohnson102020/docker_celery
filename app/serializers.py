from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import DRFModel

class DRFModelSerializer(ModelSerializer):
    class Meta:
        fields = ('file_field', 'created_at','created_by', 'updted_by')
        model = DRFModel