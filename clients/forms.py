from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from allauth.account.forms import SignupForm, LoginForm

# from django_countries.fields import CountryField
from django.utils import timezone
from lottery import models


class DateInput(forms.DateInput):
    input_type = "date"


class SelfLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs["placeholder"] = ""
        self.fields["password"].widget.attrs["placeholder"] = ""

        self.fields["login"].widget.attrs.update(
            {
                "class": "form-control-lg bg-success text-white border-0  border-bottom mb-3"
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control-lg  bg-success text-white border-0  border-bottom mb-3"
            }
        )


class MyCustomSignupForm(SignupForm):
    states = (
        ("Abia State", "Abia State"),
        ("Adamawa State", "Adamawa State"),
        ("Akwa Ibom State", "Akwa Ibom State"),
        ("Anambra State", "Anambra State"),
        ("Bauchi State", "Bauchi State"),
        ("Bayelsa State", "Bayelsa State"),
        ("Benue State", "Benue State"),
        ("Borno State", "Borno State"),
        ("Cross River State", "Cross River State"),
        ("Delta State", "Delta State"),
        ("Ebonyi State", "Ebonyi State"),
        ("Edo State", "Edo State"),
        ("Ekiti State", "Ekiti State"),
        ("Enugu State", "Enugu State"),
        ("Gombe State", "Gombe State"),
        ("Imo State", "Imo State"),
        ("Jigawa State", "Jigawa State"),
        ("Kaduna State", "Kaduna State"),
        ("Kano State", "Kano State"),
        ("Katsina State", "Katsina State"),
        ("Kebbi State", "Kebbi State"),
        ("Kogi State", "Kogi State"),
        ("Kwara State", "Kwara State"),
        ("Lagos State", "Lagos State"),
        ("Nasarawa State", "Nasarawa State"),
        ("Niger State", "Niger State"),
        ("Ogun State", "Ogun State"),
        ("Ondo State", "Ondo State"),
        ("Osun State", "Osun State"),
        ("Oyo State", "Oyo State"),
        ("Plateau State", "Plateau State"),
        ("Rivers State", "Rivers State"),
        ("Sokoto State", "Sokoto State"),
        ("Taraba State", "Taraba State"),
        ("Yobe State", "Yobe State"),
        ("Zamfara State", "Zamfara State"),
    )
    gender = (("male", "MALE"), ("female", "FEMALE"), ("others", "OTHERS"))
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last name")
    phone_number = forms.CharField(required=False)
    address = forms.CharField(
        widget=forms.Textarea(attrs={"name": "body", "rows": "2"})
    )
    # country = CountryField(blank=True).formfield()
    dob = forms.DateField(widget=DateInput)
    city = forms.ChoiceField(required=False, choices=states)
    gender = forms.ChoiceField(choices=gender, required=False)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        models.Profile.objects.create(
            user=user,
            phone_number=self.cleaned_data["phone_number"],
            city=self.cleaned_data["city"],
            address=self.cleaned_data["address"],
            gender=self.cleaned_data["gender"],
            dob=self.cleaned_data["dob"],
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

        self.fields["first_name"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["username"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["email"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["dob"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["phone_number"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["gender"].widget.attrs.update({"class": "form-control-lg"})
        self.fields["city"].widget.attrs.update({"class": "form-control-lg"})


class WithdrawalForm(forms.Form):
    banks = (
        ("", "PLEASE SELECT"),
        ("Access Bank", "Access Bank"),
        ("Fidelity Bank", "Fidelity Bank Plc"),
        ("Ecobank", "Ecobank"),
        ("First Bank", "First Bank"),
        ("Guaranty Trust Bank", "Guaranty Trust Bank"),
        ("Union Bank", "Union Bank"),
        ("United Bank", "United Bank"),
        ("Zenith Bank", "Zenith Bank"),
        ("Wema Bank", "Wema Bank"),
        ("Sterling Bank", "Sterling Bank"),
    )
    select_bank = forms.ChoiceField(choices=banks)
    account_number = forms.IntegerField()
    withdraw_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    agreement = forms.BooleanField(
        label="",
        help_text="I declare that I have carefully read and fully understood the Withdrawal Terms and Conditions of SWM Lottery, which I accept and agree with, and that I understand that any fund withdrawals from my account will result in the proportional removal of the amount in my wallet. \
        I also acknowledge and accept that my withdrawal request may be amended and completed according to the Withdrawal Priority Procedure. Furthermore, I consent to my personal data being stored and used for any future transactions.",
    )

    def __init__(self, *args, **kwargs):
        super(WithdrawalForm, self).__init__(*args, **kwargs)
        self.fields["select_bank"].widget.attrs.update(
            {
                "class": "form-control-lg rounded-9 bg-success text-white",
            }
        )
        self.fields["account_number"].widget.attrs.update(
            {
                "class": "form-control-lg rounded-9 bg-success text-white",
                "placeholder": "ENTER ACCOUNT NUMBER",
            }
        )
        self.fields["withdraw_amount"].widget.attrs.update(
            {"class": "form-control-lg rounded-9 bg-success text-white"}
        )
        self.fields["agreement"].widget.attrs.update({"class": "text-success"})
