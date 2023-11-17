from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def store(request):
    context = {}
    return render(request,'store/store.html')

def checkout(request):
    context = {}
    return render(request,'store/checkout.html')

def cart(request):
    context = {}
    return render(request,'store/cart.html')

