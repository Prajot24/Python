from rest_framework import routers
from django.urls import path,include
from .views import *

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewset)
router.register(r'employee',EmployeViewset)

urlpatterns = [
   path('', include(router.urls))
]