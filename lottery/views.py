from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "lottery/index.html")


def games(request):
    return render(request, "lottery/games.html")
