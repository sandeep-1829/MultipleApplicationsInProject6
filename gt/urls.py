from django.urls import path
from gt.views import *

app_name='IPL'

urlpatterns=[
    path('hardik/',hardik,name='hardik'),
    path('badoni/',badoni,name='badoni'),

]