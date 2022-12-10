from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    try:
        return render(request, "index.html", {"id":request.session['uid']})
    except:
        return redirect("/user/login")