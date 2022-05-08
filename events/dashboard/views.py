from django.shortcuts import render,redirect
import hashlib
import csv
import pandas as pd
import os
from azure.storage.blob import  BlobServiceClient
from django.core.mail import BadHeaderError, send_mail,EmailMessage
from django.conf import settings
import base64
from django.core.files.base import ContentFile


# Create your views here.
from django.http import HttpResponse
import datetime
from .models import Event,Invitecodes,Attendees

def Dash(request):
	if not 'umail' in request.session:
		return redirect('loginpage')
	else:
		return render(request,"dash_home.html")

def Myevents(request):
	if not 'umail' in request.session:
		return redirect('loginpage')
	try:
		data=Attendees.objects.filter(username=request.session['uname'])
	except:
		data=[]
	eve={
	"event_d":data 
	}
	return render(request,"myevents.html",eve)

def organise(request):
	if not 'umail' in request.session:
		return redirect('loginpage')
	data=Event.objects.all()
	eve={
	"event_d" : data
	}
	return render(request,"organise.html",eve)

def download_csv(request, queryset):
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response

def eventpage(request):
	if not 'umail' in request.session:
		return redirect('loginpage')
	if request.method == "POST":
		if request.POST.get('downloadbutton')=='Attendee List':
			data = download_csv(request, Attendees.objects.filter(eventid=request.POST.get('eventid')))
			return HttpResponse (data, content_type='text/csv')
	data=Event.objects.get(eventid=request.POST.get('eventid'))
	data2=Invitecodes.objects.get(eventid=request.POST.get('eventid'))
	data3="no"
	eve={
	"event_d" : data,
	"event_d2" : data2,
	"event_d3" : data3
	}
	return render(request,"eventpage.html",eve)	


def newevent(request):
	if not 'umail' in request.session:
		return redirect('loginpage')
	if request.method=='POST':
		if 'uname' in request.session:
			if request.POST.get('eventname') and request.POST.get('eventid'):
				event=Event()
				hashcodeded=Invitecodes()
				event.eventname=request.POST.get('eventname')
				event.eventid=request.POST.get('eventid')
				event.eventdescription=request.POST.get('eventdescription')
				event.username=request.session['uname']
				event.eventimage=request.POST.get('imgurl')
				hash_object = hashlib.md5(request.POST.get('eventid').encode())
				hcode=hash_object.hexdigest()
				hashcodeded.eventid=request.POST.get('eventid')
				hashcodeded.hashcode=hcode
				hashcodeded.save()
				event.save()
				return redirect('myevents')
	return render(request,"newevent.html")

def invite(request,code):
	if not 'umail' in request.session:
		return redirect('loginpage')
	data2=Invitecodes.objects.get(hashcode=code)
	data=Event.objects.get(eventid=data2.eventid)
	if request.method == "POST":
		if request.POST.get('invitebutton')=='Accept':
			attendee=Attendees()
			attendee.eventid=request.POST.get('eventid')
			attendee.username=request.session['uname']
			attendee.email=request.session['umail']
			attendee.attendence=request.POST.get('attend')
			attendee.save()
	try:
		attendee=Attendees.objects.get(username=request.session['uname'])
	except:
		attendee=[]
		data3="no"
	if request.session['uname']==data.username or attendee:
		data3="no"
	else:
		data3="yes"
	eve={
	"event_d" : data,
	"event_d2" : data2,
	"event_d3" : data3
	}
	return render(request,"eventpage.html",eve)

def attended(request,code):
	str=code.split('-')
	data=Invitecodes.objects.get(hashcode=str[0])
	data2=Event.objects.get(eventid=data.eventid)
	x = datetime.datetime.now()
	print(x)
	str1 = x.strftime('%m/%d/%y-%H:%M:%S')
	if str[2]==data2.username:
		Attendees.objects.filter(username=str[1]).update(attendence="Attended",datetime=str1)
	return HttpResponse('<p>Attendence saved</p>')

def sendmails(request,code):
	link=request.GET.get('link',-1)
	data=Event.objects.get(eventid=code)
	data2=Invitecodes.objects.get(eventid=code)
	file_id=link.split('/')[-2]
	dwn_url='https://docs.google.com/spreadsheets/d/' + file_id+"/gviz/tq?tqx=out:csv"
	df = pd.read_csv(dwn_url)
	for e in df['Email']:
		print(e)
		subject, from_email, to = 'Invitaion Link-Expatica Events', 'from@example.com', e
		html_content='<p>Hai there,you are Invited to join </p>'+'<b>'+data.eventname+'</b>'+' Organised by '+'<b>'+data.username+'</b>'+' Invite link: '+' <br>'+'<a href="http://expaticaeventsy20.herokuapp.com/invite/'+data2.hashcode+'">'+'http://expaticaeventsy20.herokuapp.com/invite/'+data2.hashcode+'</a>'
		email=EmailMessage(subject,html_content,to=[e])
		email.content_subtype = "html"
		email.send()
	return redirect('dashboard')

def getimage(request):
	if request.method=="POST":
		img_data=request.POST.get('photodata')
		print(img_data)
		format, imgstr = img_data.split(';base64,')
		ext = format.split('/')[-1]
		data = ContentFile(base64.b64decode(imgstr))
		""" connect_str=""
		blob_service_client = BlobServiceClient.from_connection_string(connect_str)
		container_name="mycontainer"
		blob_client = blob_service_client.get_blob_client(container=container_name, blob=request.session['uname']+'.jpeg')
		blob_client.upload_blob(data)
		print(blob_client.url) """
		return HttpResponse(data,headers={'Content-Type': 'image/jpeg','Content- Disposition': 'attachment; filename="foo.jpeg"'})
	return render(request,"scriptimage.html")


	
	
