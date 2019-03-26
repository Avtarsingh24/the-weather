from django.shortcuts import render
import requests
from .models import City,Continent
from .forms import CityForm
from django.views.generic import ListView



def index(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        print(city_weather)
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





class index2(ListView):
    model = Continent
    template_name = 'weather/index2.html'



class earthquake(ListView):
    model = Continent
    template_name = 'weather/earthquake.html'