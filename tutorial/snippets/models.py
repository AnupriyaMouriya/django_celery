from django.db import models

# Create your models here.
from django.db import models
from celery import result

class Tasks(models.Model):
    #id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20,default="PENDING")
    output = models.CharField(max_length=100,default="NO_OUTPUT")
    task_celery = models.CharField(max_length=100 ,default="xx")