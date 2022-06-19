from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from allauth.account.forms import SignupForm, LoginForm
# from django_countries.fields import CountryField
from django.utils import timezone
from lottery import models


class DateInput(forms.DateInput):
    input_type = 'date'


class SelfLoginForm (LoginForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs["placeholder"] = ""
        self.fields["password"].widget.attrs["placeholder"] = ""
        
        self.fields["login"].widget.attrs.update(
            {'class': 'form-control-lg bg-success border-0  border-bottom mb-3'})
        self.fields["password"].widget.attrs.update(
            {'class': 'form-control-lg  bg-success border-0  border-bottom mb-3'})


class MyCustomSignupForm(SignupForm):
    # field_order = ['first_name', 'last_name',  'username',
    #                'email', 'password1', 'password2', 'balance','country', 'address', 'dob','image']
    gender= (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('others', 'OTHERS')
    )
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last name')
    phone_number = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'2'}))
    # country = CountryField(blank=True).formfield()
    dob = forms.DateField(widget=DateInput)
    city = forms.CharField(max_length=20, required=False)
    gender = forms.ChoiceField(choices=gender,  required=False)

    def save(self, request):
            user = super(MyCustomSignupForm, self).save(request)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()

            models.Profile.objects.create(
                user=user, 
                phone_number=self.cleaned_data['phone_number'], 
                city=self.cleaned_data['city'], 
                address = self.cleaned_data['address'],
                gender=self.cleaned_data['gender'], 
                dob=self.cleaned_data['dob'],
            )
            return user


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
        self.fields["username"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["email"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["dob"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["phone_number"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["gender"].widget.attrs.update({'class': 'form-control-lg'})
        self.fields["city"].widget.attrs.update({'class': 'form-control-lg'})