from django.shortcuts import render
import requests
import json
from .models import City
from .forms import Cityform


def weather(request):
    if request.method=="POST":
        form=Cityform(request.POST)
        form.save()
        
    form=Cityform()
    cities=City.objects.all()
    weather_data = []
    for city in cities:
        print(city)
        api_key="e859b26ce54db305e980244ab4012174"
        
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        
        data=requests.get(url).json()
        
        #if data['cod']=="200":
        cityname=data['name']
        temp=data['main']['temp']
        desc=data["weather"][0]['main']
        icon=data ["weather"][0]['icon']
        context={"city":cityname,
                 "temperature":temp,
                 "description":desc,
                 "icon":icon,
                 'i':city.id}
        weather_data.append(context)
    x={'weather_data':weather_data,"form":form}
    return render(request,"weather.html",x)

def removecity(request,pk):
    c=City.objects.get(pk=pk)
    c.delete()
    cities=City.objects.all()
    weather_data = []
    for city in cities:
        print(city)
        api_key="e859b26ce54db305e980244ab4012174"
        
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        
        data=requests.get(url).json()
        
        #if data['cod']=="200":
        cityname=data['name']
        temp=data['main']['temp']
        desc=data["weather"][0]['main']
        icon=data ["weather"][0]['icon']
        context={"city":cityname,
                 "temperature":temp,
                 "description":desc,
                 "icon":icon,
                 'i':city.id}
        weather_data.append(context)
    x={'weather_data':weather_data}
    return render(request,"weather.html",x)
    
    
