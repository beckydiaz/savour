from __future__ import unicode_literals
from django.db import models
from random import random
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
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = IngredientManager()

    def random_price(self):
        return round(random() * 10, 2)

    def __repr__(self):
        return f"<Ingredient object: {self.name} ({self.id})>"

class Pantry(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Ingredient object: {self.name} ({self.id})>"

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=455)
    url = models.CharField(max_length=455)
    user = models.ForeignKey(User, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RecipeManager() 

