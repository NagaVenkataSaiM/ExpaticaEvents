from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import  Userreg
# Create your views here.
def home(request):
    return render(request,'home.html', {})


def sample(request):
    if not 'umail' in request.session:
        return redirect('loginpage')
    umail = request.session['umail']
    return render(request, 'sample.html', {'umail': umail})


def Userregestration(request):
    if 'umail' in request.session:
        return redirect('sample')
    if request.method == "POST":
        umail = request.POST.get('umail')
        umailObj = Userreg.objects.all().filter(umail=umail)
        if not umailObj:
            saverecord = Userreg()
            saverecord.uname = request.POST.get('uname')
            saverecord.gender = request.POST.get('gender')
            saverecord.umail = request.POST.get('umail')
            saverecord.pwd = request.POST.get('pwd')
            saverecord.save()
            messages.success(request, "  Regestration is succesfull!.....")
            print("  Regestration is succesfull!.....")
            request.session['umail'] = umail
            return redirect('sample')
        else:
            print("User Already Exists")
            return redirect('loginpage')
    return render(request, 'reg1.html')


def loginpage(request):
    if 'umail' in request.session:
        return redirect('sample')
    if request.method == "POST":
        try:
            print(request.POST['umail'], request.POST['pwd'])
            Userdetails = Userreg.objects.get(umail=request.POST['umail'], pwd=request.POST['pwd'])
            print("uname", Userdetails)
            request.session['umail'] = Userdetails.umail
            return redirect('sample')
        except Userreg.DoesNotExist as e:
            print('Username / Password invalid..!')
            messages.success(request, 'Username / Password invalid..!')
    return render(request, 'reg1.html')
    # if request.method=='POST':
    #     form= userreg(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"Travel.html")
    # else:
    #     form=userreg()
    # return render(request,'reg1.html',{'form':form})


def logout(request):
    if 'umail' in request.session:
        del request.session['umail']
    return redirect('loginpage')