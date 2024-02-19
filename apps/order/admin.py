from django.contrib import admin
from nested_admin import nested

from apps.core.admin import BaseModelAdmin
from apps.order import models


class OrderItemInline(nested.NestedStackedInline):
    model = models.OrderItem
    extra = 0


class ShippingAddressInline(nested.NestedStackedInline):
    model = models.ShippingAddress
    extra = 0


@admin.register(models.Order)
class OrderAdmin(nested.NestedModelAdmin, BaseModelAdmin):
    list_display = (
        'id',
        'user',
        'total',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'status',
    )
    inlines = [
        OrderItemInline,
        ShippingAddressInline
    ]

    class Media:
        js = (
            'js/steps.js',
        )


@admin.register(models.OrderItem)
class OrderItemAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'product',
        'amount',
    )


@admin.register(models.ShippingAddress)
class ShippingAddressAdmin(BaseModelAdmin):
    pass
