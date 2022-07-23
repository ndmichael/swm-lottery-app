from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from lottery.models import Profile
from lottery.models import Ticket, WinningPick
from .forms import WithdrawalForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.


def profile(request, username):
    user = get_object_or_404(User, username=username)
    p = Paginator(Ticket.objects.filter(user_id=user.id).order_by("-date"), 10)
    page = request.GET.get("page")
    tickets = p.get_page(page)
    today = datetime.now()

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
            return redirect("profile", user.username)

    else:
        w_form = WithdrawalForm()
    context = {
        "user": user,
        "tickets": tickets,
        "w_form": w_form,
        "today": today,
    }
    return render(request, "account/profile.html", context)


def update_profile(request, username):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"account successfully updated")
            return redirect(
                "profile", username=request.user.username
            )  # i solved that by passing the requesting user username
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "account/update_profile.html", context)
