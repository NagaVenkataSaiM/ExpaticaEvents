from django.db import models
from home.models import Userreg


# Create your models here.
class Event(models.Model):
	eventname=models.CharField(max_length=20,null=False,blank=False)
	eventid=models.CharField(max_length=20,null=False,blank=False)
	eventdescription=models.CharField(max_length=1000,null=False,blank=False)
	eventimage=models.CharField(max_length=1000,null=False,blank=False)
	# eventdate=models.CharField(max_length=1000,null=False,black=False)
	username=models.CharField(max_length=20,null=False,blank=False)
	eventmode=models.CharField(max_length=20,null=False,blank=False)

class Invitecodes(models.Model):
	eventid=models.CharField(max_length=20,null=False,blank=False)
	hashcode=models.CharField(max_length=200,null=False,blank=False)
class Attendees(models.Model):
	eventid=models.CharField(max_length=20,null=False,blank=False)
	username=models.CharField(max_length=20,null=False,blank=False)
	email=models.CharField(max_length=30,null=False,blank=False)
	attendence=models.CharField(max_length=20,null=True,blank=False)
	datetime= models.CharField(max_length=20,null=True,blank=False)

	class Meta:
		unique_together=('eventid','username')


