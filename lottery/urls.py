from django.urls import path
from .views import index, games, draw, contact, about


urlpatterns = [
    path('', index, name="index"),
    path('games/', games, name="all-games"),
    path('games/draws/', draw, name="pick"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
]