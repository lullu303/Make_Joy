from django.conf.urls import url
from . import views  # . 은 '현재 디렉토리 내에서' 라는 의미

urlpatterns = [
    url(r"^$", views.index, name="index")  # url은 그대로, views.py에 있는 index라는 함수를 실행해라
]
