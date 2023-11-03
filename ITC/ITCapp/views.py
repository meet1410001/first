from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def login(request):
    if request.method == 'POST':

        if request.POST['loginbtn']:

            print("Login!!")
            us = request.POST['user']
            pw = request.POST['pw']

            try:
                record = user.objects.get(username=us)
                dpw = record.password

                if pw == dpw:
                    return render(request, 'index.html')
                else:
                    print("Password Incorrect!!")
                    return render(request, 'login.html')

            except:
                print("User not found!!")
                return render(request, 'login.html')

        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def registration(request):

    if request.method == 'POST':

        if request.POST['register']:
            us = request.POST['user']
            pw = request.POST['pw']
            name = request.POST['name']
            email = request.POST['email']
            age = request.POST['age']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']

            new_user = user(username=us, password=pw, name=name, email=email, age=age, city=city, state=state, country=country)
            new_user.save()

            return render(request, 'login.html')

        else:
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')
