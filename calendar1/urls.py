from django.urls import path
from . import views

app_name = 'calendar1'

urlpatterns = [
    path('', views.calendar1_view, name='calendar1_name'),
]
