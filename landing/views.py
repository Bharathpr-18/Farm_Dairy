from django.conf.locale import el
from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http
from .models import student


# Create your views here.
def index(request):
    return render(request,'landingpage.html')