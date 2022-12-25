from app.serializers import WeatherCrudSerializer
from rest_framework.views import APIView
from app.models import CityWeatherCrud
from rest_framework.response import Response
from rest_framework import status
import requests
from django.http import HttpResponse


class WeatherApi(APIView):

    def get(self, request):
        try:
            weather = CityWeatherCrud.objects.all()
            serializer = WeatherCrudSerializer(weather, many=True)
            return Response({
                'data': serializer.data,
                'message': 'Weather fetched successfully'
            }, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({
                'data': {},
                'message': 'something went wrong ! '
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(Self, request):
        try:
            CityWeatherCrud.objects.all().delete()
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
                serializer = WeatherCrudSerializer(data=data)
                if(serializer.is_valid()):

                    serializer.save()

                else:
                    return Response({
                        'data': {},
                        'message': 'something went wrong ! '
                    }, status=status.HTTP_400_BAD_REQUEST)
            return Response({

                'message': 'Weather posted successfully !'}, status=status.HTTP_201_CREATED)

        except:
            return Response({
                'data': {},
                'message': 'something went wrong ! '
            }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:

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
                weather = CityWeatherCrud.objects.filter(city=city_name)
                serializer = WeatherCrudSerializer(
                    weather[0], data=data, partial=True)
                if(serializer.is_valid()):

                    serializer.save()

                else:
                    return Response({
                        'data': {},
                        'message': 'something went wrong ! '
                    }, status=status.HTTP_400_BAD_REQUEST)
            return Response({

                'message': 'Weather updated  successfully !'}, status=status.HTTP_201_CREATED)

        except:
            return Response({
                'data': {},
                'message': 'something went wrong ! '
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CityWeatherCrud.objects.all().delete()
        return Response({
            'data': {},
            'message': 'Weather deleted successfully .'
        }, status=status.HTTP_200_OK)
