from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from lottery.models import Profile

# Create your views here.


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        "user": user,
    }
    return render(request, "account/profile.html", context)
