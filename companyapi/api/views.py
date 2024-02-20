from multiprocessing import context
from sys import exception
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serialize = EmployeeSerializer(emp, many = True, context={'request':request})
            return Response(emp_serialize.data)
        except Exception as e:
            return Response({
                "Message":"Company Not found"
            })

class EmployeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
