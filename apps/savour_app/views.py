from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def savour_dashboard(request):
    if not 'user_id' in request.session:
        messages.error(request, "Please log in!")
        return redirect ('/')
#     context = {
#     'user': User.objects.get(id = request.session['user_id'])
#    }
    return render(request, 'savour_app/savour_dashboard.html')

# Create your views here.
