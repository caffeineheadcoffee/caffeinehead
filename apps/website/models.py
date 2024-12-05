from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import *


class Enquiry(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.full_name

class Submission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField()
    address = models.CharField(max_length=100)
    service = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name