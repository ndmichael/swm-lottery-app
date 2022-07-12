from django.shortcuts import render, get_object_or_404, redirect
from lottery.models import Ticket, Drawing
from django.contrib.auth.models import User
from lottery.models import (
    WinningPick,
    BallNumbers,
    Bronze,
    Silver,
    Gold,
    Platinum,
    Jackpot,
    Megawin,
)
from .forms import WinnerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator

# Create your views here.


@login_required
def index(request, username):
    if not request.user.is_staff:
        redirect("index")
        messages.success(request, "You do not have permission to access this page.")

    return render(request, "adminapp/index.html")


@login_required
def admin_games(request, game_type):
    print(game_type)
    if not request.user.is_staff:
        messages.success(request, "You do not have permission to access this page.")
        return redirect("index")
    if game_type == "bronze":
        p = Paginator(Ticket.objects.filter(draw_type=game_type).order_by("-date"), 20)
        page = request.GET.get("page")
        details = p.get_page(page)

    elif game_type == "silver":
        p = Paginator(Ticket.objects.filter(draw_type=game_type).order_by("-date"), 20)
        page = request.GET.get("page")
        details = p.get_page(page)

    elif game_type == "gold":
        p = Paginator(Ticket.objects.filter(draw_type=game_type).order_by("-date"), 20)
        page = request.GET.get("page")
        details = p.get_page(page)

    elif game_type == "platinum":
        p = Paginator(Ticket.objects.filter(draw_type=game_type).order_by("-date"), 20)
        page = request.GET.get("page")
        details = p.get_page(page)

    elif game_type == "jackpot":
        p = Paginator(Ticket.objects.filter(draw_type=game_type).order_by("-date"), 20)
        page = request.GET.get("page")
        details = p.get_page(page)

    elif game_type == "megawin":
        p = Paginator(Ticket.objects.filter(draw_type=game_type).order_by("-date"), 20)
        page = request.GET.get("page")
        details = p.get_page(page)

    context = {"details": details, "type": game_type}
    return render(request, "adminapp/admin_games.html", context)


@login_required
def winner(request, ticket_id):
    game_id = None
    if not request.user.is_staff:
        redirect("index")
        messages.success(request, "You do not have permission to access this page.")
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user = get_object_or_404(User, id=ticket.user_id.id)
    # draw = get_object_or_404(Drawing, id=ticket.drawing_id.id)

    if request.method == "POST":
        correct_number = request.POST.getlist("ball_numbers")
        special_number = request.POST.get("special_number")

        winningpick = WinningPick(
            ticket=ticket,
            special_number=special_number,
        )
        winningpick.save()
        for ball in correct_number:
            winningpick.correct_number.add(BallNumbers.objects.create(ball=ball))
        ticket.correct_count = True
        ticket.winning = winningpick
        if ticket.draw_type == "bronze" and not ticket.bronze.winning_set:
            bronze = get_object_or_404(Bronze, id=ticket.bronze.id)
            bronze.winning_set = True
            game_id = bronze.id
            bronze.save()
        elif ticket.draw_type == "silver" and not ticket.silver.winning_set:
            silver = get_object_or_404(Silver, id=ticket.silver.id)
            silver.winning_set = True
            game_id = silver.id
            silver.save()
        elif ticket.draw_type == "gold" and not ticket.gold.winning_set:
            gold = get_object_or_404(Gold, id=ticket.gold.id)
            gold.winning_set = True
            game_id = gold.id
            gold.save()
        elif ticket.draw_type == "platinum" and not ticket.platinum.winning_set:
            platinum = get_object_or_404(Platinum, id=ticket.platinum.id)
            platinum.winning_set = True
            game_id = platinum.id
            platinum.save()
        elif ticket.draw_type == "jackpot" and not ticket.jackpot.winning_set:
            jackpot = get_object_or_404(Jackpot, id=ticket.jackpot.id)
            jackpot.winning_set = True
            game_id = jackpot.id
            jackpot.save()
        elif ticket.draw_type == "megawin" and not ticket.megawin.winning_set:
            megawin = get_object_or_404(Megawin, id=ticket.megawin.id)
            megawin.winning_set = True
            game_id = jackpot.id
            megawin.save()
        else:
            messages.warning(request, f"winner has already been set for that game.")
            return redirect("admin_index", request.user.username)

        ticket.save()

        subject = f"Winner for gameID:{game_id} TYPE:{ticket.draw_type}"
        email = f"{user.email}"
        message = f"""Ticket with CODE: {ticket.ticket_code} has won the game
        GameID:{game_id}
        type: {ticket.draw_type}
        Visit your profile for all necessary updates.

        signed
        swmlottery team.
        """
        send_mail(subject, message, "Lttrglbl@gmail.com", [email], fail_silently=True)
        messages.success(request, f"{user.username} has been confirmed as winner.")
        return redirect("admin_index", request.user.username)

    w_form = WinnerForm()
    context = {"user": user, "ticket": ticket, "w_form": w_form}
    return render(request, "adminapp/winner.html", context)
