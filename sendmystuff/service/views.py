from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def login(request):
    return render(request,'registration/login.html')

def clientReg(request):
    return render(request,'registration/client.html')

def transReg(request):
    return render(request,'registration/transporter.html')

def ownerReg(request):
    return render(request,'registration/owner.html')