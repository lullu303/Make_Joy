from django.contrib import admin
from django.urls import path, include

from index.views import base_views
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('todo/', include('todo.urls')),
    path('memo/', include('memo.urls')),
    path('weather/', include('weather.urls')),
    path('calendar1/', include('calendar1.urls')),

    

]
