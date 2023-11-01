from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def login(request):
    if(request.method=='POST'):
        if(request.POST['loginbtn']):
            print("Login!!")
            us = request.POST['user']
            pw = request.POST['pw']

            try:
                record = User.objects.get(username=us)
                dbpw = record.password

                if(pw==dbpw):
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
    if(request.method=='POST'):
        if (request.POST ['register']):
            us = request.POST['user']
            pw = request.POST['pw']
            name = request.POST['name']
            email = request.POST['email']
            age = request.POST['age']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']

            newuser = User(username=us, password=pw, name=name, email=email, age=age, city=city, state=state, country=country)
            newuser.save()

            return render (request, 'login.html')
        
        else:
            return render (request, 'register.html')
        
    else:
            return render (request, 'register.html')