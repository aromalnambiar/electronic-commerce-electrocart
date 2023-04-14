from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json


#home

def home(request):
    product = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0, 'shipping ' : False}    
    
    context = {'items' : items, 'order': order, 'product': product}
    return render(request, 'store/index.html', context)

#store

def store(request):
    product = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0, 'shipping ' : False}    
        
    context = {
        'products' : product,
        'items': items,
        'order': order,
    }
    return render(request, 'store/store.html', context)

#cart

def cart(request):
    #important     
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0, 'shipping ' : False}    
    
    context = {'items' : items, 'order': order}
    return render(request, 'store/cart.html', context)

#checkout

def checkout(request):
    #important     
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0, 'shipping ' : False}    
    
    context = {'items' : items, 'order': order}
    return render(request, 'store/checkout.html', context)

#register

def register(request):
    context = {}
    return render(request, 'store/register.html', context)

#signin

def signin(request):
    context = {}
    return render(request, 'store/signin.html', context)


#product

def product(request):
    context = {}
    return render(request, 'store/product.html', context)


#update item

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action :' , action)
    print('productId :' , productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    else:
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0 :
        orderItem.delete()
    
    return JsonResponse('item was added' , safe=False)