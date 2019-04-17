from django.shortcuts import render
import requests
from .models import City,Continent,Earthquake_data,Temp_changes_couses
from .forms import CityForm
from django.views.generic import ListView

 

def index(request):
    cities = City.objects.all()[0:4] #return all the cities in the database
    citiesd = City.objects.all().latest('name') #return all the cities in the database
    print(citiesd)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=205ac0b11586197656f07adb5e533793'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
            }

        weather_data.append(weather) 
    
    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context) 




class Continent_list(ListView):
    model = Continent
    template_name = 'weather/weather.html'



def index1(request):
    qs1 = Temp_changes_couses.objects.all()
    qs2 = Earthquake_data.objects.all()
    context = {
        'qs1':qs1,
        'qs2':qs2
    }
    return render (request, 'weather/index2.html', context)