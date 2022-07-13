from django.shortcuts import render, get_object_or_404, redirect
from .forms import PickForm, ContactForm
from .models import (
    Drawing,
    Ticket,
    Pick,
    BallNumbers,
    WinningPick,
    Bronze,
    Silver,
    Gold,
    Platinum,
    Jackpot,
    Megawin,
)
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.template import loader
import json
from django.core.mail import send_mail
import datetime
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    # bronze_data = Drawing.objects.filter(type="bronze", status=True).first()
    bronze_data = Bronze.objects.filter(status=True).first()
    silver_data = Silver.objects.filter(status=True).first()
    gold_data = Gold.objects.filter(status=True).first()
    platinum_data = Platinum.objects.filter(status=True).first()
    jackpot_data = Jackpot.objects.filter(status=True).first()
    mega_data = Megawin.objects.filter(status=True).first()

    context = {
        "b_data": bronze_data,
        "s_data": silver_data,
        "g_data": gold_data,
        "p_data": platinum_data,
        "j_data": jackpot_data,
        "m_data": mega_data,
    }
    return render(request, "lottery/index.html", context)


def games(request):
    context = {"title": "swm-all games"}
    return render(request, "lottery/games.html", context)


def about(request):
    return render(request, "lottery/about.html")


def receipt(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    context = {"ticket": ticket}
    return render(request, "lottery/receipt.html", context)


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
            return redirect("all-games")
    form = ContactForm()

    context = {"form": form}
    return render(request, "lottery/contact.html", context)


@login_required
def draw(request, type, id):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        ball_numbers = request.POST.getlist("ball_numbers")
        special_number = request.POST.get("special_number")
        print(ball_numbers)
        if type == "bronze" and user.profile.balance >= 100:
            bronze = get_object_or_404(Bronze, id=id)
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=type, bronze=bronze
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
        elif type == "silver" and user.profile.balance >= 200:
            silver = get_object_or_404(Silver, id=id)
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=type, silver=silver
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
        elif type == "gold" and user.profile.balance >= 350:
            gold = get_object_or_404(Gold, id=id)
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=type, gold=gold
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
        elif type == "platinum" and user.profile.balance >= 500:
            platinum = get_object_or_404(Platinum, id=id)
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=type, platinum=platinum
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

        elif type == "jackpot" and user.profile.balance >= 300:
            jackpot = get_object_or_404(Jackpot, id=id)
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=type, jackpot=jackpot
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
            user.profile.balance -= 300
            user.profile.save()

        elif type == "megawin" and user.profile.balance >= 400:
            megawin = get_object_or_404(Megawin, id=id)
            ticket = Ticket.objects.create(
                user_id=user, status=True, draw_type=type, megawin=megawin
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
            user.profile.balance -= 400
            user.profile.save()
        else:
            messages.warning(request, f"Insufficient balance.")
            return redirect("initiate-payment")
        messages.success(request, f"{ticket.ticket_code} has been confirmed for game.")
        return redirect("profile", request.user)
    draw_type = type
    form = PickForm()
    context = {"form": form, "draw_type": draw_type}
    return render(request, "lottery/draw.html", context)


def faq(request):
    return render(request, "lottery/faq.html")


def bonus(request):
    return render(request, "lottery/bonus.html")


def result(request):

    bronze_result = WinningPick.objects.filter(ticket__draw_type="bronze").last()
    silver_result = WinningPick.objects.filter(
        ticket__draw_type="silver",
    ).last()
    gold_result = WinningPick.objects.filter(
        ticket__draw_type="gold",
    ).last()
    platinum_result = WinningPick.objects.filter(
        ticket__draw_type="platinum",
    ).last()
    jackpot_result = WinningPick.objects.filter(
        ticket__draw_type="jackpot",
    ).last()
    megawin_result = WinningPick.objects.filter(
        ticket__draw_type="megawin",
    ).last()
    context = {
        "bronze_result": bronze_result,
        "silver_result": silver_result,
        "gold_result": gold_result,
        "plat_result": platinum_result,
        "jackpot_result": jackpot_result,
        "megawin_result": megawin_result,
        "title": "swm-results",
    }
    return render(request, "lottery/result.html", context)


def reset_bronze(request):
    id = request.POST.get("draw_id")
    draw = Drawing.objects.filter(type="bronze").first()
    if request.POST.get("action") == "post" and id != "":
        bronze = get_object_or_404(Bronze, id=id)
        if datetime.datetime.now() == bronze.enddate:
            bronze.status = False
            bronze.save()  # set it to false then save.
            Bronze.objects.create(draw=draw, status=True)
            return JsonResponse({"result": "Bronze updated successful"})

    return HttpResponse("Error access denied")


def reset_silver(request):
    id = request.POST.get("draw_id")
    draw = Drawing.objects.filter(type="silver").first()

    if request.POST.get("action") == "post" and id != "":
        silver = get_object_or_404(Silver, id=id)
        if datetime.datetime.now() == silver.enddate:
            silver.status = False
            silver.save()  # set it to false then save.
            Silver.objects.create(draw=draw, status=True)
            return JsonResponse({"result": "Silver updated successful"})

    return HttpResponse("Error access denied")


def reset_gold(request):
    id = request.POST.get("draw_id")
    draw = Drawing.objects.filter(type="gold").first()

    if request.POST.get("action") == "post" and id != "":
        gold = get_object_or_404(Gold, id=id)
        if datetime.datetime.now() == gold.enddate:
            gold.status = False
            gold.save()  # set it to false then save.
            Gold.objects.create(draw=draw, status=True)
            return JsonResponse({"result": "gold updated successful"})

    return HttpResponse("Error access denied")


def reset_platinum(request):
    id = request.POST.get("draw_id")
    draw = Drawing.objects.filter(type="platinum").first()
    if request.POST.get("action") == "post" and id != "":
        platinum = get_object_or_404(Platinum, id=id)
        if datetime.datetime.now() == platinum.enddate:
            platinum.status = False
            platinum.save()  # set it to false then save.
            Platinum.objects.create(draw=draw, status=True)
            return JsonResponse({"result": "platinum updated successful"})

    return HttpResponse("Error access denied")


def reset_jackpot(request):
    id = request.POST.get("draw_id")
    draw = Drawing.objects.filter(type="jackpot").first()
    if request.POST.get("action") == "post" and id != "":
        jackpot = get_object_or_404(Jackpot, id=id)
        if datetime.datetime.now() == jackpot.enddate:
            jackpot.status = False
            jackpot.save()  # set it to false then save.
            Jackpot.objects.create(draw=draw, status=True)
            return JsonResponse({"result": "jackpot updated successful"})

    return HttpResponse("Error access denied")


def reset_megawin(request):
    id = request.POST.get("draw_id")
    draw = Drawing.objects.filter(type="megawin").first()
    if request.POST.get("action") == "post" and id != "":
        megawin = get_object_or_404(Jackpot, id=id)
        if datetime.datetime.now() == megawin.enddate:
            megawin.status = False
            megawin.save()  # set it to false then save.
            Megawin.objects.create(draw=draw, status=True)
            return JsonResponse({"result": "megawin updated successful"})

    return HttpResponse("Error access denied")


def result_details(request, type):
    if type == "bronze":
        p = Paginator(
            WinningPick.objects.filter(ticket__draw_type=type).order_by("-date"), 20
        )
        page = request.GET.get("page")
        results = p.get_page(page)
    elif type == "silver":
        p = Paginator(
            WinningPick.objects.filter(ticket__draw_type=type).order_by("-date"), 20
        )
        page = request.GET.get("page")
        results = p.get_page(page)
    elif type == "gold":
        p = Paginator(
            WinningPick.objects.filter(ticket__draw_type=type).order_by("-date"), 20
        )
        page = request.GET.get("page")
        results = p.get_page(page)
    elif type == "platinum":
        p = Paginator(
            WinningPick.objects.filter(ticket__draw_type=type).order_by("-date"), 20
        )
        page = request.GET.get("page")
        results = p.get_page(page)
    elif type == "jackpot":
        p = Paginator(
            WinningPick.objects.filter(ticket__draw_type=type).order_by("-date"), 20
        )
        page = request.GET.get("page")
        results = p.get_page(page)
    elif type == "megawin":
        p = Paginator(
            WinningPick.objects.filter(ticket__draw_type=type).order_by("-date"), 20
        )
        page = request.GET.get("page")
        results = p.get_page(page)
    result_type = type
    context = {"results": results, "title": "swm-results", "result_type": result_type}
    return render(request, "lottery/result_details.html", context)


def terms(request):
    context = {"title": "Terms & Conditions"}
    return render(request, "lottery/terms.html", context)
