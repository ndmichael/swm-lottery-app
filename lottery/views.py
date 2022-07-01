from django.shortcuts import render, get_object_or_404, redirect
from .forms import PickForm, ContactForm
from .models import Drawing, Ticket, Pick, BallNumbers
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.template import loader
import json
from django.core.mail import send_mail

# Create your views here.


def index(request):
    bronze_data = Drawing.objects.filter(type="bronze", status=True).first()
    silver_data = Drawing.objects.filter(status=True).filter(type="silver").first()
    gold_data = Drawing.objects.filter(status=True).filter(type="gold").first()
    platinum_data = Drawing.objects.filter(status=True).filter(type="platinum").first()
    b_enddate = bronze_data.enddate.strftime("%Y-%m-%dT%H:%M:%S")
    s_enddate = silver_data.enddate.strftime("%Y-%m-%dT%H:%M:%S")
    g_enddate = gold_data.enddate.strftime("%Y-%m-%dT%H:%M:%S")
    p_enddate = platinum_data.enddate.strftime("%Y-%m-%dT%H:%M:%S")

    context = {
        "b_enddate": b_enddate,
        "s_enddate": s_enddate,
        "g_enddate": g_enddate,
        "p_enddate": p_enddate,
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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            send_mail(
                subject,
                message,
                email,
                ["Lttrglbl@gmail.com"],
            )
            messages.success(request, "Mail successfully sent.")
            redirect("all-games")
    form = ContactForm()

    context = {"form": form}
    return render(request, "lottery/contact.html", context)


@login_required
def draw(request, type, id):
    draw = get_object_or_404(Drawing, id=id)
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        ball_numbers = request.POST.getlist("ball_numbers")
        special_number = request.POST.get("special_number")
        print(ball_numbers)
        if draw.type == "bronze" and user.profile.balance >= 100:
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=draw.type, drawing_id=draw
            )
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            for ball in ball_numbers:
                picks.ball_numbers.add(BallNumbers.objects.create(ball=ball))
            user.profile.balance -= 100
            user.profile.save()
        elif draw.type == "silver" and user.profile.balance >= 200:
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=draw.type, drawing_id=draw
            )
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            for ball in ball_numbers:
                picks.ball_numbers.add(BallNumbers.objects.create(ball=ball))
            user.profile.balance -= 200
            user.profile.save()
        elif draw.type == "gold" and user.profile.balance >= 350:
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=draw.type, drawing_id=draw
            )
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            for ball in ball_numbers:
                picks.ball_numbers.add(BallNumbers.objects.create(ball=ball))
            user.profile.balance -= 350
            user.profile.save()
        elif draw.type == "platinum" and user.profile.balance >= 500:
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=draw.type, drawing_id=draw
            )
            picks = Pick(
                user_id=user,
                ticket_id=ticket,
                special_number=special_number,
            )
            ticket.save()
            picks.save()
            for ball in ball_numbers:
                picks.ball_numbers.add(BallNumbers.objects.create(ball=ball))
            user.profile.balance -= 500
            user.profile.save()
        else:
            messages.warning(request, f"Insufficient balance.")
            return redirect("initiate-payment")
        messages.success(request, f"{ticket.ticket_code} has been confirmed for game.")
        return redirect("profile", request.user)

    form = PickForm()
    context = {"form": form, "draw": draw}
    return render(request, "lottery/draw.html", context)


def faq(request):
    return render(request, "lottery/faq.html")


def bonus(request):
    return render(request, "lottery/bonus.html")


def result(request):
    return render(request, "lottery/result.html")


def reset_draw(request):
    if request.POST.get("action") == "post":
        drawid = int(request.POST.get("draw_id"))
        draw = get_object_or_404(Drawing, id=drawid)
        draw.status = False
        draw.save()

        new_draw = Drawing.objects.create(type=draw.type, status=True)
        return JsonResponse({"result": new_draw.enddate})

    return HttpResponse("Error access denied")
