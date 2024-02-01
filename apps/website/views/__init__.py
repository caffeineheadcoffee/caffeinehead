from django.views import generic

from apps.order.mixins import OrderMixin
from apps.product.models import Product, ImageSlider


class HomeView(OrderMixin, generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'products_list': Product.objects.all().order_by('-id')[:4],
            'cover_images': ImageSlider.objects.all(),
            'current_route': self.request.path,
        })
        if self.request.user.is_authenticated:
            context.update({
                'order_items_count': self.get_order_items_count(),
            })
        return context
