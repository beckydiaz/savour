from __future__ import unicode_literals
from django.db import models
from apps.login_app.models import *

class IngredientManager(models.Manager):
    def ingredient_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Ingredient name should be at least 3 characters"
        if len(postData['quantity']) <= 0:
            errors["quantity"] = "Quantity shouldn't be empty"
        return errors

class RecipeManager(models.Manager):
    def recipe_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["title"] = "Title should be at least 3 characters"
        if len(postData['description']) < 3:
            errors["description"] = "Description should be at least 3 characters"
        return errors

class Ingredient(models.Model):
    quantity=models.FloatField()
    measurement=models.CharField(max_length=45)
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = IngredientManager() 

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RecipeManager() 

