from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
