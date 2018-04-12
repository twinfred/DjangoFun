# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'survey_form/index.html')

def submit(request):
    print "Form submitted"
    if not 'survey_count' in request.session:
        request.session['survey_count'] = 1
    else:
        request.session['survey_count'] += 1
    request.session['name'] = request.POST['name']
    print request.session['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/survey/result/')

def result(request):
    return render(request, 'survey_form/result.html')