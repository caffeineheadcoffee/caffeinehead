from django.urls import path
from . import views


urlpatterns=[
<<<<<<< HEAD
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('logout/',views.logout_user),
    path('',views.homepage),
    path('productspage/',views.productpage),
    path('productdetails/<int:product_id>', views.product_details),
    path('about/',views.aboutus),
    path('services/',views.services),
=======
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('dashboard/<int:user_id>',views.update_user,name='dashboard'),
    path('',views.homepage,name='home'),
    path('allproducts/',views.productpage,name='products'),
    path('productdetails/<int:product_id>', views.product_details,name='productdetail'),
    path('about/',views.aboutus,name='about'),
    path('services/',views.services,name='services'),
>>>>>>> 3d5d0b90940b58cf0c723bb7b3f5947889e96060
    path('services_contractRoasting/',views.services_contractRoasting),
    path('services_Wholesale/',views.services_Wholesale),
    path('services_POS/',views.services_POS),
    path('services_Appdev/',views.services_Appdev),
    path('services_MSP/',views.services_MSP),
    path('services_CyberSecurity/',views.services_CyberSecurity),
    path('services_CoffeeCocktails/',views.services_CoffeeCocktails),
  
    path('contact/', views.save_contact,name='contact'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]