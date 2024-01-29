from apps.order.models import OrderItem


class OrderMixin:
    def get_order_items_count(self):
        return OrderItem.objects.filter(
            order__user=self.request.user,
            order__status='initiated',
            is_archived=False,
            order__is_archived=False
        ).count()
