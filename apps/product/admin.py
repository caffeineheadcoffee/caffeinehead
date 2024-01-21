from django.contrib import admin
from nested_admin import nested

from apps.core.admin import BaseModelAdmin
from apps.product import models


class ProductImageInline(nested.NestedStackedInline):
    model = models.ProductImage
    extra = 0


@admin.register(models.Product)
class ProductAdmin(nested.NestedModelAdmin, BaseModelAdmin):
    list_display = (
        'id',
        'name',
        'product_price',
        'created'
    )
    inlines = [
        ProductImageInline,
    ]

    class Media:
        js = (
            'js/steps.js',
        )


@admin.register(models.ProductImage)
class ProductImageAdmin(BaseModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(BaseModelAdmin):
    pass


admin.site.register(models.Member)
admin.site.register(models.AboutUs)
admin.site.register(models.ImageSlider)
