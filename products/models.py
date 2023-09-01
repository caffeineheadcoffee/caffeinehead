import imp
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import *
from django.core import validators
# from djongo import models

User = get_user_model()

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='static/uploads', null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_name
    


class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_data = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    PAYMENT = (
        ('Cash on Delivery','Cash on Delivery'),
        ('Paypal','Paypal'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField(null=True)
    status = models.CharField(default='Pending', max_length=200)
    payment_method = models.CharField(max_length=200,choices=PAYMENT)
    payment_status = models.BooleanField(default=False,null=True,blank=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9),MaxLengthValidator(10)], max_length=10)
    address = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    
class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.FileField(upload_to='static/uploads')
    description = models.TextField()
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkdin = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Aboutus(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='static/uploads')
    description = models.TextField()
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)

class Imageslider(models.Model):
    image = models.FileField(upload_to='static/uploads')
