from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.productsList, name='products'),
    path('product/<int:pk>/', views.productDetails, name='product'),
]