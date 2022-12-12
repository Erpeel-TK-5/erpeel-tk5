from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='focustimer'),
    path('edit', views.edit, name='edit'),
    path('session-update', views.update_session, name="updatesession")
]