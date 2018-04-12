# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = 'Placeholder to later display all the blogs.'
    return HttpResponse(response)

def new(request):
    response = 'Placeholder to display a new form to create a new blog.'
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blog_number):
    response = 'Placeholder to display blog {}.'.format(blog_number)
    return HttpResponse(response)

def edit(request, blog_number):
    response = 'Placeholder to edit blog {}.'.format(blog_number)
    return HttpResponse(response)

def destroy(request, blog_number):
    return redirect('/')