from django.shortcuts import render
from store.models import *

# Create your views here.

def store(request):
    product = Product.objects.all()
    context = {'obj':product}
    return render(request,'store/store.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html')

def cart(request):
    context = {}
    return render(request,'store/cart.html')

