from django.db import models

# Create your models here.


class CityWeather(models.Model):
    city = models.CharField(max_length=20)
    temp = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    visibility = models.IntegerField()
    wind_speed = models.IntegerField()
class CityWeatherCrud(models.Model):
    city = models.CharField(max_length=20)
    temp = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    visibility = models.IntegerField()
    wind_speed = models.IntegerField()
