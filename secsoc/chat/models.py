from django.db import models
from datetime import datetime

class Community(models.Model):
    name = models.CharField(max_length=100000)

class Message(models.Model):
    value= models.CharField(max_length=100000)
    user= models.CharField(max_length=100000)
    room= models.CharField(max_length=100000)
    date = models.DateTimeField(default= datetime.now, blank=True)
 