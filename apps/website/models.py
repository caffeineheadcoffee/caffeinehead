from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Enquiry(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.full_name
