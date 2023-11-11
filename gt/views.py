from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hardik(request):
    return render(request,'hardik.html')

def badoni(request):
    return HttpResponse('<h1>***...Best Emerging player in 2023...*** IPL</h1>')
