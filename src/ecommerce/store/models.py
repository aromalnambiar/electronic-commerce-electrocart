from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#customer 

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


#product

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()    
    digital = models.BooleanField(default=False, null=True, blank=True)
    #image
    
    def __str__(self):
        return self.name
    
    

#Order

class Order(models.Model):
    order = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=False)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
    
    
#order item

class OrderItem(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=False)
    
    
    
#shiping address

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer ,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return self.address
    
    
    
    