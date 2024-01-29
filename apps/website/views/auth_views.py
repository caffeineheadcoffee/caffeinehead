from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import generic

from apps.website import forms


class LoginView(generic.FormView):
    template_name = 'pages/login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(self.request, email=data['email'], password=data['password'])

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class SignupView(generic.FormView):
    template_name = 'pages/signup.html'
    form_class = forms.SignupForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
