from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import timer
import time
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "index.html") 

def detection(request):
    return render(request, "detection.html")

def static(request):
    return render(request, "static.html")

def settings(request):
    return render(request, "settings.html")
