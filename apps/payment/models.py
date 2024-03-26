from typing import Union

from django.db import models

from apps.core.models import BaseModel
from apps.order.models import Order
from apps.payment import PaymentStatus


class Payment(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    #: Transaction status
    status = models.CharField(
        db_index=True,
        max_length=10,
        choices=PaymentStatus.CHOICES,
        default=PaymentStatus.WAITING
    )
    #: Transaction ID (if applicable)
    transaction_id = models.CharField(max_length=255, blank=True)
    #: Currency code (may be provider-specific)
    currency = models.CharField(max_length=10)
    #: Total amount (gross)
    total = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")
    extra_data = models.JSONField(blank=True, default=dict)
    captured_amount = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")

    def __str__(self):
        return self.provider
