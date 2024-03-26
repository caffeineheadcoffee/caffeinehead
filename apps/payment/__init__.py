from django.utils.translation import pgettext_lazy

default_app_config = 'apps.payment.apps.PaymentConfig'


class PaymentStatus:
    WAITING = "waiting"
    PREAUTH = "preauth"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"
    REFUNDED = "refunded"
    ERROR = "error"
    INPUT = "input"

    CHOICES = [
        (WAITING, pgettext_lazy("payment status", "Waiting for confirmation")),
        (PREAUTH, pgettext_lazy("payment status", "Pre-authorized")),
        (CONFIRMED, pgettext_lazy("payment status", "Confirmed")),
        (REJECTED, pgettext_lazy("payment status", "Rejected")),
        (REFUNDED, pgettext_lazy("payment status", "Refunded")),
        (ERROR, pgettext_lazy("payment status", "Error")),
        (INPUT, pgettext_lazy("payment status", "Input")),
    ]
