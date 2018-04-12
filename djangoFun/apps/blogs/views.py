# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = 'Placeholder to later display all the blogs.'
    return render(request, 'blogs/index.html')

def new(request):
    response = 'Placeholder to display a new form to create a new blog.'
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
    request.session['name'] = request.POST['name']
    print request.POST['name']
    print request.POST['description']
    return redirect('/')

def show(request, blog_id):
    response = 'Placeholder to display blog {}.'.format(blog_id)
    return HttpResponse(response)

def edit(request, blog_id):
    response = 'Placeholder to edit blog {}.'.format(blog_id)
    return HttpResponse(response)

def destroy(request, blog_id):
    return redirect('/')