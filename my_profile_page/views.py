from django.shortcuts import render

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