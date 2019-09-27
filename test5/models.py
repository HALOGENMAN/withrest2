from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class B(models.Model):
    name = models.CharField(max_length=100,default="shayak")
    section = models.CharField(max_length=50,default="A")
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)