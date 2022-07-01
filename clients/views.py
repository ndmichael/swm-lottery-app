from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from lottery.models import Profile
from lottery.models import Ticket, WinningPick
from .forms import WithdrawalForm
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def profile(request, username):
    user = get_object_or_404(User, username=username)
    tickets = Ticket.objects.filter(user_id=user.id).order_by("-date")

    if request.method == "POST":
        w_form = WithdrawalForm(request.POST)
        if w_form.is_valid():
            select_bank = w_form.cleaned_data["select_bank"]
            account_number = w_form.cleaned_data["account_number"]
            withdraw_amount = w_form.cleaned_data["withdraw_amount"]
            email = user.email
            subject = f"Withdrawal Request by - {user.username}"
            message = f"User: {user.username}\nBank: {select_bank}\nAccount Number:{account_number}\nRequested amount: #{withdraw_amount}\n"
            print(message)
            send_mail(
                subject,
                message,
                email,
                ["Lttrglbl@gmail.com"],
            )
            messages.success(request, "Withdrawal Request Has been successfully sent.")
            return redirect("all-games")

    else:
        w_form = WithdrawalForm()
    context = {
        "user": user,
        "tickets": tickets,
        "w_form": w_form,
    }
    return render(request, "account/profile.html", context)
