from django.shortcuts import render

def index(request):
    if "isLogin" in request.session and request.session['bahasa'] == 'id':
        return render(request, 'home.html')
    else:
        return render(request, 'home-en.html')