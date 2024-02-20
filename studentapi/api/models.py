
from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.IntegerField()
    name = models.CharField( max_length=50)
    city = models.CharField( max_length=50)


