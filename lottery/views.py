from django.shortcuts import render, get_object_or_404
from .forms import DrawForm, ContactForm
from .models import Drawing
import json

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


def draw(request, type, id):
    draw = get_object_or_404(Drawing, id=id)
    context = {"form": DrawForm, "draw": draw}
    return render(request, "lottery/draw.html", context)
