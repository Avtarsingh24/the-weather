from django.shortcuts import render
import requests
from .models import City,Temp_imp_climate,Earthquake_data,Temp_changes_couses,Feedback,City1
from .forms import CityForm,CForm
from django.views.generic import ListView
import datetime

def index(request):
    cities = City.objects.all()[0:5] #return all the cities in the database
    
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



def indexc(request):

    #appid="a0d5659a015c8b72076e37f18fb9b18b";
    cities = City1.objects.all() #return all the cities in the database
    print("cities>>>",cities)
    dt = datetime.datetime.now()
    print (dt)
    weather_data1 = []
    if request.method=="POST":
            form = CityForm(request.POST) # add actual request data to form for processing
            form.save() # will validate and save if validate

            if form.is_valid():
                city=form.cleaned_data.get('name')
                url="http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=a0d5659a015c8b72076e37f18fb9b18b"
                response=requests.get(url.format(city))
                json_response=response.json()
                if response.status_code==200 and json_response['list']:
                        # response=response.json();
                        # if response['list']:
                        # response=response.json();

                            name=json_response['list'][0]['name']
                            temp=json_response['list'][0]['main']['temp']
                            des=json_response['list'][0]['weather'][0]['description']
                            icon=json_response['list'][0]['weather'][0]['icon']
                            wind=json_response['list'][0]['wind']['speed']
                            country=json_response['list'][0]['sys']['country']
                            rain=json_response['list'][0]['rain']
                            snow=json_response['list'][0]['snow']
                            weather={
                                "city":name,"temp":temp,
                                "des":des,"icon":icon,"wind":wind,"country":country,"rain":rain,"snow":snow
                            }
                            
                            weather_data1=weather
                            return render(request,"weather/index.html",{"weather":weather,"form":form,"valid":True})
                        # else:
                        #     return render(request,"index.html",{"valid":False,"touser":"Please Be Sure Of City Name And Spelling","form":form})
                else:
                        return render(request,"weather/index.html",{"valid":False,"touser":"Please Be Sure Of City Name And Spelling..","form":form})
                
    
    form = CForm()
    return render(request,"weather/index.html",{"form":form})


















class Temp_imp_climate(ListView):
    model = Temp_imp_climate
    template_name = 'weather/index2.html'





def index1(request):
    qs1 = Temp_changes_couses.objects.all()
    qs2 = Earthquake_data.objects.all()
    context = {
        'qs1':qs1,
        'qs2':qs2
    }
    return render (request, 'weather/index2.html', context)




def FeedBack(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('msg'):
                post=Feedback()
                post.name= request.POST.get('name')
                post.email= request.POST.get('email')
                post.msg= request.POST.get('msg')
                post.save()
                return render(request, 'weather/FeedBack.html')  

        else:
                return render(request,'weather/FeedBack.html')


def admin_login(request):
    return render(request,'weather/admin_login.html')
