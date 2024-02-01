from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from apps.core import usecases
from apps.order.models import Order, OrderItem
from apps.product.models import Product

User = get_user_model()


class AddToCartUseCase(usecases.BaseUseCase):
    def __init__(self, product: Product, user: User):
        self._user = user
        self._product = product

    def _factory(self):
        order, _created = Order.objects.get_or_create(
            is_archived=False,
            user=self._user,
            status='initiated'
        )
        order_item, _order_item_created = OrderItem.objects.get_or_create(
            order=order,
            is_archived=False,
            product=self._product
        )
        order_item.quantity += 1
        order_item.save()


class DeleteOrderItemUseCase(usecases.BaseUseCase):
    def __init__(self, order_item: OrderItem, user: User):
        self._user = user
        self._order_item = order_item

    def _factory(self):
        self._order_item.archive()

    def is_valid(self):
        # 1. check if order item is of same user
        if self._order_item.order.user != self._user:
            raise ValidationError('Not a valid order item id')
