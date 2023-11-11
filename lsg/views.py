from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def rahul(request):
    return render(request,'rahul.html')


def stonis(request):
    return HttpResponse('<h1>***Powerfull Hitter For LSG...***')
