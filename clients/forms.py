from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from allauth.account.forms import SignupForm, LoginForm
# from django_countries.fields import CountryField
from django.utils import timezone
from . import models


class MyCustomSignupForm(SignupForm):
    # field_order = ['first_name', 'last_name',  'username',
    #                'email', 'password1', 'password2', 'balance','country', 'address', 'dob','image']
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last name')
    phoneNumber = forms.CharField()
    address = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'2'}))
    # country = CountryField(blank=True).formfield()
    country = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    gender = forms.ChoiceField()

    

    def __init__(self, *args, **kwargs):

        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = ""
        self.fields["last_name"].widget.attrs["placeholder"] = ""
        self.fields["email"].widget.attrs["placeholder"] = ""
        self.fields["username"].widget.attrs["placeholder"] = ""
        self.fields["password1"].widget.attrs["placeholder"] = ""
        self.fields["password2"].widget.attrs["placeholder"] = ""

        self.fields["first_name"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["last_name"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["email"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["country"].widget.attrs.update({'class': 'form-control-lg'})