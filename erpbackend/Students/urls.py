from django.urls import path
from . import views
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='MyModel')

urlpatterns = router.urls