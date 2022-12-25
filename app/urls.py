from django.urls import path, include
from .views import login, signup, home, logout, crud

urlpatterns = [
    path('', home.index, name='homepage'),
    path('signup/', signup.Signup.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', logout.logout),
    path('api/weather/', crud.WeatherApi.as_view())
]
