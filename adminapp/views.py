from django.shortcuts import render
from lottery.models import Ticket, Drawing

# Create your views here.


def index(request, username):
    return render(request, "adminapp/index.html")


def admin_games(request, game_type):
    if game_type == "bronze":
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(draw_type=game_type).order_by("-date")
        print(details)

    elif game_type == "silver":
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(drawing_type=game_type).order_by("-date")

    elif game_type == "gold":
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(drawing_type=game_type).order_by("-date")

    else:
        draw = Drawing.objects.get(type=game_type, status=True)
        details = Ticket.objects.filter(drawing_id=game_type).order_by("-date")

    context = {"details": details, "type": game_type}
    return render(request, "adminapp/admin_games.html", context)
