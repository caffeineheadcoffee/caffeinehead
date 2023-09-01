from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index),
    path('addproduct/', views.post_product),
    path('addcategory/', views.post_category),
    path('updateproduct/<int:product_id>', views.update_product),
    path('deleteproduct/<int:product_id>', views.delete_product),
    path('category/', views.show_category),
    path('updatecategory/<int:category_id>',views.update_category),
    path('deletecategory/<int:category_id>',views.delete_category),
    path('add_to_cart/<int:product_id>',views.add_to_cart),
    path('mycart',views.show_cart_item),
    path('deletecartitems/<int:cart_id>', views.remove_cart_item),
    path('orderitemform/<int:product_id>/<int:cart_id>', views.order_item_form),
    
    path('my_order',views.my_order),
    path('allorder',views.all_order),
    path('addmember/', views.post_member),
    path('updatemember/<int:member_id>', views.update_member),
    path('deletemember/<int:member_id>', views.delete_member),
    path('addaboutus/', views.post_aboutus),
    path('updateaboutus/<int:aboutus_id>', views.update_aboutus),
    path('deleteaboutus/<int:aboutus_id>', views.delete_aboutus),
    path('addcoverimage/', views.post_coverimage),
    path('updatecoverimage/<int:imageslider_id>', views.update_coverimage),
    path('deletecoverimage/<int:imageslider_id>', views.delete_coverimage),
    path('member/', views.show_member),
    path('aboutus/', views.show_aboutus),
    path('coverimage/', views.show_coverimage),
    
]