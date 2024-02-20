from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.AuthHome, name='authHome'),
    path('login/', views.AuthHome, name='authHome'),
    path('logout/', views.AuthHome, name='authHome'),
]