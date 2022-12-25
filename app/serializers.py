from rest_framework import serializers
from .models import CityWeather, CityWeatherCrud


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeather
        fields = '__all__'


class WeatherCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeatherCrud
        fields = '__all__'
