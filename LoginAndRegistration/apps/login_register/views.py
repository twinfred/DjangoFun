# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'login_register/index.html')

def success(request):
    if 'user_id' in request.session:
        print request.session['user_id']
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'login_register/success.html', context)
    else:
        messages.error(request, "You must be logged in.")
        return redirect('/')

def register_account(request):
    if len(request.POST['password']) < 8:
        messages.error(request, "Your password must be at least 8 characters long.")
        return redirect('/')
    elif request.POST['password'] != request.POST['pass_conf']:
        messages.error(request, "Your passwords don't match.")
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        birthday = str(request.POST['birthday_year']) + "-" + str(request.POST['birthday_month']) + "-" + str(request.POST['birthday_day'])
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, birthday = birthday)
        Password.objects.create(pwd = password, user = User.objects.get(id = new_user.id))
        request.session['user_id'] = new_user.id
    return redirect ('/success/')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    print user
    if not len(user):
        messages.error(request, "Your email is incorrect.")
        return redirect('/')
    else:
        user = User.objects.filter(email = request.POST['email'])[0]
        password = bcrypt.checkpw(request.POST['password'].encode(), user.password.pwd.encode())
        if password == True:
            request.session['user_id'] = user.id
            return redirect('/success/')
        else:
            messages.error(request, "Your password is incorrect.")
            return redirect('/')