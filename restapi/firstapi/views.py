from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import*
from rest_framework.renderers import JSONRenderer

# Create your views here.
def StudentDetails(request):
    st = Student.objects.get(id=1)
    ser = studentSerializer(st)
    Json_data = JSONRenderer.render(ser.data)
    return HttpResponse(Json_data,content_type = 'application/json')
