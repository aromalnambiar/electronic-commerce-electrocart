from django.shortcuts import render
from .models import *



#home

def home(request):
    product = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}    
    
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
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}    
        
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
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}    
    
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
        order = {'get_cart_total' : 0, 'get_cart_items' : 0}    
    
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
