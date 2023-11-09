from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def login(request):
    if request.method == 'POST':
        us = request.POST['username']
        pw = request.POST['password']

        user = authenticate(request, username=us, password=pw)

        if user is not None:
            if check_password(pw, user.password):  # Use check_password to validate the password
                auth_login(request, user)
                return render(request, 'index.html')
            else:
                print("Password Incorrect!!")
                return render(request, 'login.html')
        else:
            print("User not found!!")
            return render(request, 'login.html')

    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return render(request, 'login.html')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

# def index(request):
#     return render(request, 'index.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required(login_url='login')  # Decorator to ensure the user is logged in
def index(request):
    current_username = request.user.username
    all_usernames = User.objects.values_list('username', flat=True)

    return render(request, 'index.html', {'current_username': current_username, 'all_usernames': all_usernames})
