from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'store/index.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def register(request):
    context = {}
    return render(request, 'store/register.html', context)

def signin(request):
    context = {}
    return render(request, 'store/signin.html', context)


def product(request):
    context = {}
    return render(request, 'store/product.html', context)
