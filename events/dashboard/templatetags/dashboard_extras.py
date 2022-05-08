from django import template
import qrcode
import qrcode.image.svg
from io import BytesIO
from dashboard.models import Invitecodes,Event

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def addall(arg1,arg2):
    str1="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="
    print(str1+"'"+arg1+"-"+arg2+"'")
    return str1+"'"+arg1+"-"+arg2+"'"

@register.filter
def generateqr(arg1,arg2):
    strx=arg1+"-"+arg2
    context = {}
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(strx, image_factory=factory, box_size=10)
    stream = BytesIO()
    img.save(stream)
    context["svg"] = stream.getvalue().decode()
    return context

@register.filter
def getstorecode(arg1):
    data=Invitecodes.objects.get(eventid=arg1)
    return data.hashcode

@register.filter
def geteventname(arg1):
    data=Event.objects.get(eventid=arg1)
    return data.eventname