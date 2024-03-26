from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED

from apps.payment import PaymentStatus
from apps.payment.models import Payment


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        payment = Payment.objects.get(pk=ipn_obj.invoice)
        order = payment.order
        payment.status = PaymentStatus.CONFIRMED
        order.status = 'invoiced'
        order.save()
        payment.save()
