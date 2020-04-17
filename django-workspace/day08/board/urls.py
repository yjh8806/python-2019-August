from django.contrib import admin
from django.urls import path, include

# http://localhost:8000/board/
from . import views
urlpatterns = [
    path('', views.board, name='board'),    
]