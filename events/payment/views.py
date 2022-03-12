from django.shortcuts import render

# Create your views here.
def paymode(request):
    return render(request, "payment/paymode.html",{"title":"PayNow"})