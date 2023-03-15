from django.urls import path

from .views import base_views

app_name = 'index'

urlpatterns = [
    path('', base_views.index, name='index'),
]

