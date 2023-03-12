from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_view, name='todo_name'),
]
