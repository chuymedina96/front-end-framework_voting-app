from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib import messages
from .models import *

# Create your views here.
def index(request, *args, **kwargs):

    if 'react' not in request.session:
        request.session["react"] = 0
    if 'angular' not in request.session:
        request.session["angular"] = 0
    if 'vue' not in request.session:
        request.session["vue"] = 0
    if 'ember' not in request.session:
        request.session["ember"] = 0

    context ={
        'react'     : request.session["react"],
        'angular'   : request.session["angular"],
        'vue'       : request.session["vue"],
        'ember'     : request.session["ember"],
        'session'   : request.session,
    }

    return render(request, "base.html", context)

def vote(request):

    errors = Vote.objects.basic_validator(request.POST)

    if len(errors) > 0:
    
        request.session['email']        = request.POST['email']
        request.session['framework']    = request.POST['framework']
        
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')

    else:

        email                           = request.POST['email']
        framework                       = request.POST['framework']

        # checking for duplicate emails in database. If there is one, throw error

        if(Vote.objects.filter(email=email).exists()):
            messages.error(request, "Looks like an email like that has voted already, sorry!")
            return redirect("/")
        if("user_id" in request.session):
            messages.error(request, "You are still in a Browser Session. Nice Try. Clear your session by going to /logout route then try again.")
            return redirect("/")

        else: 
            
            if request.POST['framework'] == 'react':
                request.session["react"] += 1
    
            if request.POST['framework'] == 'angular':
                request.session["angular"] += 1
            
            if request.POST['framework'] == 'vue':
                request.session["vue"] += 1

            if request.POST['framework'] == 'ember':
                request.session["ember"] += 1

            Vote.objects.create(email=email, framework=framework)

            createdVote = Vote.objects.last()

            request.session['user_id']   = createdVote.id


            messages.success(request, "You have successfully voted. Thank you. Now please logout and let the next voter vote on the computer.")

            return redirect("/")


def logout(request):
    request.session.modified = True

    del request.session['user_id']

    messages.success(request, "Session has ended for that voter. Now the next voter can vote on the computer.")
    return redirect("/")