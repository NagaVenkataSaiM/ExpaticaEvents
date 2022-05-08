from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
  path('dashboard/',views.Dash,name="dashboard"),
  path('myevents/',views.Myevents,name="myevents"),
  path('organise/',views.organise),
  path('eventpage/',views.eventpage),
  path('newevent/',views.newevent),
  path('invite/<str:code>/',views.invite,name='invite'),
  path('attend/<str:code>/',views.attended),
  path('output/<str:code>/',views.sendmails,name="script"),
  path('getimage/',views.getimage,name="getimage"),
  ]