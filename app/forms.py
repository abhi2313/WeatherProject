from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateField
from dataclasses import fields
from django.views.generic import CreateView

from django.contrib.auth.models import User
from django.forms import TextInput
from django.utils import timezone


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class CityForm(forms.ModelForm):
#     class Meta:
#         model = Weather
#         fields = '__all__'


# class eventForm(forms.ModelForm):

#     class Meta:
#         model = events
#         fields = ['host', 'event_name', 'invited_user', 'date', 'time']
#         widgets = {
#             'date': DatePickerInput(),
#             'time': TimePickerInput(),
#             'invited_user': forms.SelectMultiple()

#         }
