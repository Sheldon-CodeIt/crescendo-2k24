from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'foodsafety/home.html')


def productsList(request):
    return render(request, 'foodsafety/product_list.html')


def productDetails(request, pk):
    return render(request, 'foodsafety/product.html')
