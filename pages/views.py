from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomePageView():
    return HttpResponse("Hello Ranga")
