import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponse

def index(request):
    response = {}
    if 'isLogin' in request.session:
        firstName = request.session['firstName']
        lastName = request.session['lastName']
        age = int(request.session['age'])
        description = request.session['description']
        response = {"firstName": firstName, "lastName": lastName, "age": age, "description": description}
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
    data = {"data1": {"firstName": request.POST.get('firstName')}, "data2": {"lastName": request.POST.get('lastName')}, "data3": {"age": int(request.POST.get('age'))}, "data4": {"description": request.POST.get('description')}}
    
    api_response = requests.put('https://strapi-production-ef0a.up.railway.app/api/calendar-users/' + str(request.session['uid']), json=data, headers=headers).json()
    request.session['firstName'] = request.POST.get('firstName')
    request.session['lastName'] = request.POST.get('lastName')
    request.session['age'] = request.POST.get('age')
    request.session['description'] = request.POST.get('description')
    return HttpResponse('ok')