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
        user = User.objects.get(id = request.session['user_id'])
        response = requests.get(request.POST['url'])
        soup = BeautifulSoup(response.text, 'html.parser')
        units = ['ounce', 'ounces', 'teaspoon', 'teaspoons', 'tablespoon', 'tablespoons', 'cup', 'cups', 'pound', 'pounds', 'fluid ounce', 'fluid ounces']
        
        ingredients = []

        recipe = soup.find_all(class_='recipe-ingred_txt added')
        for ingredient in recipe:

            ingredients.append(ingredient.get_text())

        
        QUANTITY_REGEX = re.compile(r'\d*\/?\d+')

        output = []

        for ingredient in ingredients:
            ingredient = ingredient.split()
            print(ingredient)
            while QUANTITY_REGEX.match(ingredient[0]):
                ingredient.pop(0)

            if ingredient[0] in units:
                ingredient.pop(0)
            output.append(' '.join(ingredient))
        
        for i in range(0, len(output)):
            if len(Ingredient.objects.filter(name = output[i])) == 0:
                Ingredient.objects.create(name=output[i])
        
        images = soup.find_all(class_="rec-photo")
        for image in images:
            recipe_photo_src = image.get('src')
        
        titles = soup.find_all(class_='recipe-summary__h1')
        for title in titles:
            title = title.get_text()
            new_recipe = Recipe.objects.create(title=title, image=recipe_photo_src, url=request.POST['url'], user =user)
        ingredients_to_add = Ingredient.objects.all()
        new_recipe.ingredients.add(*ingredients_to_add)
    return redirect('/savour/dashboard')

def savour_recipes(request):
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        "recipe": Recipe.objects.last()
    }
    return render(request, 'savour_app/savour_recipes.html', context)

def savour_favorites(request):
    return render(request, 'savour_app/savour_favorites.html')

def savour_list(request):
    # if not "recipe" in request.session:
    #     request.session('recipe') = Recipe.objects.last()
    user_recipe = Recipe.objects.filter(user= User.objects.get(id= request.session['user_id'])).last()
    context = {
        'user_recipe': Recipe.objects.filter(user= User.objects.get(id= request.session['user_id'])).last(),
        'ingredients': Ingredient.objects.filter(recipes= user_recipe)
        }
    print('user_recipe'),
    return render(request, 'savour_app/savour_list.html', context)

def savour_pantry(request):
    return render(request, 'savour_app/savour_pantry.html')

def delete_ingredient(request, ingredient_id):
    this_ingredient = Ingredient.objects.get(id=ingredient_id)
    this_ingredient.delete()
    return redirect('/savour/list')

def clear_list(request):
    Ingredient.objects.all().delete()
    return redirect('/savour/list')