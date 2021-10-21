from os import read
from django.db.models import fields
from django.db.models.fields.related import RelatedField
from rest_framework.serializers import ModelSerializer
from .models import DRFModel
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        model = User

class SimpleDRFModelSerializer(ModelSerializer):    
    class Meta:
        fields = ('id', 'created_by','file_field', 'description', 'created_at', 'updated_at')
        model = DRFModel

class DRFModelSerializer(ModelSerializer):
    created_by = UserSerializer()
    
    class Meta:
        fields = ('id', 'created_by','file_field', 'description', 'created_at', 'updated_at')
        model = DRFModel
