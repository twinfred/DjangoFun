# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Validatons
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors['last_name'] = "Your email already exists within our system. Please log in."
            return errors
        if len(postData['first_name']) < 1:
            errors['first_name'] = "A first name is required."
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name is too short."
        if len(postData['last_name']) < 1:
            errors['last_name'] = "A last name is required."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name is too short."
        if not NAME_REGEX.match(postData['first_name']) or not NAME_REGEX.match(postData['last_name']):
            errors['email'] = "Your name can only contain alphabetic characters."
        if len(postData['email']) < 1:
            errors['last_name'] = "Your last name is too short."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Your email is not the correct format."
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long."
        if postData['password'] != postData['pass_conf']:
            errors['password'] = "Your passwords don't match."
        return errors
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if len(user):
            user = User.objects.filter(email = postData['email'])[0]
        else:
            errors['email'] = "The email you entered is not registered."
            return errors
        password = bcrypt.checkpw(postData['password'].encode(), user.password.encode())
        if password == False:
            errors['password'] = "The password you entered was incorrect."
        if errors:
            return errors

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "A book title is required."
        if len(postData['title']) < 2:
            errors['title'] = "Your book title is too short."
        if len(postData['author']) < 1 and postData['author_list'] == "None":
            errors['author'] = "An author is required."
        if len(postData['author']) < 2 and postData['author_list'] == "None":
            errors['author'] = "The author name you entered is too short."
        if len(postData['author']) > 1 and postData['author_list'] != "None":
            errors['author'] = "You cannot choose an author from the list and add a new author at the same time."
        return errors

class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['review']) < 1:
            errors['review'] = "A review is required."
        if len(postData['review']) < 10:
            errors['review'] = "Your review is too short."
        if postData['rating'] == "None":
            errors['rating'] = "A rating is required."

# Database Tables
class User(models.Model):
    first_name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=42)
    email = models.CharField(max_length=84)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Validation
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="books_uploaded")
    #Validation
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User, related_name="reviews")
    of_book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    #Validation
    objects = ReviewManager()