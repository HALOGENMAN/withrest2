from django.db import models

# Create your models here.
class A(models.Model):
    name = models.CharField(default="aman",max_length=100)
    section = models.CharField(default="A",max_length=10)
