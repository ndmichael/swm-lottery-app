from django.shortcuts import render, get_object_or_404, redirect
from lottery.models import Ticket, Drawing
from django.contrib.auth.models import User
from lottery.models import WinningPick, BallNumbers
from .forms import WinnerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request, username):
    if not request.user.is_staff:
        redirect("index")
        messages.success(request, "You do not have permission to access this page.")
    return render(request, "adminapp/index.html")


@login_required
def admin_games(request, game_type):
    if not request.user.is_staff:
        redirect("index")
        messages.success(request, "You do not have permission to access this page.")
    if game_type == "bronze":
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(draw_type=game_type).order_by("-date")
        print(details)

    elif game_type == "silver":
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(draw_type=game_type).order_by("-date")

    elif game_type == "gold":
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(draw_type=game_type).order_by("-date")

    else:
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(draw_type=game_type).order_by("-date")

    context = {"details": details, "type": game_type}
    return render(request, "adminapp/admin_games.html", context)


@login_required
def winner(request, ticket_id):
    if not request.user.is_staff:
        redirect("index")
        messages.success(request, "You do not have permission to access this page.")
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user = get_object_or_404(User, id=ticket.user_id.id)
    draw = get_object_or_404(Drawing, id=ticket.drawing_id.id)

    print(ticket.drawing_id)
    if request.method == "POST":
        correct_number = request.POST.getlist("ball_numbers")
        special_number = request.POST.get("special_number")

        winningpick = WinningPick(
            drawing_id=ticket.drawing_id,
            special_number=special_number,
        )
        winningpick.save()
        for ball in correct_number:
            winningpick.correct_number.add(BallNumbers.objects.create(ball=ball))
        redirect("admin_index", request.user.username)
        messages.success(request, f"{user.username} has been confirmed as winner.")
    w_form = WinnerForm()
    context = {"user": user, "ticket": ticket, "w_form": w_form}
    return render(request, "adminapp/winner.html", context)
