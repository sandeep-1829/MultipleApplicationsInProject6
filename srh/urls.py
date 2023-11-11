from srh.views import *

from django.urls import path

app_name = 'IPL'

urlpatterns=[
    path('bhuvi/',bhuvi,name='bhuvi'),
    path('nattu/',nattu,name='nattu'),

]