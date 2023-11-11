from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def bhuvi(request):
    return render(request,'bhuvi.html')

def nattu(request):
    return HttpResponse('<h1>***...Best Left Hand Bowler for Indian Team...***</h1>')