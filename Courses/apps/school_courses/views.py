# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, 'school_courses/index.html', context)

def add(request):
    print "Form Received"
    if len(request.POST['name']) > 5 and len(request.POST['desc']) > 15:
        new_course = Course.objects.create(name = request.POST['name'])
        Description.objects.create(desc = request.POST['desc'], course = Course.objects.get(id = new_course.id))
        print "Course Added"
    if len(request.POST['name']) < 6:
        messages.error(request, "Course name must be longer than 5 characters.")
        print "Course name error"
    if len(request.POST['desc']) < 16:
        messages.error(request, "Course description must be longer than 15 characters.")
        print "Course description error"
    return redirect('/courses/')

def destroy(request, course_id):
    print "Course " + str(course_id) + " Deleted"
    context = {
        "course": Course.objects.get(id = course_id)
    }
    return render(request, 'school_courses/delete_conf.html', context)

def destroy_conf(request, course_id):
    print request.POST['confirm']
    if request.POST['confirm'] == 'confirm':
        Course.objects.get(id = course_id).delete()
        return redirect('/courses/')
    elif request.POST['confirm'] == 'cancel':
        return redirect('/courses/')