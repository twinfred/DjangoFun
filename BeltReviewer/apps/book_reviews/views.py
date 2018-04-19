# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Render Routes
def index(request):
    if 'logged' in request.session:
        if request.session['logged'] == True:
            return redirect('/books/')
        else:
            print "hello"
            context = {
                "user": User.objects.get(id=request.session['user_id'])
            }
            return render(request, 'book_reviews/index.html', context)
    if not 'logged' in request.session:
        print "what's up"
        return render(request, 'book_reviews/index.html')

def books(request):
    if not 'logged' in request.session:
        return redirect('/')
    else:
        if request.session['logged'] == True:
            context = {
                "user": User.objects.get(id=request.session['user_id']),
                "books": Book.objects.all()
            }
            return render(request, 'book_reviews/books.html', context)
        else:
            return redirect('/')

def add_book(request):
    if request.session['logged'] == True:
        context = {
            "books": Book.objects.all()
        }
        return render(request, 'book_reviews/add_book.html', context)
    else:
        return redirect('/')

def book_profile(request, book_id):
    if request.session['logged'] == True:
        book = Book.objects.get(id = book_id)
        return render(request, 'book_reviews/book_profile.html', book)
    else:
        return redirect('/')

def user_profile(request, user_id):
    if request.session['logged'] == True:
        user = User.objects.get(id = user_id)
        return render(request, 'book_reviews/user_profile.html', user)
    else:
        return redirect('/')

# POST Routes
def register(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session['user_id'] = new_user.id
        request.session['logged'] = True
        return redirect('/books/')

def login(request):
    # if request.method != 'POST':
    #     return redirect('/')
    errors = User.objects.login_validator(request.POST)
    print errors
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.filter(email = request.POST['email'])[0]
        request.session['user_id'] = user.id
        request.session['logged'] = True
        return redirect('/books/')

def add(request):
    if request.method != 'POST':
        return redirect('/')
    book_errors = Book.objects.basic_validator(request.POST)
    review_errors = Review.objects.basic_validator(request.POST)
    if book_errors or review_errors:
        for tag, error in book_errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        for tag, error in review_errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/books/')
    else:
        this_uploader = User.objects.get(id=request.session['user_id'])
        if request.POST['author_list'] != "None":
            new_book = Book.objects.create(title = request.POST['title'], author = request.POST['author_list'], uploader = this_uploader)
            Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], reviewer = this_uploader, of_book = new_book)
            messages.success(request, "Your book and review were added.")
            return redirect('/books/{}/'.format(new_book.id))
        else:
            new_book = Book.objects.create(title = request.POST['title'], author = request.POST['author'], uploader = this_uploader)
            Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], reviewer = this_uploader, of_book = new_book)
            messages.success(request, "Your book and review were added.")
            return redirect('/books/{}/'.format(new_book.id))

def add_review(request, book_id):
    if request.method != 'POST':
        return redirect('/')
    review_errors = Review.objects.basic_validator(request.POST)
    if review_errors:
        for tag, error in review_errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/books/{}/'.format(book_id))
    else:
        this_reviewer = User.objects.get(id=request.session['user_id'])
        this_book = Book.objects.get(id=book_id)
        Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], reviewer = this_reviewer, of_book = this_book)
        messages.success(request, "Your review was added.")
        return redirect('/books/{}/'.format(book_id))

def delete_review(request, review_id, user_id):
    if request.session['logged'] == False:
        return redirect('/')
    this_review = Review.objects.get(id=review_id)
    this_review.delete()
    messages.success(request, "Your review was deleted.")
    return redirect('/books/')

def logout(request):
    request.session['logged'] = False
    return redirect('/')

def clear_logged(request):
    request.session.clear()
    return redirect('/')