from apps.core import usecases
from apps.order.exceptions import OrderItemNotFound
from apps.order.models import OrderItem


class GetOrderItemUseCase(usecases.BaseUseCase):
    def __init__(self, order_item_id: int):
        self._order_item_id = order_item_id

    def _factory(self):
        try:
            return OrderItem.objects.get(pk=self._order_item_id)
        except OrderItem.DoesNotExist:
            raise OrderItemNotFound
