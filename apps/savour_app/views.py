from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt, requests
from bs4 import BeautifulSoup


def savour_dashboard(request):
    if not 'user_id' in request.session:
        messages.error(request, "Please log in!")
        return redirect ('/')
    context = {
    'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'savour_app/savour_dashboard.html', context)


def generate_lists(request):
    if request.method == "POST":
        response = requests.get(request.POST['url'])
        soup = BeautifulSoup(response.text, 'html.parser')
        recipes = soup.find_all(class_='recipe-ingred_txt added')
        for recipe in recipes:
            ingredient = recipe.get_text()
            Ingredient.objects.create(name=ingredient)
        for recipe in recipes:
    return redirect('/savour/dashboard')


def savour_recipes(request):
    return render(request, 'savour_app/savour_recipes.html')

def savour_favorites(request):
    return render(request, 'savour_app/savour_favorites.html')

def savour_list(request):
    context = {
        "ingredients": Ingredient.objects.exclude(name='1/2 teaspoon salt').exclude(name= '1/4 teaspoon salt').exclude(name='teaspoon salt')
        }
    return render(request, 'savour_app/savour_list.html', context)

def savour_pantry(request):
    return render(request, 'savour_app/savour_pantry.html')

def delete_ingredient(request, ingredient_id):
    this_ingredient = Ingredient.objects.get(id=ingredient_id)
    this_ingredient.delete()
    return redirect('/savour/list')