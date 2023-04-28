from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('store/', views.store, name="store"),
    path('register/', views.register, name="register"),
    path('signin/', views.signin, name="signin"),
    path('product/', views.product, name="product"),
    path('update_item/', views.updateItem, name="update-item"),
    path('process_order/', views.processOrder, name="process-order"),
    
]
