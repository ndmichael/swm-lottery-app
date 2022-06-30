from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from lottery.models import Profile
from lottery.models import Ticket, WinningPick
from .forms import WithdrawalForm

# Create your views here.


def profile(request, username):
    w_form = WithdrawalForm()
    user = get_object_or_404(User, username=username)
    tickets = Ticket.objects.filter(user_id=user.id).order_by("-date")

    context = {
        "user": user,
        "tickets": tickets,
        "w_form": w_form,
    }
    return render(request, "account/profile.html", context)
