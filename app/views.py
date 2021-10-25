# from django.shortcuts import get_list_or_404
# from django.contrib.auth.models import User
from app.models import DRFModel
from .serializers import DRFModelSerializer, SimpleDRFModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS
from rest_framework import status
# from rest_framework.response import Response

class DRFModelViewSet(ModelViewSet):
    serializer_class = DRFModelSerializer
    simple_serialzier_class = SimpleDRFModelSerializer
    queryset = DRFModel.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return super().get_serializer_class()
        return self.simple_serialzier_class
     
    # add action here
    @action(detail=True, methods=['GET'])
    def extra_action(self, request, pk):
        print(pk)
        return Response(data={'key': 'Test'}, status=status.HTTP_200_OK)
