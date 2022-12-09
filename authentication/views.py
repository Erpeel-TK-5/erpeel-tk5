import requests
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect


def index(request):
    if "isLogin" in request.session:
        return redirect('/') #ganti sama url yg nampilin display kalo user ud login
    else:
        return render(request, 'auth.html')

def login(request):
    if "isLogin" in request.session:
        return redirect('/') #ganti sama url yg nampilin display kalo user ud login
    response={}
    response['error'] = False
    form = LoginForm(request.POST or None)
    response['form'] = form
    if(request.method == 'POST'):
        if(form.is_valid()) :
            username = request.POST['username']
            password = request.POST['password']
            headers = {"Authorization": "Bearer fdca0f928bbcc40b67191f73f381c15b9b30cb5a8befe6facb62c503d4d24af3e9c0d1df7a1e7f448c9a992bc7e44d9b905158a602fa68f75ffdd740bc09a9ba342012eb35dda37ea89bba1b28399929b679c28487542aa5f041fa1eb1a3ee323ed6e234ec9e637444426a2b72f0ae336bd1e9e76aa6753c1a97b549c564efdc"}
            api_response = requests.get('https://strapi-production-ef0a.up.railway.app/api/calendar-users?fields[0]=username&fields[1]=email&fields[2]=password', headers=headers).json()
            if api_response.get('error') != None:
                error_list = api_response.get('error').get('details').get('errors')
                error_messages = ""
                for error in error_list:
                    error_messages += error.get('message') + ", "
                messages.info(request, error_messages[:-2])
                return render(request, 'login.html', response)
            username_list = []
            email_list = []
            password_list = []
            id_list = []
            for user in api_response.get('data'):
                attrs = user.get('attributes')
                username_list.append(attrs.get('username'))
                email_list.append(attrs.get('email'))
                password_list.append(attrs.get('password'))
                id_list.append(user.get('id'))
            index = -1
            if username in username_list:
                index = username_list.index(username)
            elif username in email_list:
                index = email_list.index(username)
            else:
                messages.info(request, 'Username/email tidak ditemukan')
                return render(request, 'login.html', response)
            if index != -1 and password == password_list[index]:
                request.session['uid'] = id_list[index]
                request.session['isLogin'] = True
                return redirect('/') #ganti sama url yg nampilin display kalo user ud login
            else:
                messages.info(request, 'Password salah')
            return render(request, 'login.html', response)
        else:
            return render(request, 'login.html', response)
    else:
        form = LoginForm(request.POST or None)
        response['form'] = form
        return render(request,'login.html',response)

def logout(request):
    if "uid" in request.session:
        request.session.flush()
        return redirect('/')
    return redirect('/')

def register(request):
    if "isLogin" in request.session:
        return redirect('/') #ganti sama url yg nampilin display kalo user ud login
    response={}
    response['error'] = False
    form = RegisterForm(request.POST or None)
    response['form'] = form
    if(request.method == 'POST'):
        if(form.is_valid()) :
             username = request.POST['username']
             password = request.POST['password']
             email = request.POST['email']
             name = request.POST['name']
             headers = {"Authorization": "Bearer fdca0f928bbcc40b67191f73f381c15b9b30cb5a8befe6facb62c503d4d24af3e9c0d1df7a1e7f448c9a992bc7e44d9b905158a602fa68f75ffdd740bc09a9ba342012eb35dda37ea89bba1b28399929b679c28487542aa5f041fa1eb1a3ee323ed6e234ec9e637444426a2b72f0ae336bd1e9e76aa6753c1a97b549c564efdc"}
             data = {"data": {"username": username, "password": password, "email": email, "nama": name}}
             api_response = requests.post('https://strapi-production-ef0a.up.railway.app/api/calendar-users', json=data, headers=headers).json()
             if api_response.get('error') != None:
                error_list = api_response.get('error').get('details').get('errors')
                error_messages = ""
                for error in error_list:
                    error_messages += error.get('message') + ", "
                messages.info(request, error_messages[:-2])
                return render(request, 'register.html', response)
             request.session['uid'] = api_response.get('data').get('id')
             request.session['isLogin'] = True
             return redirect('/') #ganti sama url yg nampilin display kalo user ud login
        else:
            return render(request, 'register.html', response)
    else:
        form = RegisterForm(request.POST or None)
        response['form'] = form
        return render(request,'register.html',response)
