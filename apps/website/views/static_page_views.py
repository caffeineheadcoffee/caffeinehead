from django.views import generic

from apps.website.mixins import OrderMixin


class AboutUsView(OrderMixin, generic.TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context.update({
            'order_items_count': self.get_order_items_count(),
        })
        return context


class ServicesView(OrderMixin, generic.TemplateView):
    template_name = 'pages/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context.update({
            'order_items_count': self.get_order_items_count(),
        })
        return context


class ContactUsView(OrderMixin, generic.TemplateView):
    template_name = 'pages/contact_us.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context.update({
            'order_items_count': self.get_order_items_count(),
        })
        return context