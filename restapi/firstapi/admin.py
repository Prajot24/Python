from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    dic_list = ['id','name','city','roll_no']