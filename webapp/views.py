from urllib.robotparser import RequestRate
from django.shortcuts import render
from django.http import HttpResponse



def homePageView(request):
    context={}
    return render(request, 'webapp/home.html')

def aboutPageView(request):
    context={}
    return render(request, 'webapp/about.html')
