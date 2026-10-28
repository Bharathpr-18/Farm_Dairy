from django.conf.locale import el
from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http
from .models import student


# Create your views here.
def index(request):
    if (request.method == "POST"):
        sobj = student()
        sobj.sid = request.POST['studid']
        sobj.sname = request.POST['studname']
        sobj.save()
        return HttpResponse("Sucessfully saved")
    else:
        return render(request,'landingpage.html')