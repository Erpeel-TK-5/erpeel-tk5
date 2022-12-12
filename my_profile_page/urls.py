from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='myprofile'),
    path('edit', views.edit, name='edit'),
    path('session-update', views.update_session, name="updatesession")
]