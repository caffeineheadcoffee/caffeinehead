import uuid

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from paypal.standard.forms import PayPalPaymentsForm

from apps.order.mixins import OrderMixin, OrderItemMixin
from apps.order.models import Order
from apps.payment.models import Payment
from apps.product.mixins import ProductMixin
from apps.website import forms
from apps.website.usecases import cart_usecases


class CartView(LoginRequiredMixin, OrderMixin, generic.TemplateView):
    template_name = 'pages/cart.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        order = Order.objects.filter(
            user=self.request.user,
            is_archived=False,
            status='initiated'
        ).last()
        context.update({
            'order': order,
            'order_items': order.orderitem_set.unarchived(),
            'order_items_count': self.get_order_items_count(),
        })
        return context


class AddToCartView(LoginRequiredMixin, ProductMixin, generic.View):
    login_url = '/login'

    def get(self, request, *args, **kwargs):
        cart_usecases.AddToCartUseCase(
            product=self.get_product(),
            user=self.request.user
        ).execute()
        return HttpResponseRedirect(request.GET.get('next'))


class DeleteOrderItemView(LoginRequiredMixin, OrderItemMixin, generic.View):
    login_url = '/login'

    def get(self, request, *args, **kwargs):
        cart_usecases.DeleteOrderItemUseCase(
            order_item=self.get_order_item(),
            user=self.request.user
        ).execute()
        return HttpResponseRedirect(request.GET.get('next'))


class PaymentView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/payment.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        order = Order.objects.filter(
            user=self.request.user,
            is_archived=False,
            status='initiated'
        ).last()

        host = self.request.get_host()
        currency = 'USD'

        payment = Payment.objects.create(
            order=order,
            provider='paypal',
            currency=currency,
            total=order.total
        )

        paypal_checkout = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': order.total,
            'invoice': payment.id,
            'currency_code': 'USD',
            'notify_url': f"http://{host}{reverse('paypal-ipn')}",
            'return_url': f"http://{host}{reverse('order_complete')}",
            'cancel_url': f"http://{host}cancel",
        }
        paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

        context.update({
            'order': order,
            'shipping_address': order.shippingaddress if hasattr(order, 'shippingaddress') else None,
            'order_items': order.orderitem_set.unarchived(),
            'paypal': paypal_payment
        })
        return context


class OrderCompleteView(OrderMixin, generic.TemplateView):
    template_name = 'pages/order_complete.html'


class AddShippingAddressView(LoginRequiredMixin, OrderMixin, generic.View):
    login_url = '/login'

    def post(self, request, *args, **kwargs):
        form = forms.AddShippingAddressForm(request.POST)
        if form.is_valid():
            cart_usecases.AddShippingAddressUseCase(
                order=self.get_order(),
                form=form
            ).execute()
            return JsonResponse(form.cleaned_data)
        else:
            return JsonResponse({'errors': form.errors}, status=400)





