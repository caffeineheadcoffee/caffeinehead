from django.views import generic

from apps.order.mixins import OrderMixin
from apps.website import forms


class AboutUsView(OrderMixin, generic.TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context.update({
                'order_items_count': self.get_order_items_count(),
            })
        return context


class ServicesView(OrderMixin, generic.TemplateView):
    template_name = 'pages/services/index.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context.update({
                'order_items_count': self.get_order_items_count(),
            })
        return context


class ContractRoastingServiceView(ServicesView):
    template_name = 'pages/services/contract_roasting.html'


class AppDevelopmentServiceView(ServicesView):
    template_name = 'pages/services/app_development.html'


class CoffeeCocktailsServiceView(ServicesView):
    template_name = 'pages/services/coffee_cocktails.html'


class CyberSecurityServiceView(ServicesView):
    template_name = 'pages/services/cyber_security.html'


class MspServiceView(ServicesView):
    template_name = 'pages/services/msp.html'


class PosServiceView(ServicesView):
    template_name = 'pages/services/pos.html'


class WholesaleServiceView(ServicesView):
    template_name = 'pages/services/wholesale.html'


class ContactUsView(OrderMixin, generic.FormView):
    template_name = 'pages/contact_us.html'
    form_class = forms.EnquiryForm

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context.update({
            'order_items_count': self.get_order_items_count(),
        })
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
