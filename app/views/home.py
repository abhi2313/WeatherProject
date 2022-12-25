from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.serializers import WeatherSerializer
from django.views import View
from rest_framework import status
import requests
from rest_framework.response import Response
from app.models import CityWeather
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    CityWeather.objects.all().delete()
    API_KEY = '4da85e50a9e8c8b0e38766bcdb4de4da'
    cities = ["Delhi", "Mumbai", "Kolkata", "Bangalore", "Hyderabad"]
    for city_name in cities:

        
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}'
        list_of_data = requests.get(url.format(city_name)).json()

        data = {
            "city": city_name,
            "temp": int(list_of_data['main']['temp']),
            "pressure": list_of_data['main']['pressure'],
            "humidity": list_of_data['main']['humidity'],
            "visibility": list_of_data['visibility'],
            "wind_speed": int(list_of_data['wind']['speed']),

        }
        serializer = WeatherSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
        else:
            print(serializer.errors)
            return HttpResponse("not valid")
    data = CityWeather.objects.all()

    return render(request, 'show_weather.html', {'data': data})
