# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *
from ..login_reg.models import *
from django.contrib import messages

# User-facing pages
def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        context = User.objects.all_users(request.session['user_id'])
        return render(request, 'dashboard/index.html', context)
        
def user_profile(request, profile_id):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        context = User.objects.profile_users(profile_id, request.session['user_id'])
        return render(request, 'dashboard/user_profile.html', context)
        
def edit_user(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        context = User.objects.this_user(request.session['user_id'])
        return render(request, 'dashboard/edit_user.html', context)
# Admin: User-facing pages
def add_user(request):
    if not 'user_id' in request.session:
        return redirect('/')
    elif User.objects.get(id=request.session['user_id']).user_level != 9:
        return redirect('/')
    else:
        return render(request, 'dashboard/add_user.html')

# Admin: Post requests
def delete_user(request, user_id):
    if not 'user_id' in request.session:
        return redirect('/')
    elif User.objects.get(id=request.session['user_id']).user_level != 9:
        return redirect('/')
    else:
        delete_me = User.objects.delete_user(user_id)
        print delete_me
        return redirect('/')

# Post requests
def edit_my_info(request):
    if not 'user_id' in request.session:
        print "not logged in"
        return redirect('/')
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.edit_info_validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/dashboard/user/edit')
    else: 
        update_me = User.objects.edit_my_info(request.POST, request.session['user_id'])
        messages.success(request, update_me)
        return redirect('/dashboard/user/edit')   

def edit_my_password(request):
    if not 'user_id' in request.session:
        print "not logged in"
        return redirect('/')
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.edit_password_validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/dashboard/user/edit')
    else:
        update_me = User.objects.edit_my_password(request.POST, request.session['user_id'])
        messages.success(request, update_me)
        return redirect('/dashboard/user/edit')

# Get requests