from rest_framework import routers
from django.urls import path,include
from .views import StudentviewSet

router = routers.DefaultRouter()
router.register(r'student', StudentviewSet)

urlpatterns = [
    path('', include(router.urls))
]