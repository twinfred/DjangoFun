# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        today_year = int(datetime.today().year)
        today_month = int(datetime.today().month)
        today_day = int(datetime.today().day)
        if postData['first_name'] == "":
            errors['first_name'] = "A first name is required."
        elif len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name must be at least two characters long."
        elif postData['first_name'].isalpha() == False:
            errors['first_name'] = "Your first name must only contain letters."
        if postData['last_name'] == "":
            errors['last_name'] = "A last name is required."
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name must be at least two characters long."
        elif postData['last_name'].isalpha() == False:
            errors['last_name'] = "Your last name must only contain letters."
        if postData['email'] == "":
            errors['email'] = "An email is required."
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Your email is not the correct format."
        if int(postData['birthday_month']) == 0 or int(postData['birthday_day']) == 0 or int(postData['birthday_year']) == 0:
            errors['birthday'] = "A birthday is required."
        elif int(postData['birthday_year']) == today_year and int(postData['birthday_month']) > today_month:
            errors['birthday'] = "Your birthday must preceed today's date."
        elif int(postData['birthday_month']) == today_month and int(postData['birthday_day']) > today_day:
            errors['birthday'] = "Your birthday must preceed today's date."
        return errors        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Password(models.Model):
    pwd = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)