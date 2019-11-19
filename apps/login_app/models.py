from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(data['first_name']) <= 1:
            errors["first_name"] = "First name should be at least 2 characters."
        if len(data['last_name']) <= 1:
            errors["last_name"] = "Last name should be at least 2 characters."   
        if len(data['email']) <= 7:
            errors["email"] = "Email should be at least 8 characters."
        if not EMAIL_REGEX.match(data['email']):              
            errors['email'] = ("Invalid email address!")
        if len(User.objects.filter(email = data['email'])) != 0:
            errors['email_invalid'] = "Email is already in use."
        if data['password'] != data['confirm_password']:
            errors['password_match'] = "Passwords do not match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    


