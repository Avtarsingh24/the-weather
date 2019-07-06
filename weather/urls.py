from django.urls import path,include
from . import views
from . views import *
from django.views.generic import TemplateView

urlpatterns = [
    
    path('', indexc, name = 'home'),
    path('FeedBack/',FeedBack, name ='FeedBack'),
    path('climate/',climate,name ='Climate'),
    path('major_earthquakes/',major_earthquakes,name='major_earthquakes'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]