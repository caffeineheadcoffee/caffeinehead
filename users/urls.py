from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('logout/',views.logout_user),
    path('',views.homepage),
    path('allproducts/',views.productpage),
    path('productdetails/<int:product_id>', views.product_details),
    path('about/',views.aboutus),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]