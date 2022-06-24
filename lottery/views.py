from django.shortcuts import render, get_object_or_404, redirect
from .forms import PickForm, ContactForm
from .models import Drawing, Ticket, Pick
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    obj = Drawing.objects.filter(status=True).first()
    bronze_data = Drawing.objects.filter(status=True).filter(type="bronze").first()
    silver_data = Drawing.objects.filter(status=True).filter(type="silver").first()
    gold_data = Drawing.objects.filter(status=True).filter(type="gold").first()
    platinum_data = Drawing.objects.filter(status=True).filter(type="platinum").first()
    startdate = obj.created.strftime("%Y-%m-%dT%H:%M:%S")
    enddate = obj.enddate().strftime("%Y-%m-%dT%H:%M:%S")
    print(startdate, enddate)
    context = {
        "startdate": startdate,
        "enddate": enddate,
        "b_data": bronze_data,
        "s_data": silver_data,
        "g_data": gold_data,
        "p_data": platinum_data,
    }
    return render(request, "lottery/index.html", context)


def games(request):
    bronze_data = Drawing.objects.filter(status=True).filter(type="bronze").first()
    silver_data = Drawing.objects.filter(status=True).filter(type="silver").first()
    gold_data = Drawing.objects.filter(status=True).filter(type="gold").first()
    platinum_data = Drawing.objects.filter(status=True).filter(type="platinum").first()
    context = {
        "b_data": bronze_data,
        "s_data": silver_data,
        "g_data": gold_data,
        "p_data": platinum_data,
    }
    return render(request, "lottery/games.html", context)


def about(request):
    return render(request, "lottery/about.html")


def contact(request):
    form = ContactForm()

    context = {"form": form}
    return render(request, "lottery/contact.html", context)


@login_required
def draw(request, type, id):
    draw = get_object_or_404(Drawing, id=id)
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        ball_number = request.POST.getlist("ball_number")
        special_number = request.POST.getlist("special_number")
        print("len: ", len(special_number))
        if draw.type == "bronze" and user.profile.balance >= 100:
            ticket = Ticket.objects.create(user_id=user, status=True, drawing_id=draw)
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                ball_number=ball_number,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            user.profile.balance -= 100
            user.profile.save()

        elif draw.type == "silver" and user.profile.balance >= 200:
            ticket = Ticket.objects.create(user_id=user, status=True, drawing_id=draw)
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                ball_number=ball_number,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            user.profile.balance -= 200
            user.profile.save()
        elif draw.type == "gold" and user.profile.balance >= 350:
            ticket = Ticket.objects.create(user_id=user, status=True, drawing_id=draw)
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                ball_number=ball_number,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            user.profile.balance -= 350
            user.profile.save()
        elif draw.type == "platinum" and user.profile.balance >= 500:
            ticket = Ticket.objects.create(user_id=user, status=True, drawing_id=draw)
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                ball_number=ball_number,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            user.profile.balance -= 500
            user.profile.save()
        else:
            messages.warning(request, f"Insufficient balance.")
            return redirect("initiate-payment")
        messages.success(request, f"{ticket.ticket_code} has been confirmed for game.")

    form = PickForm()
    context = {"form": form, "draw": draw}
    return render(request, "lottery/draw.html", context)
