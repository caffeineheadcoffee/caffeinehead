from django.urls import path

from apps.website.views import product_views, cart_views

urlpatterns = [
    path(
        'cart',
        cart_views.CartView.as_view(),
        name='cart'
    ),
    path(
        'product/<int:product_id>/add-to-cart',
        cart_views.AddToCartView.as_view(),
        name='add_to_cart'
    ),
    path(
        'payment',
        cart_views.PaymentView.as_view(),
        name='payment'
    ),
]
