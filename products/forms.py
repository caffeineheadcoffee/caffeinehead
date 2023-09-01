import imp
from django.forms import ModelForm,fields
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity','payment_method','contact_no','address']

class EditOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status','payment_status']

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


class AboutusForm(ModelForm):
    class Meta:
        model = Aboutus
        fields = "__all__"
    

class ImagesliderForm(ModelForm):
    class Meta:
        model = Imageslider
        fields = "__all__"

