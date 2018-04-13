# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'ecommerce/index.html')

def add_to_cart(request):
    product_prices = {
        '001': 19.99,
        '002': 29.99,
        '003': 4.99,
        '004': 49.99,
    }
    charge_amt = product_prices[request.POST['product_id']] * int(request.POST['quantity'])
    request.session['charge_amt'] = charge_amt
    if not 'purchase_count' in request.session:
        request.session['purchase_count'] = 1 * int(request.POST['quantity'])
        request.session['total_spent'] = charge_amt
    else:
        request.session['purchase_count'] += 1 * int(request.POST['quantity'])
        request.session['total_spent'] += charge_amt
    
    print request.POST['product_id']
    print product_prices[request.POST['product_id']]
    print request.session['charge_amt']
    return redirect('/store/checkout/')

def checkout(request):
    return render(request, 'ecommerce/checkout.html')