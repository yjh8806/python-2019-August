# myapp1/urls.py (만든파일)

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index')
]
