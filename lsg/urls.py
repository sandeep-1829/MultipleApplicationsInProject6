from django.urls import path

from lsg.views import *

app_name = 'IPL'

urlpatterns=[
    path('rahul/',rahul,name='rahul'),
    path('stonis/',stonis,name='stonis'),
]