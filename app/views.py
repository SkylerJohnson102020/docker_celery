# from django.shortcuts import get_list_or_404
# from django.contrib.auth.models import User
from app.models import DRFModel
from .serializers import DRFModelSerializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

class DRFModelViewSet(ModelViewSet):
    serializer_class = DRFModelSerializer
    queryset = DRFModel.objects.all()
