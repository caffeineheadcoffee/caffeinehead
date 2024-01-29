from apps.core import usecases
from apps.product.exceptions import ProductNotFound
from apps.product.models import Product


class GetProductUseCase(usecases.BaseUseCase):
    def __init__(self, product_id: int):
        self._product_id = product_id

    def _factory(self):
        try:
            return Product.objects.get(pk=self._product_id)
        except Product.DoesNotExist:
            raise ProductNotFound
