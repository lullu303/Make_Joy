from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.memo_view, name='memo_name'),
]
