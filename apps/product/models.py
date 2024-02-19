from django.contrib.auth import get_user_model
from django.db import models

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.validators import validate_image
from apps.product.utils import upload_product_image_to

User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(max_length=100)
    price = fields.AmountField()
    discounted_price = fields.AmountField(null=True, blank=True)
    stock = models.PositiveIntegerField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    @property
    def display_image(self):
        return self.productimage_set.filter(is_display_image=True).last()

    @property
    def product_price(self):
        return self.discounted_price if self.discounted_price else self.price


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    is_display_image = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to=upload_product_image_to,
        validators=[validate_image]
    )

    def __str__(self):
        return str(self.pk)


class Member(models.Model):
    ROLE = (
        ('Main', 'Main'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkdin = models.URLField(max_length=200)
    role = models.CharField(max_length=100, choices=ROLE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    description = models.TextField()
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)


class ImageSlider(models.Model):
    image = models.ImageField()


class Service(models.Model):
    service_name = models.CharField(max_length=200)

    def __str__(self):
        return self.service_name
