from django.urls import path

from . import views

urlpatterns = [
    path('auth', views.index, name='auth'),
    path('login', views.login, name='login'),
    path('signup', views.register, name='signup'),
]