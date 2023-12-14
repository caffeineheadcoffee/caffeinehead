from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/<int:user_id>', views.update_user, name='dashboard'),
    path(
        '',
        views.HomePageView.as_view(),
        name='home'
    ),
    path(
        'all-products/',
        views.AllProductPageView.as_view(),
        name='all-products'
    ),
    path(
        'product/<int:product_id>/product-detail',
        views.ProductDetailView.as_view(),
        name='product-detail'
    ),
    path('about/', views.aboutus, name='about'),
    path('services/', views.services, name='services'),
    path('services_contractRoasting/', views.services_contractRoasting),
    path('services_Wholesale/', views.services_Wholesale),
    path('services_POS/', views.services_POS),
    path('services_Appdev/', views.services_Appdev),
    path('services_MSP/', views.services_MSP),
    path('services_CyberSecurity/', views.services_CyberSecurity),
    path('services_CoffeeCocktails/', views.services_CoffeeCocktails),

    path('contact/', views.save_contact, name='contact'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
