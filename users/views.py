from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from products.models import *
from .filters import *

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hurray! You are now registered user.')
    else:
        form = RegistrationForm()
    context = {
        "registration_form": form,
    }
    return render(request, "users/register.html", context)

def login_user(request):
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])
            
            if user is  not None:
                login(request,user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR, 'Please provide correct credentails ')
                return render(request,'users/login.html',{
                    'forms':form
                })

    form = AccountAuthenticationForm
    context = {
        'form': form
    }
    return render(request,'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/login')

def homepage(request):
    products = Product.objects.all().order_by('-id')[:9]
    coverimage = Imageslider.objects.all()
    if request.user.is_authenticated:
        user = request.user
    
        context = {
            'products':products,
            'coverimage':coverimage,

        }
        return render(request,'users/index.html',context)
    context = {
        'products':products,
        'coverimage':coverimage,
    }
    return render(request, 'users/index.html',context)

def productpage(request):
    products = Product.objects.all()
    category = Category.objects.all().order_by('-id')
    product_filter = ProductFilter(request.GET,queryset=products)
    category_filter = CategoryFilter(request.GET,queryset=category)
    product_final = product_filter.qs
    category_final = category_filter.qs
    if request.user.is_authenticated:
        user = request.user
        items = Cart.objects.filter(user=user)
        context = {
            'products':products,
            'items':items,
            'product_filter':product_filter,
            'category': category_final
        }
        return render(request,'users/products.html',context)
    context = {
        'products':product_final,
        'product_filter':product_filter,
        'category': category_final
    }
    return render(request, 'users/products.html',context)

def product_details(request,product_id):
    products=Product.objects.get(id=product_id)
    product = Product.objects.all().order_by('-id')[:3]
    context = {
        'products':products,
        'product':product
    }

    return render(request,'users/productdetails.html',context)

def aboutus(request):
    members = Member.objects.all()
    context = {
        'members':members
    }
    return render(request, 'users/aboutus.html', context)


def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    

    paypal_dict = {
        'business': "sb-pmllk26578065@business.example.com",
        'amount': '%.2f' % order.total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }
    

    form = PayPalPaymentsForm(initial=paypal_dict)
    print(form)
    return render(request, 'users/aboutus.html', {'order': order, 'form': form})


@csrf_exempt
def payment_done(request):
    return render(request, 'users/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'users/payment_cancelled.html')
