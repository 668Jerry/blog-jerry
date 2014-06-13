from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def home(request):
    s = "This is the Main Page."
    return HttpResponse(s)
def now(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    return HttpResponse(str(year) + "/" + str(month) + "/" + str(day))
def helloWorld(request):
    s = "Bad URL!!!"
    return HttpResponse(s)
