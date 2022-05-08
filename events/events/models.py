from django.db import models

# Create your models here.

class Userreg(models.Model):
    uname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    umail=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    uage = models.CharField(max_length=100)
    upref = models.CharField(max_length=100)