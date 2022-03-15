from django.db import models

# Create your models here.

class PayDetails(models.Model):
    uname=models.CharField(max_length=100)
    accno=models.CharField(max_length=100)
    bankname=models.CharField(max_length=100)
    class Meta:
        db_table="paydet"
