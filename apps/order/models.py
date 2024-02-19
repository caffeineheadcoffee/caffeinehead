from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

from apps.core import fields
from apps.core.models import BaseModel
from apps.product.models import Product

User = get_user_model()


class Order(BaseModel):
    STATUS_CHOICES = (
        ('initiated', 'Initiated'),
        ('invoiced', 'Invoiced'),
        ('shipped', 'Shipped'),
        ('delivered', 'delivered'),
        ('cancelled', 'Cancelled'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        choices=STATUS_CHOICES,
        default='initiated',
        db_index=True,
        max_length=10
    )
    shipping_amount = fields.AmountField(default=Decimal(0.0))
    discount_amount = fields.AmountField(default=Decimal(0.0))
    sub_total = fields.AmountField(default=Decimal(0.0))
    total = fields.AmountField(default=Decimal(0.0))
    contact_number = models.CharField(max_length=14)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.total = self.sub_total - self.discount_amount + self.shipping_amount
        return super(Order, self).save(*args, **kwargs)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    per_price = fields.AmountField(null=True, blank=True)
    amount = fields.AmountField(null=True, blank=True)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.per_price = self.product.product_price
        self.amount = self.per_price * self.quantity
        return super(OrderItem, self).save(*args, **kwargs)


class ShippingAddress(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=14)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname
