from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('continent/',Continent_list.as_view(), name ='Continentlist'),
    path('index2/',index2.as_view(), name ='index2'),
    path('earthquake/',earthquake.as_view(), name ='earthquake'),
]