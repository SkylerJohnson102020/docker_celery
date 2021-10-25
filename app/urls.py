from django.urls import path, include
from rest_framework import routers
from .views import DRFModelViewSet

router = routers.DefaultRouter()
router.register('model_test', DRFModelViewSet)
urlpatterns = router.urls