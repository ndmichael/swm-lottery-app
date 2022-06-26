from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from lottery.models import Profile
from lottery.models import Ticket

# Create your views here.


def profile(request, username):
    user = get_object_or_404(User, username=username)
    tickets = Ticket.objects.filter(user_id=user.id).order_by("-date")
    context = {"user": user, "tickets": tickets}
    return render(request, "account/profile.html", context)
