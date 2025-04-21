from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect, \
    get_object_or_404, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from paypal.standard.forms import PayPalPaymentsForm

from .filters import *
from .forms import *
from ..product.forms import Contact_usForm
from ..product.models import ImageSlider, Cart, Member, Order


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


def update_user(request, user_id):
    instance = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated')
            return redirect('/users/dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'please verify forms fields. ')
            return render(request, 'users/dashboard.html', {
                'form': form
            })
    context = {
        'form': RegistrationForm(instance=instance)
    }

    return render(request, 'users/dashboard.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Please provide correct credentails ')
                return render(request, 'users/login.html', {
                    'forms': form
                })

    form = AccountAuthenticationForm
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login')


class HomePageView(TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['products_list'] = Product.objects.all().order_by('-id')[:4]
        context['cover_images'] = ImageSlider.objects.all()
        return context


class CollectionPageView(TemplateView):
    template_name = 'users/collection.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionPageView, self).get_context_data(**kwargs)
        categories = Category.objects.annotate(
            product_count=Count('product')
        ).filter(product_count__gt=0)

        category_products = [
            {
                'id': category.id,
                'name': category.name,
                'products': category.product_set.all()
            } for category in categories
        ]
        context.update({
            'products': Product.objects.all(),
            'category_products': category_products
        })
        if self.request.user.is_authenticated:
            items = Cart.objects.filter(user=self.request.user)
            context.update({
                'items': items,
            })
        return context


# def productpage(request):
#     products = Product.objects.all()
#     category = Category.objects.all().order_by('-id')
#     product_filter = ProductFilter(request.GET, queryset=products)
#     category_filter = CategoryFilter(request.GET, queryset=category)
#     product_final = product_filter.qs
#     category_final = category_filter.qs
#     if request.user.is_authenticated:
#         user = request.user
#         items = Cart.objects.filter(user=user)
#         context = {
#             'products': products,
#             'items': items,
#             'product_filter': product_filter,
#             'category': category_final
#         }
#         return render(request, 'users/products.html', context)
#     context = {
#         'products': product_final,
#         'product_filter': product_filter,
#         'category': category_final
#     }
#     return render(request, 'users/products.html', context)


class ProductDetailView(TemplateView):
    template_name = 'users/productdetails.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update({
            'product_list': Product.objects.all()[:3],
            'product': Product.objects.get(pk=self.kwargs['product_id'])
        })
        return context


def aboutus(request):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'users/aboutus.html', context)


def services(request):
    return render(request, 'users/services.html')


def services_contractRoasting(request):
    return render(request, 'users/services_contractRoasting.html')


def services_Wholesale(request):
    return render(request, 'users/services_Wholesale.html')


def services_POS(request):
    return render(request, 'users/services_POS.html')


def services_Appdev(request):
    return render(request, 'users/services_Appdev.html')


def services_MSP(request):
    return render(request, 'users/services_MSP.html')


def services_CyberSecurity(request):
    return render(request, 'users/services_CyberSecurity.html')


def services_CoffeeCocktails(request):
    return render(request, 'users/services_CoffeeCocktails.html')


def contact(request):
    return render(request, 'users/contact.html')


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


def save_contact(request):
    if request.method == "POST":
        form = Contact_usForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Contact added')
            return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify forms fields. ')
            return render(request, 'users/contact.html', {
                'form': form
            })
    context = {
        'form': Contact_usForm
    }
    return render(request, 'users/contact.html', context)


def user_profile(request):
    profilelist = User.objects.get(pk=request.user.pk)
    context = {
        "profile": profilelist
    }
    return render(request, "users/dashboard.html", context)
