
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


# Create your views here.
class StudentviewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['city']
    search_fields = ['name','city']

    



    

