from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='public_event'),
    path('<str:nama>/', views.user_public_event, name="user_public_event")
]