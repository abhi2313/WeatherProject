from django.contrib import admin

# Register your models here.
from .models import CityWeather, CityWeatherCrud

admin.site.register(CityWeather)
admin.site.register(CityWeatherCrud)
