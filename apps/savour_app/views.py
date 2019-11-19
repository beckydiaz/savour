from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


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
            ingredient.objects.create(name='ingredient')
        context: {
            ingredient: Ingredient.objects.all()
        }
        return redirect('savour/list', context)


def savour_recipes(request):
    return render(request, 'savour_app/savour_recipes.html')

def savour_favorites(request):
    return render(request, 'savour_app/savour_favorites.html')

def savour_list(request):
    return render(request, 'savour_app/savour_list.html')

def savour_pantry(request):
    return render(request, 'savour_app/savour_pantry.html')