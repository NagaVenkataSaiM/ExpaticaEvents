from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Userreg
import mysql.connector
import matplotlib.pyplot as plt
import io
import urllib,base64
import numpy as np
# Create your views here.
def home(request):
    return render(request,'home.html', {})

def services(request):
    return render(request,'services.html',{})

def graph(request):
    return render(request, 'graph.html',{})

def profile(request):
    return render(request, 'profile.html', {})

def comingsoon(request):
    return render(request, 'comingsoon.html', {})

def sample(request):
    if not 'umail' in request.session:
        return redirect('loginpage')
    umail = request.session['umail']
    uname=request.session['uname']
    return render(request, 'sample.html', {'umail': umail, 'uname': uname})


def Userregestration(request):
    if 'umail' in request.session:
        return redirect('sample')
    if request.method == "POST":
        umail = request.POST.get('umail')
        uname = request.POST.get('uname')
        umailObj = Userreg.objects.all().filter(umail=umail)
        if not umailObj:
            saverecord = Userreg()
            saverecord.uname = request.POST.get('uname')
            saverecord.gender = request.POST.get('gender')
            saverecord.umail = request.POST.get('umail')
            saverecord.pwd = request.POST.get('pwd')
            saverecord.uage = request.POST.get('uage')
            saverecord.upref = request.POST.get('upref')

            saverecord.save()
            messages.success(request, "  Regestration is succesfull!.....")
            print("  Regestration is succesfull!.....")
            request.session['umail'] = umail
            request.session['uname'] = uname
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
            request.session['uname'] = Userdetails.uname

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


def stat(request):
    mydb = mysql.connector.connect(host="127.0.0.1",
                                   user="root",
                                   password="1142",
                                   database="mydb")
    mycursor = mydb.cursor()
    mycursor.execute("select upref from newreg")
    result = mycursor.fetchall

    upref = []
    for i in mycursor:

        upref.append(i[0])
    bar_plt = plt
    plot = plt
    hist_plot = plt

    bar_plt.hist(upref)
    bar_plt.xlabel("Mode")

    bar_plt.ylabel("Strength")
    bar_plt.title("Costumers info")
    bar_plt.rc('axes', edgecolor='white')

    fig = bar_plt.gcf()

    buf = io.BytesIO()
    fig.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri1 = urllib.parse.quote(string)

    # plot.bar(gend, tran)
    # plot.xlabel("gender")
    # plot.ylabel("transport")
    # plot.title("traveler's Rate")
    # fig=plot.gcf()
    # buf=io.BytesIO()
    # fig.savefig(buf,format='png')
    # buf.seek(0)
    # string=base64.b64encode(buf.read())
    # uri2=urllib.parse.quote(string)

    # hist_plot.scatter(gend, tran)
    # hist_plot.xlabel("gender")
    # hist_plot.ylabel("transport")
    # hist_plot.title("traveler's Bio")
    # fig=hist_plot.gcf()
    # buf=io.BytesIO()
    # fig.savefig(buf,format='png')
    # buf.seek(0)
    # string=base64.b64encode(buf.read())
    # uri3=urllib.parse.quote(string)
    context = {
        'data1': uri1,
        'data2': uri1,
        'data3': uri1
    }

    return render(request, 'graph.html', context)