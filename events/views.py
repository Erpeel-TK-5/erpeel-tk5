import requests
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect

def create_event(request) :
    if "isLogin" in request.session:
        response = {}
        response['error'] = False
        form = EventForm(request.POST or None)
        response['form'] = form
        if(request.method == 'POST'):
            if(form.is_valid()) :
                title = request.POST['title']
                description = request.POST['description']
                start = request.POST['start']
                end = request.POST['end']
                headers = {"Authorization":