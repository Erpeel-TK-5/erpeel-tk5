from django.shortcuts import render

def index(request):
    return render(request, 'public_event.html')

def user_public_event(request, nama):
    return render(request, "user_public_event.html", {"nama":nama})