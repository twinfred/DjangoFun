# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import gmtime, strftime, localtime

# Create your views here.

def index(request):
    return render(request, 'session_words/index.html')

def add_session(request):
    # New word to add:
    new_word = {}
    if not 'word' in request.POST:
        return redirect('/session-words/')
    else:
        new_word['word'] = request.POST['word']
        if not 'color' in request.POST:
            new_word['color'] = "black"
        elif request.POST['color'] == "red":
            new_word['color'] = "red"
        elif request.POST['color'] == "green":
            new_word['color'] = "green"
        elif request.POST['color'] == "blue":
            new_word['color'] = "blue"
        if not 'big_fonts' in request.POST:
            new_word['font_size'] = "p"
        else:
            new_word['font_size'] = "h2"
        new_word['created_at'] = strftime("%I:%M:%S %p, %b %d, %Y", localtime())
        # Append new word to word list
        if not 'word_list' in request.session:
            request.session['word_list'] = []
            request.session['word_list'].append(new_word)
        else:
            word_list = request.session['word_list']
            word_list.append(new_word)
            request.session['word_list'] = word_list
        print "Session added."
        print "Word List:"
        print request.session['word_list']
        for x in request.session['word_list']:
            print x
        return redirect('/session-words/')

def clear_session(request):
    if 'word_list' in request.session:
        del request.session['word_list']
    if 'new_word' in request.session:
        del request.session['new_word']
    print "Session cleared."
    return redirect('/session-words/')