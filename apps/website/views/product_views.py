from django.db.models import Count
from django.views import generic

from apps.order.models import Order, OrderItem
from apps.product.mixins import ProductMixin
from apps.product.models import Product, Category
from apps.website.mixins import OrderMixin


class ProductDetailView(generic.TemplateView, OrderMixin, ProductMixin):
    template_name = 'pages/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = self.get_product()
        context.update({
            'product_list': Product.objects.all()[:3],
            'product': product,
            'product_images': product.productimage_set.unarchived(),
            'current_route': self.request.path,
            'order_items_count': self.get_order_items_count(),

        })
        return context


class CollectionView(OrderMixin, generic.TemplateView):
    template_name = 'pages/collection.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionView, self).get_context_data(**kwargs)
        categories = Category.objects.annotate(
            product_count=Count('product')
        ).filter(product_count__gt=0)

        category_products = [
            {
                'id': category.id,
                'name': category.name,
                'products': category.product_set.all()[:5]
            } for category in categories
        ]
        context.update({
            'products': Product.objects.all()[:5],
            'category_products': category_products,
            'current_route': self.request.path
        })
        if self.request.user.is_authenticated:
            context.update({
                'order_items_count': self.get_order_items_count(),
            })
        return context
