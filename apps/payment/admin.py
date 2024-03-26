from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.payment import models


@admin.register(models.Payment)
class OrderItemAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'provider',
        'total',
    )
