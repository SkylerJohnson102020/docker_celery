from os import read
from django.db.models import fields
from django.db.models.fields.related import RelatedField
from rest_framework.serializers import ModelSerializer
from .models import DRFModel
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email', 
            'first_name',
            'last_name')
            

class SimpleDRFModelSerializer(ModelSerializer):    
    class Meta:
        model = DRFModel
        fields = (
            'id', 
            'created_by',
            'file_field', 
            'description', 
            'created_at', 
            'updated_at')

class DRFModelSerializer(ModelSerializer):
    created_by = UserSerializer()
    
    class Meta:
        model = DRFModel
        fields = (
            'id', 
            'created_by',
            'file_field', 
            'description', 
            'created_at', 
            'updated_at')
