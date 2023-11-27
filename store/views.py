from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else : 
        items = []
        order = {'get_cart_items':0,'order.get_cart_total':0,'shipping':False}
    product = Product.objects.all()
    context = {'obj':product,'order':order}
    return render(request,'store/store.html',context)

def main(request):
    order = Order.objects.all()
    context = {'order':order}
    return render(request,'store/main.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else : 
        items = []
        order = {'get_cart_items':0,'order.get_cart_total':0,'shipping':False}

    context = {'items':items,'order':order}
    return render(request , 'store/cart.html',context)




def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order ,created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0,'shipping':False}

    context = {'items':items,'order':order}
    return render(request,'store/checkout.html',context)


def update_cart(request):
   
   data = json.loads(request.body)
   productId = data['productId']
   action = data['action']

   print('action: ',action)
   print('productId : ',productId)

   customer = request.user.customer
   product = Product.objects.get(id=productId)
   order , created = Order.objects.get_or_create(customer=customer,complete=False)

   orderItem , created = OrderItem.objects.get_or_create(order=order,product=product)

   if action=='add':
        orderItem.quantity = (orderItem.quantity+1)
   elif action=='remove':
        orderItem.quantity = (orderItem.quantity-1)
        

   orderItem.save()
   
   if orderItem.quantity <= 0:
       orderItem.delete()

   return JsonResponse("item is added ", safe=False)





   
