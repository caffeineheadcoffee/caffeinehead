from apps.product.usecases import GetProductUseCase


class ProductMixin:
    def get_product(self, *args, **kwargs):
        return GetProductUseCase(
            product_id=self.kwargs.get('product_id')
        ).execute()
