from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def home(request):
    s = "Hello World!"
    return HttpResponse(s)
def now(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    return HttpResponse(str(year) + "/" + str(month) + "/" + str(day))