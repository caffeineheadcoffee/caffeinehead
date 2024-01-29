from django.urls import path, include

from apps.website import views

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'product/',
        include('apps.website.urls.product_urls')
    ),
    path(
        '',
        include('apps.website.urls.cart_urls')
    ),
    path(
        '',
        include('apps.website.urls.static_page_urls')
    ),
    path(
        '',
        include('apps.website.urls.auth_urls')
    )
]