from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EditForm

# Create your views here.
import requests
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect

def index(request):
    if "isLogin" in request.session:
        return render(request, 'input.html')
    else:
        return redirect('/user/auth')

def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditForm()

    return render(request, 'input.html', {'form': form})