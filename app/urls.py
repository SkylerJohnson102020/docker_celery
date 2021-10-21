from django.urls import path, include
from rest_framework import routers
from .views import DRFModelViewSet

router = routers.DefaultRouter()
router.register('', DRFModelViewSet)
urlpatterns = router.urls