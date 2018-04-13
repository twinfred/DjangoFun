# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from time import gmtime, strftime, localtime

# Create your views here.

def index(request):
    if not 'gold_count' in request.session:
        request.session['gold_count'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def reset(request):
    if 'gold_count' in request.session:
        print "resetting gold count"
        del request.session['gold_count']
        request.session['activities'] = []
    return redirect('/')

def find_gold(request):
    print "searching the", request.POST['location']
    location_amt = {
        'farm': random.randrange(10,21),
        'cave': random.randrange(5,11),
        'house': random.randrange(2,6),
        'casino': random.randrange(-50,51),
    }
    result = {}
    result['created_at'] = strftime("%I:%M:%S %p, %b %d, %Y", localtime())
    result['winnings'] = location_amt[request.POST['location']]
    result['location'] = request.POST['location']
    if result['winnings'] < 0:
        result['outcome'] = 'red'
    else:
        result['outcome'] = 'green'
    activities = request.session['activities']
    activities.append(result)
    request.session['activities'] = activities
    print request.session['activities']
    request.session['gold_count'] += result['winnings']
    print request.session['gold_count']
    return redirect('/')