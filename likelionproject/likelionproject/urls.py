"""
Urls.py
특정 url에 GET요청을 받았을 때
어떤 함수를 실행할지 정의하는 공간
"""
from django.contrib import admin
from django.urls import path

# 여기부터 import하는 것
from quizapp.views import get_home
from quizapp.views import check_answer
# 만약 여기서 
# import quizapp.views라고 작성했다면
# 아래에서는
# path('', views.get_home) 이런 식으로 써야 함
# 모듈이 커질수록 위와 같이 작성해야 함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home),
    path('result/', check_answer)
]
