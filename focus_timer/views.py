import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponse

def index(request):
    response = {}
    if 'isLogin' in request.session:
        hours = int(request.session['durasi_timer']) // 3600
        mins = (int(request.session['durasi_timer']) - hours * 60) // 60
        secs = (int(request.session['durasi_timer']) - mins * 60)
        response = {"hours": hours, "mins": mins, "secs": secs}
        if request.session['bahasa'] == 'id':
            return render(request, 'index.html', response)
        return render(request, 'index-en.html', response)
    return redirect('user/auth')

def edit(request):
    if 'isLogin' in request.session:
        if request.session['bahasa'] == 'id':
            return render(request, 'input.html')
        return render(request, 'input-en.html')
    return redirect('user/auth')

def update_session(request):
    if not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])
    headers = {"Authorization": "Bearer fdca0f928bbcc40b67191f73f381c15b9b30cb5a8befe6facb62c503d4d24af3e9c0d1df7a1e7f448c9a992bc7e44d9b905158a602fa68f75ffdd740bc09a9ba342012eb35dda37ea89bba1b28399929b679c28487542aa5f041fa1eb1a3ee323ed6e234ec9e637444426a2b72f0ae336bd1e9e76aa6753c1a97b549c564efdc"}
    data = {"data": {"durasiFocusTimer": int(request.POST.get('hour')) * 3600 + int(request.POST.get('minute')) * 60 + int(request.POST.get('second'))}}
    api_response = requests.put('https://strapi-production-ef0a.up.railway.app/api/calendar-users/' + str(request.session['uid']), json=data, headers=headers).json()
    request.session['durasi_timer'] = int(request.POST.get('hour')) * 3600 + int(request.POST.get('minute')) * 60 + int(request.POST.get('second'))
    return HttpResponse('ok')