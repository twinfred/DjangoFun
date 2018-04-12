# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'rand_word/index.html')

def generate(request):
    print "Generate random word"
    request.session['count'] += 1
    request.session['word'] = get_random_string(length=14)
    return redirect('/random-word/')

def reset(request):
    print "Reset session count"
    del request.session['count']
    del request.session['word']
    return redirect('/random-word/')
    