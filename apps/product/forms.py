from django.forms import ModelForm, fields
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


class AboutusForm(ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"


class ImagesliderForm(ModelForm):
    class Meta:
        model = ImageSlider
        fields = "__all__"


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

