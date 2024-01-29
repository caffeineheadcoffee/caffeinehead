from django.db.models import DecimalField

from apps.core import validators


class AmountField(DecimalField):
    def __init__(self, allow_zero=False, *args, **kwargs):
        self.allow_zero = allow_zero
        kwargs.setdefault('max_digits', 8)
        kwargs.setdefault('decimal_places', 2)
        super().__init__(*args, **kwargs)
        self.validators.append(validators.AmountValidator(allow_zero=self.allow_zero))
