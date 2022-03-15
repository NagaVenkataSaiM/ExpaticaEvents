from django.shortcuts import render
from .models import PayDetails
# Create your views here.
def mode(request):
    return render(request,'paymode.html',{'title':'PayNow','payments':PayDetails.objects.all()})