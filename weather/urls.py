from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('continent/',Continent_list.as_view(), name ='Continentlist'),
    path('index2/',index1 ,name ='index2'),
    ]