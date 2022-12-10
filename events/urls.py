from django.urls import path

from . import views

urlpatterns = [
    path('create-event', views.create_event, name='create-event'),
    path('', views.index, name='events'),
    path('all-events', views.read_all_events, name='all-events'),
]