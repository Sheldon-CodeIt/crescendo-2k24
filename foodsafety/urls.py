from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('report', views.report, name='report'),
    path('dash/', views.dash, name='dash'),
    path('products/', views.productsList, name='products'),
    # path('product/<int:pk>/', views.productDetails, name='product'),

    # path('product/<slug:product>/', views.lays, name='lays'),
    path('product/<slug:product>/', views.productDetails, name='productDetails'),

]