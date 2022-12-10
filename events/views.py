import requests
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect

def index(request):
    if "isLogin" in request.session:
        return render(request, 'events.html')
    else:
        return redirect('/user/auth')

def create_event(request) :
    if "isLogin" in request.session:
        response = {}
        response['error'] = False
        form = EventForm(request.POST or None)
        response['form'] = form
        if(request.method == 'POST'):
            if(form.is_valid()) :
                name = request.POST['name']
                start_date = request.POST['start_date']
                end_date = request.POST['end_date']
                is_public = True if request.POST['is_public']=="on" else False
                is_recurring = True if request.POST['is_recurring']=="on" else False
                notes = request.POST['notes']
                headers = {"Authorization": "Bearer fdca0f928bbcc40b67191f73f381c15b9b30cb5a8befe6facb62c503d4d24af3e9c0d1df7a1e7f448c9a992bc7e44d9b905158a602fa68f75ffdd740bc09a9ba342012eb35dda37ea89bba1b28399929b679c28487542aa5f041fa1eb1a3ee323ed6e234ec9e637444426a2b72f0ae336bd1e9e76aa6753c1a97b549c564efdc"}
                data = {"data":{'title': name, 'startDate': start_date, 'endDate': end_date, 'isPublic': is_public, 'isRecurring': is_recurring, 'notes': notes}}
                api_response = requests.post('https://strapi-production-ef0a.up.railway.app/api/events', json=data, headers=headers).json()

                if api_response.get('error') != None:
                    error_list = api_response.get('error').get('details').get('errors')
                    error_messages = ""
                    for error in error_list:
                        error_messages += error.get('message') + ", "
                    messages.info(request, error_messages[:-2])
                    return render(request, 'create_event.html', response)
                request.session['uid'] = api_response.get('data').get('id')
                messages.info(request, "Event created successfully")
                return redirect('/')
            else :
                messages.info(request, "Form is not valid")
                return render(request, 'create_event.html', response)
        else :
            form = EventForm(request.POST or None)
            response['form'] = form
            return render(request, 'create_event.html', response)

    return redirect('/user/auth')