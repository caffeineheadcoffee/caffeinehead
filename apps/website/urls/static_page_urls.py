from django.urls import path
from . import views

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
        'services/contract-roasting',
        static_page_views.ContractRoastingServiceView.as_view(),
        name='contract_roasting_service'
    ),
    path(
        'services/app-development',
        static_page_views.AppDevelopmentServiceView.as_view(),
        name='app_development_service'
    ),
    path(
        'services/coffee-cocktails',
        static_page_views.CoffeeCocktailsServiceView.as_view(),
        name='coffee_cocktails_service'
    ),
    path(
        'services/cyber-security',
        static_page_views.CyberSecurityServiceView.as_view(),
        name='cyber_security_service'
    ),
    path(
        'services/msp',
        static_page_views.MspServiceView.as_view(),
        name='msp_service'
    ),
    path(
        'services/pos',
        static_page_views.PosServiceView.as_view(),
        name='pos_service'
    ),
    path(
        'services/wholesale',
        static_page_views.WholesaleServiceView.as_view(),
        name='wholesale_service'
    ),
    path(
        'contact-us',
        static_page_views.ContactUsView.as_view(),
        name='contact_us'
    ),
    path(
        'partnership',
        static_page_views.PartnershipView.as_view(),
        name='partnership'
    ),
    path('form/',static_page_views.index, name='serviceform'),
    path('show/',static_page_views.services, name='serviceshow'),
    path('contact/',static_page_views.contact, name='contact'),
    path('messages/',static_page_views.show_message, name='messages')
]