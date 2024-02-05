from django.urls import path

from apps.website.views import cart_views, auth_views

urlpatterns = [
    path(
        'login',
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'signup',
        auth_views.SignupView.as_view(),
        name='signup'
    ),
]
