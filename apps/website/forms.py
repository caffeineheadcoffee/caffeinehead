from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from apps.website.models import Enquiry

User = get_user_model()


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid email or password')


class SignupForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. Add a valid email address')

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "password1",
            "password2"
        )


class EnquiryForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='AU')
    )

    class Meta:
        model = Enquiry
        fields = "__all__"
