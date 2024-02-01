from apps.order.models import OrderItem
from apps.order.usecases import GetOrderItemUseCase


class OrderMixin:
    def get_order_items_count(self):
        return OrderItem.objects.filter(
            order__user=self.request.user,
            order__status='initiated',
            is_archived=False,
            order__is_archived=False
        ).count()


class OrderItemMixin:
    def get_order_item(self):
        return GetOrderItemUseCase(
            order_item_id=self.kwargs.get('order_item_id')
        ).execute()
