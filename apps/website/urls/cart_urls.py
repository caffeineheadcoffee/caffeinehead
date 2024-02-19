from django.urls import path

from apps.website.views import cart_views

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
        'order-item/<int:order_item_id>/delete-order-item',
        cart_views.DeleteOrderItemView.as_view(),
        name='delete_order_item'
    ),
    path(
        'payment',
        cart_views.PaymentView.as_view(),
        name='payment'
    ),
    path(
        'order/<int:order_id>/add-shipping-address',
        cart_views.AddShippingAddressView.as_view(),
        name='add_shipping_address'
    ),
    path(
        'order-complete',
        cart_views.OrderCompleteView.as_view(),
        name='order_complete'
    ),
]
