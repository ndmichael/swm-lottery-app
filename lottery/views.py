from django.shortcuts import render
from .forms import DrawForm, ContactForm

# Create your views here.


def index(request):
    return render(request, "lottery/index.html")


def games(request):
    return render(request, "lottery/games.html")

def about(request):
    return render(request, "lottery/about.html")

def contact(request):
    form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "lottery/contact.html", context)

def draw(request):
    context ={
        'form': DrawForm
    }
    return render(request, "lottery/draw.html", context)
