from django.urls import path

from apps.website.views import product_views

urlpatterns = [
    path(
        '<int:product_id>/product-detail',
        product_views.ProductDetailView.as_view(),
        name='product_detail'
    ),
    path(
        'collection',
        product_views.CollectionView.as_view(),
        name='collection'
    ),
    path(
        'view_products',
        product_views.ViewProductsView.as_view(),
        name='view_products'
    )
]