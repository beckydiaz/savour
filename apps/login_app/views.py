from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "login_app/login.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        return redirect('/savour/dashboard')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST['email'])
        except:
            messages.error(request, "Email or password is incorrect")
            return redirect('/')
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/savour/dashboard')
        else:
            messages.error(request, "Email or Password is incorrect.")
            return redirect ('/')
    return redirect('/savour/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')