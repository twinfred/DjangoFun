# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Users Manager
class UserManager(models.Manager):
    # Login Validator
    def login_validation(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if len(user):
            user = User.objects.filter(email = postData['email'])[0]
        else:
            errors['email'] = "The email or password you entered was incorrect."
            return errors
        password = bcrypt.checkpw(postData['password'].encode(), user.password.encode())
        if password == False:
            errors['password'] = "The email or password you entered was incorrect."
        if errors:
            return errors
    # User Login
    def login_user(self, postData):
        user = User.objects.filter(email = postData['email'])[0]
        return user
    # Registration Validator
    def reg_validation(self, postData):
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
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Your email is not the correct format."
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long."
        if postData['password'] != postData['pass_conf']:
            errors['password'] = "Your passwords don't match."
        return errors
    # Create New Normal User
    def create_user(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
        return new_user
    # Create Admin User
    def create_admin(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        new_admin = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password, user_lever = 9)
        return new_admin
    # Admin: Delete User
    def delete_user(self, user_id):
        User.objects.get(id=user_id).delete()
        return "User deleted"
    # User: Validate & Edit User Info
    def edit_info_validation(self, postData):
        errors = {}
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
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Your email is not the correct format."
        return errors
    def edit_my_info(self, postData, user_id):
        edited_user = User.objects.get(id=user_id)
        edited_user.email = postData['email']
        edited_user.first_name = postData['first_name']
        edited_user.last_name = postData['last_name']
        edited_user.save()
        return "Your info was updated."
    # User: Validate & Edit User Password
    def edit_password_validation(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long."
        if postData['password'] != postData['pass_conf']:
            errors['password'] = "Your passwords don't match."
        return errors
    def edit_my_password(self, postData, user_id):
        edited_user = User.objects.get(id=user_id)
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        edited_user.password = password
        edited_user.save()
        return "Your password was updated."
    # Context Options
    def all_users(self, user_id):
        context = {
            "all_users": User.objects.all(),
            "this_user": User.objects.get(id=user_id),
        }
        return context
    def this_user(self, user_id):
        context = {
            "this_user": User.objects.get(id=user_id),
        }
        return context
    def profile_users(self, profile_id, user_id):
        context = {
            "all_users": User.objects.all(),
            "profile": User.objects.get(id=profile_id),
            "this_user": User.objects.get(id=user_id),
        }
        return context
    # Edit User Password

# Users DB Table
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()