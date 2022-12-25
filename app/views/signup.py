
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from app.forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.contrib import messages


class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        form = UserRegistrationForm()
        message = None
        context = {'form': form, 'message': message}
        return render(request, 'signup.html', context)

    def post(self, request):
        print("here ")
        if request.user.is_authenticated:
            return redirect('homepage')
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('homepage')

        else:
            # expalnation = form.errors.as_data()
            # for key in expalnation:
            #     for value in expalnation[key]:
            #         message = value
            #         if message is not None:
            #             break
            form = UserRegistrationForm()
            context = {'form': form}
            return render(request, 'signup.html', context)
