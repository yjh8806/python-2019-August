from django.contrib import admin
from django.urls import path, include

from . import views

# 서브앱의 urls.py는 서브앱의 views.py에게 연결시켜준다

urlpatterns = [
    path('', views.index, name='index'),
    path('ex01/', views.ex01, name='ex01'),             # 함수 뷰
    path('ex02/', views.Ex02.as_view(), name='ex02'),   # 클래스 뷰
    path('ex03/', views.Ex03.as_view(), name='ex03'),
]
