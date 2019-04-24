from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('FeedBack/',FeedBack, name ='FeedBack'),
    path('index2/',index1 ,name ='index2'),
    path('admin_login/',admin_login, name ='admin'),
    ]