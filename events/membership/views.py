from django.shortcuts import render, redirect
from .models import MemberData
from .forms import MembershipForm

# Create your views here.
def memberdetails(request):
    return render(request,'membership/memberdetails.html',{'title':'MemberDetails'})

def viewmemberdetails(request):
    return render(request,'membership/viewmemberdetails.html',{'title':'View','members':MemberData.objects.all()}) #select statement

def addmember(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save() #inserting data into table
            return redirect('view')
        else:
            form = MembershipForm()
    return render(request,'membership/addmember.html',{'title':'New Member','form':form})


