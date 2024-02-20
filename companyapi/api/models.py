from random import choices
from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField( max_length=50)
    location = models.CharField( max_length=50)
    about = models.TextField()
    added_date = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    city = models.CharField( max_length=50)
    roll = models.CharField( max_length=50, choices =(
        ('Manager','manager'),
        ('Software Dev',"SDE"),
        ('Devops','DevOps')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

