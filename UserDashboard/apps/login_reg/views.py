# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages

# User-facing pages
def login(request):
    if 'user_id' in request.session:
        return redirect('/dashboard/')
    else:
        return render(request, 'login_reg/login.html')

def registration(request):
    if 'user_id' in request.session:
        return redirect('/dashboard/')
    else:
        return render(request, 'login_reg/registration.html')

def logout(request):
    return render(request, 'login_reg/logout.html')

# Post requests
def user_reg(request):
    print "registering new user"
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.reg_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/registration')
    else:
        new_user = User.objects.create_user(request.POST)
        if not 'user_id' in request.session:
            request.session['user_id'] = new_user.id
        print "new user registered"
        return redirect('/dashboard/')

def user_login(request):
    print "logging in"
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.login_validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.login_user(request.POST)
        request.session['user_id'] = user.id
        print "logged in"
        return redirect('/dashboard/')

# Get requests
def logout_user(request):
    print "logging out"
    del request.session['user_id']
    print "logged out"
    return redirect('/logout/')