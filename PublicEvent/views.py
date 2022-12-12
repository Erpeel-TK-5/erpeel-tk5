from django.shortcuts import render
from django.utils.translation import get_language

def index(request):
    if ('isLogin' in request.session and request.session['bahasa'] == 'id') or get_language() == 'id':
        return render(request, 'public_event.html')
    return render(request, 'public_event-en.html')

def user_public_event(request, nama):
    if ('isLogin' in request.session and request.session['bahasa'] == 'id') or get_language() == 'id':
        return render(request, 'user_public_event.html', {"nama":nama})
    return render(request, "user_public_event-en.html", {"nama":nama})