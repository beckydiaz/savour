from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt, requests
from bs4 import BeautifulSoup
import re


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
            new_ingredient = Ingredient.objects.create(name=ingredient)
        images = soup.find_all(class_="rec-photo")
        for image in images:
            recipe_photo_src = image.get('src')
        titles = soup.find_all(class_='recipe-summary__h1')
        for title in titles:
            title = title.get_text()
        new_recipe = Recipe.objects.create(title=title, image=recipe_photo_src, url=request.POST['url'])
        new_recipe.ingredients.add(new_ingredient)

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

# def clear_list(request):
#     # ingredient.all.delete()
#     return redirect('/savour/list')