from decimal import Decimal

from django.db.models import Sum, F
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from apps.order import models


@receiver(post_save, sender=models.OrderItem)
@receiver(post_delete, sender=models.OrderItem)
def update_order(sender, instance, **kwargs):
    order_instance = instance.order
    # get sub amount
    sub_total = models.OrderItem.objects.filter(
        order=order_instance,
        is_archived=False
    ).aggregate(
        sub_total=Sum('amount')
    ).get('sub_total')

    if not sub_total:
        sub_total = Decimal(0)

    # update order  amount
    order_instance.sub_total = sub_total
    order_instance.total = order_instance.sub_total - Decimal(order_instance.discount_amount) + Decimal(order_instance.shipping_amount)
    order_instance.save()


@receiver(post_save, sender=models.OrderItem)
def update_product_stock(sender, instance, **kwargs):
    if instance.order.status == 'ordered':
        # get products
        order_items = models.OrderItem.objects.filter(
            order=instance,
            is_archived=False
        )
        for order_item in order_items:
            product = order_item.product
            product.stock -= order_item.quantity
            product.save()




