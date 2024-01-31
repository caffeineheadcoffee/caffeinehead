from django.urls import path

from apps.website.views import product_views, static_page_views

urlpatterns = [
    path(
        'about_us',
        static_page_views.AboutUsView.as_view(),
        name='about_us'
    ),
    path(
        'services',
        static_page_views.ServicesView.as_view(),
        name='services'
    ),
    path(
        'contact_us',
        static_page_views.ContactUsView.as_view(),
        name='contact_us'
    )
]