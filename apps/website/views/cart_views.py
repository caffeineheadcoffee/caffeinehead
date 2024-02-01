from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from apps.order.models import Order
from apps.product.mixins import ProductMixin
from apps.website.mixins import OrderMixin
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


class PaymentView(OrderMixin, generic.TemplateView):
    template_name = 'pages/payment.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
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
    
class OrderCompleteView(OrderMixin, generic.TemplateView):
    order_complete = 'pages/order_complete.html'